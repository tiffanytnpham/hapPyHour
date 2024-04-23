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

    # Font settings
    FONT_NAME = "sunnyspellsregular"
    FONT_SIZE = 20

    # Paths
    BACKGROUND_PATH = "Sprites/back.jpg"
    LOGO_PATH = "Sprites/logo.png"
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

    START_BUTTON_POSITION = pygame.Rect(SCREEN_WIDTH // 2 - 70, 350, 140, 50)

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
