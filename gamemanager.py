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
        self.load_game()
        pygame.time.set_timer(pygame.USEREVENT + 1, 3600000)  # Set for hourly updates

    def save_game(self, filename='game_save.json'):
        """Save the current state of the game to a JSON file, including a timestamp."""
        game_data = {
            'name': self.pet.name,
            'food': self.pet.food,
            'happiness': self.pet.happiness,
            'health': self.pet.health,
            'last_saved': datetime.datetime.now().isoformat()
        }
        with open(filename, 'w') as f:
            json.dump(game_data, f, indent=4)
        print("Game state saved.")

    def load_game(self, filename='game_save.json'):
        """Load the game state from a file or initialize new state if the file doesn't exist."""
        try:
            with open(filename, 'r') as f:
                game_data = json.load(f)
            if game_data:
                self.set_game_state(game_data)
        except FileNotFoundError:
            self.create_initial_game_state()

    def set_game_state(self, game_data):
        """Update the game state from loaded data, including simulating missed time."""
        last_saved = datetime.datetime.fromisoformat(game_data['last_saved'])
        elapsed_time = datetime.datetime.now() - last_saved
        hours_passed = elapsed_time.total_seconds() // 3600
        for _ in range(int(hours_passed)):
            self.pet.update_hourly()

        self.pet.name = game_data['name']
        self.pet.food = game_data['food']
        self.pet.happiness = game_data['happiness']
        self.pet.health = game_data['health']
        self.game_loaded = True

    def create_initial_game_state(self):
        """Initialize a new game state and save it, marking as not loaded."""
        self.pet = Pet()
        self.save_game()
        self.game_loaded = False
        print("Initial game state created and saved.")

    def handle_event(self, event):
        """Respond to timed updates for the pet's state."""
        if event.type == pygame.USEREVENT + 1:
            self.pet.update_hourly()
            self.save_game()