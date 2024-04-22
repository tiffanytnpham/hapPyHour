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

    # Button settings
    START_BUTTON_COLOR = PINK
    START_BUTTON_POSITION = pygame.Rect(SCREEN_WIDTH // 2 - 70, 350, 140, 50)
    START_BUTTON_TEXT = "Start!"

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
