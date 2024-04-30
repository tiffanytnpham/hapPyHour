import json
import pygame
import os
import datetime
from pet import Pet
from config import Config


class GameManager:
    def __init__(self):
        """Initialize the GameManager, handling game state management and timing of updates."""
        self.pet = Pet()
        self.game_loaded = False
        self.state_valid_for_save = False
        self.load_game()
        pygame.time.set_timer(pygame.USEREVENT + 1, 3600000)  # Set for hourly updates

    def save_game(self, filename="game_save.json"):
        """Save the current state of the game to a JSON file, including a timestamp."""
        if not self.state_valid_for_save:
            print("Game state not valid for saving yet.")
            return

        game_data = {
            "name": self.pet.name,
            "food": self.pet.food,
            "happiness": self.pet.happiness,
            "health": self.pet.health,
            "is_asleep": self.pet.is_asleep,
            "last_saved": datetime.datetime.now().isoformat(),
        }

        with open(filename, "w") as f:
            json.dump(game_data, f, indent=4)
        print("Game state saved.")

    def load_game(self, filename="game_save.json"):
        """Load the game state from a file or initialize a new state if the file doesn't exist."""
        try:
            with open(filename, "r") as f:
                game_data = json.load(f)
            if game_data:
                self.set_game_state(game_data)
        except FileNotFoundError:
            self.create_initial_game_state()

    def set_game_state(self, game_data):
        """Update the game state from loaded data, including simulating missed time."""
        last_saved = datetime.datetime.fromisoformat(game_data["last_saved"])
        elapsed_time = datetime.datetime.now() - last_saved
        hours_passed = int(elapsed_time.total_seconds() // 3600)
        print(f"Loading game... Hours passed since last save: {hours_passed}")

        # Set the pet's attributes based on the loaded game data before updating.
        self.pet.name = game_data["name"]
        self.pet.food = game_data["food"]
        self.pet.happiness = game_data["happiness"]
        self.pet.health = game_data["health"]
        self.pet.is_asleep = game_data.get("is_asleep", False)

        # Update based on time passed since last save
        for _ in range(hours_passed):
            self.pet.update_hourly()

        self.state_valid_for_save = True
        self.save_game()
        self.game_loaded = True

        print(
            f"After update for {self.pet.name} - Food: {self.pet.food}, Happiness: {self.pet.happiness}, Health: {self.pet.health}, Asleep: {self.pet.is_asleep}")

    def create_initial_game_state(self):
        """Initialize a new game state and save it, marking as not loaded."""
        self.pet = Pet()
        self.save_game()
        self.game_loaded = False
        self.state_valid_for_save = False
        print("Initial game state created and saved.")

    def handle_event(self, event):
        """Respond to timed updates for the pet's state."""
        if event.type == pygame.USEREVENT + 1:
            print("Hourly update event triggered")
            self.pet.update_hourly()
            self.save_game()
