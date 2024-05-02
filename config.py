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

    BGM_PATH = "bgm.wav"

    # Button paths
    CONTINUE_PATH = "Sprites/Button/continue.png"
    CONTINUE_HOVER_PATH = "Sprites/Button/continue_hover.png"
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
    GAME1_PATH = "Sprites/Button/game1.png"
    GAME1_HOVER_PATH = "Sprites/Button/game1_hover.png"
    GAME2_PATH = "Sprites/Button/game2.png"
    GAME2_HOVER_PATH = "Sprites/Button/game2_hover.png"
    X_PATH = "Sprites/Button/x.png"
    X_HOVER_PATH = "Sprites/Button/x_hover.png"

    # Level 1 Pet Paths
    L1_HAPPY1_PATH = "Sprites/Level1/Happy/happy1.png"
    L1_HAPPY2_PATH = "Sprites/Level1/Happy/happy2.png"
    L1_HAPPY3_PATH = "Sprites/Level1/Happy/happy3.png"

    L1_UNHAPPY1_PATH = "Sprites/Level1/Unhappy/unhappy1.png"
    L1_UNHAPPY2_PATH = "Sprites/Level1/Unhappy/unhappy2.png"
    L1_UNHAPPY3_PATH = "Sprites/Level1/Unhappy/unhappy3.png"

    L1_IDLE1_PATH = "Sprites/Level1/Idle/idle1.png"
    L1_IDLE2_PATH = "Sprites/Level1/Idle/idle2.png"
    L1_IDLE3_PATH = "Sprites/Level1/Idle/idle3.png"
    L1_IDLE4_PATH = "Sprites/Level1/Idle/idle4.png"

    L1_ASLEEP1_PATH = "Sprites/Level1/Asleep/asleep1.png"
    L1_ASLEEP2_PATH = "Sprites/Level1/Asleep/asleep2.png"
    L1_ASLEEP3_PATH = "Sprites/Level1/Asleep/asleep3.png"

    #Level 2 Pet Paths
    L2_HAPPY1_PATH = "Sprites/Level2/Happy/happy1.png"
    L2_HAPPY2_PATH = "Sprites/Level2/Happy/happy2.png"
    L2_HAPPY3_PATH = "Sprites/Level2/Happy/happy3.png"

    L2_UNHAPPY1_PATH = "Sprites/Level2/Unhappy/unhappy1.png"
    L2_UNHAPPY2_PATH = "Sprites/Level2/Unhappy/unhappy2.png"
    L2_UNHAPPY3_PATH = "Sprites/Level2/Unhappy/unhappy3.png"

    L2_IDLE1_PATH = "Sprites/Level2/Idle/idle1.png"
    L2_IDLE2_PATH = "Sprites/Level2/Idle/idle2.png"
    L2_IDLE3_PATH = "Sprites/Level2/Idle/idle3.png"
    L2_IDLE4_PATH = "Sprites/Level2/Idle/idle4.png"

    L2_ASLEEP1_PATH = "Sprites/Level2/Asleep/asleep1.png"
    L2_ASLEEP2_PATH = "Sprites/Level2/Asleep/asleep2.png"
    L2_ASLEEP3_PATH = "Sprites/Level2/Asleep/asleep3.png"

    #Level 3 Pet Paths
    L3_HAPPY1_PATH = "Sprites/Level3/Happy/happy1.png"
    L3_HAPPY2_PATH = "Sprites/Level3/Happy/happy2.png"
    L3_HAPPY3_PATH = "Sprites/Level3/Happy/happy3.png"

    L3_UNHAPPY1_PATH = "Sprites/Level3/Unhappy/unhappy1.png"
    L3_UNHAPPY2_PATH = "Sprites/Level3/Unhappy/unhappy2.png"
    L3_UNHAPPY3_PATH = "Sprites/Level3/Unhappy/unhappy3.png"

    L3_IDLE1_PATH = "Sprites/Level3/Idle/idle1.png"
    L3_IDLE2_PATH = "Sprites/Level3/Idle/idle2.png"
    L3_IDLE3_PATH = "Sprites/Level3/Idle/idle3.png"
    L3_IDLE4_PATH = "Sprites/Level3/Idle/idle4.png"

    L3_ASLEEP1_PATH = "Sprites/Level3/Asleep/asleep1.png"
    L3_ASLEEP2_PATH = "Sprites/Level3/Asleep/asleep2.png"
    L3_ASLEEP3_PATH = "Sprites/Level3/Asleep/asleep3.png"

    # Health paths
    FULL_HEART_PATH = "Sprites/Bars/full_heart.png"
    EMPTY_HEART_PATH = "Sprites/Bars/empty_heart.png"
    FULL_FISH_PATH = "Sprites/Bars/full_fish.png"
    EMPTY_FISH_PATH = "Sprites/Bars/empty_fish.png"
    FULL_PAW_PATH = "Sprites/Bars/full_paw.png"
    EMPTY_PAW_PATH = "Sprites/Bars/empty_paw.png"

    FOOD_GRID_PATH = "Sprites/Food/food_grid.png"
    TOY_GRID_PATH = "Sprites/Toy/toy_grid.png"

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
