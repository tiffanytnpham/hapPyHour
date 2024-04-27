import pygame
import os
class Config:
    # Screen dimensions
    SCREEN_WIDTH = 512
    SCREEN_HEIGHT = 512

    # Colors
    WHITE = (255, 255, 255)
    PINK = (225, 158, 176)
    BLUE = (212, 223, 230)
    GREEN = (185, 212, 199)
    GREY = (193, 193, 193)
    YELLOW = (244, 226, 178)
    PURPLE = (223, 186, 255)

    # Font settings
    FONT_NAME = "sunnyspellsregular"
    FONT_SIZE = 20

    # Background Paths
    BACKGROUND_PATH = "Sprites/back.jpg"
    LOGO_PATH = "Sprites/logo.png"

    # Button paths
    CONTINUE_PATH = "Sprites/Button/continue.png"
    CONTINUE_HOVER_PATH = "Sprites/Button/continue_hover.png"
    NEW_GAME_PATH = "Sprites/Button/new_game.png"
    NEW_GAME_HOVER_PATH = "Sprites/Button/new_game_hover.png"
    FEED_PATH = "Sprites/Button/feed.png"
    FEED_HOVER_PATH = "Sprites/Button/feed_hover.png"
    HAPPY_PATH = "Sprites/Button/happy.png"
    HAPPY_HOVER_PATH = "Sprites/Button/happy_hover.png"
    PLAY_PATH = "Sprites/Button/play.png"
    PLAY_HOVER_PATH = "Sprites/Button/play_hover.png"
    SLEEP_PATH = "Sprites/Button/sleep.png"
    SLEEP_HOVER_PATH = "Sprites/Button/sleep_hover.png"
    BACK_PATH = "Sprites/Button/back.png"
    BACK_HOVER_PATH = "Sprites/Button/back_hover.png"

    # Pet paths
    HAPPY1_PATH = "Sprites/Level1/Happy/happy1.png"
    HAPPY2_PATH = "Sprites/Level1/Happy/happy2.png"
    HAPPY3_PATH = "Sprites/Level1/Happy/happy3.png"

    UNHAPPY1_PATH = "Sprites/Level1/Unhappy/unhappy1.png"
    UNHAPPY2_PATH = "Sprites/Level1/Unhappy/unhappy2.png"
    UNHAPPY3_PATH = "Sprites/Level1/Unhappy/unhappy3.png"

    IDLE1_PATH = "Sprites/Level1/Idle/idle1.png"
    IDLE2_PATH = "Sprites/Level1/Idle/idle2.png"
    IDLE3_PATH = "Sprites/Level1/Idle/idle3.png"
    IDLE4_PATH = "Sprites/Level1/Idle/idle4.png"

    # Health paths
    FULL_HEART_PATH = "Sprites/Bars/full_heart.png"
    EMPTY_HEART_PATH = "Sprites/Bars/empty_heart.png"

    FOOD_GRID_PATH = "Sprites/Food/food_grid.png"
    TOY_GRID_PATH = "Sprites/Toy/toy_grid.png"

    buttons = {}

    # Helper method for loading images
    @staticmethod
    def load_image(path, alpha=False):
        """Loads an image from the specified path."""
        if os.path.exists(path):
            if alpha:
                return pygame.image.load(path).convert_alpha()
            return pygame.image.load(path).convert()
        else:
            print(f"Image not found: {path}")
            return None
