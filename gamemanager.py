import json
import pygame
import os
from pet import Pet
from config import Config

class GameManager:
    def __init__(self):
        """Initialize the GameManager, which manages the state of the game."""
        self.pet = Pet()
        self.game_loaded = False
        self.load_game()
        # Set a timer event to trigger hourly updates to the game's state.
        pygame.time.set_timer(pygame.USEREVENT + 1, 3600000)  # 1 hour in milliseconds

    def save_game(self, filename='game_save.json'):
        """Save the current state of the game to a JSON file."""
        # Collect game state data in a dictionary.
        game_data = {
            'name': self.pet.name,
            'food': self.pet.food,
            'happiness': self.pet.happiness,
            'health': self.pet.health
        }
        # Open the specified file and dump the game data into it in JSON format.
        with open(filename, 'w') as f:
            json.dump(game_data, f, indent=4)

    def load_game(self, filename='game_save.json'):
        """Load the game state from a JSON file if it exists."""
        try:
            # Attempt to open and read the specified game save file.
            with open(filename, 'r') as f:
                game_data = json.load(f)
            # Set the pet's attributes based on the loaded game data.
            self.pet.name = game_data['name']
            self.pet.food = game_data['food']
            self.pet.happiness = game_data['happiness']
            self.pet.health = game_data['health']
            # Set the game_loaded flag to True if loading is successful.
            self.game_loaded = True
        except FileNotFoundError:
            # If the file is not found, print a message and start a new game.
            print("No existing game state found. Starting a new game.")

    def handle_event(self, event):
        """Handle specific events triggered by the pygame timer."""
        if event.type == pygame.USEREVENT + 1:
            # When the hourly event is triggered, update the pet's state.
            self.pet.update_hourly()
            # Save the game automatically after updating the pet's state.
            self.save_game()
