import pygame
from config import Config

class Food:
    def __init__(self, name, image_path, hunger_value, alpha=True):
        self.name = name
        self.image = self.load_image(image_path, alpha)
        self.hunger_value = hunger_value
        self.rect = self.image.get_rect()

    def load_image(self, path, alpha):
        """Loads an image and optionally converts it to a format with an alpha channel."""
        image = pygame.image.load(path)
        if alpha:
            image = image.convert_alpha()
        else:
            image = image.convert()
        return image

    def draw(self, screen, position):
        """Draws the food item on the screen at the given position."""
        self.rect.topleft = position
        screen.blit(self.image, self.rect)
