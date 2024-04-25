import pygame
from config import Config

class SpriteManager:
    def __init__(self):
        self.sprites = {
            "start_background": self.load_image(Config.BACKGROUND_PATH),
            "game_background": self.load_image(Config.BACKGROUND_PATH),
            "logo": self.load_image(Config.LOGO_PATH, alpha=True),
            "continue_normal": self.load_image(Config.CONTINUE_PATH, alpha=True),
            "continue_hover": self.load_image(Config.CONTINUE_HOVER_PATH, alpha=True),
            "feed_normal": self.load_image(Config.FEED_PATH, alpha=True),
            "feed_hover": self.load_image(Config.FEED_HOVER_PATH, alpha=True),
            "happy_normal": self.load_image(Config.HAPPY_PATH, alpha=True),
            "happy_hover": self.load_image(Config.HAPPY_HOVER_PATH, alpha=True),
            "play_normal": self.load_image(Config.PLAY_PATH, alpha=True),
            "play_hover": self.load_image(Config.PLAY_HOVER_PATH, alpha=True),
            "sleep_normal": self.load_image(Config.SLEEP_PATH, alpha=True),
            "sleep_hover": self.load_image(Config.SLEEP_HOVER_PATH, alpha=True),
            "back_normal": self.load_image(Config.BACK_PATH, alpha=True),
            "back_hover": self.load_image(Config.BACK_HOVER_PATH, alpha=True),
            "full_heart": self.load_image(Config.FULL_HEART_PATH, alpha=True),
            "empty_heart": self.load_image(Config.EMPTY_HEART_PATH, alpha=True),
            "peach": self.load_image("Sprites/Food/peach.png", alpha=True),
            "cherry": self.load_image("Sprites/Food/cherry.png", alpha=True),
            "pet_happy": [self.load_image("Sprites/Pet/happy1.png", alpha=True),
                          self.load_image("Sprites/Pet/happy2.png", alpha=True),
                          self.load_image("Sprites/Pet/happy3.png", alpha=True)],
            "pet_unhappy": [self.load_image("Sprites/Pet/unhappy1.png", alpha=True),
                            self.load_image("Sprites/Pet/unhappy2.png", alpha=True),
                            self.load_image("Sprites/Pet/unhappy3.png", alpha=True)],
            "pet_idle": [self.load_image("Sprites/Pet/idle1.png", alpha=True),
                         self.load_image("Sprites/Pet/idle2.png", alpha=True),
                         self.load_image("Sprites/Pet/idle3.png", alpha=True),
                         self.load_image("Sprites/Pet/idle4.png", alpha=True)]
        }

    def load_image(self, path, alpha=False):
        """Loads an image from the specified path with optional alpha transparency."""
        if alpha:
            return pygame.image.load(path).convert_alpha()
        return pygame.image.load(path).convert()

    def get_sprite(self, key):
        """Retrieve a sprite or list of sprites by key."""
        return self.sprites.get(key)

    def get_pet_sprite(self, state, current_time):
        """Retrieve the correct pet sprite based on state and animation frame."""
        if state == 'idle':
            index = (current_time // 500) % 4  # 4 frames for the idle state
        else:
            index = (current_time // 500) % 3  # 3 frames for happy or unhappy states

        return self.sprites[f"pet_{state}"][index]


