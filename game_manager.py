import json
import pygame
import os
import datetime
from pet import Pet
from config import Config


class GameManager:
    def __init__(self, food_items, toy_items):
        """Initialize the GameManager, handling game state management and timing of updates."""
        self.pet = Pet()
        self.food_items = food_items
        self.toy_items = toy_items

        self.game_loaded = False
        self.state_valid_for_save = False
        self.load_game()
        self.initialize_audio(Config.BGM_PATH)
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
            "level": self.pet.level,
            "inventory": {item.name: item.quantity for item in self.food_items + self.toy_items},
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

        # Set the pet's attributes
        self.pet.name = game_data["name"]
        self.pet.food = game_data["food"]
        self.pet.happiness = game_data["happiness"]
        self.pet.health = game_data["health"]
        self.pet.level = game_data["level"]
        self.pet.is_asleep = game_data.get("is_asleep", False)

        # Update based on time passed
        for _ in range(hours_passed):
            self.pet.update_hourly()

        # Set inventory counts
        inventory_data = game_data.get("inventory", {})
        for item in self.food_items + self.toy_items:
            item.quantity = inventory_data.get(item.name, 0)

        self.state_valid_for_save = True
        self.save_game()
        self.game_loaded = True

        print(
            f"After update for {self.pet.name} - Food: {self.pet.food}, Happiness: {self.pet.happiness}, Health: {self.pet.health}, Level: {self.pet.level} Asleep: {self.pet.is_asleep}")

    def create_initial_game_state(self):
        """Initialize a new game state and save it, marking as not loaded."""
        self.pet = Pet()
        self.save_game()
        self.game_loaded = False
        self.state_valid_for_save = False
        print("Initial game state created and saved.")

    def initialize_audio(self, audio_file):
        """Load and play background music using Pygame's mixer."""
        pygame.mixer.init()  # Initialize the mixer
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play(-1)  # Play in a loop


    def handle_event(self, event):
        """Respond to timed updates for the pet's state."""
        if event.type == pygame.USEREVENT + 1:
            print("Hourly update event triggered")
            self.pet.update_hourly()
            self.save_game()