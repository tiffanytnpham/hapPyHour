import pygame
from config import Config


class Toy:
    def __init__(self, name, image_path, happy_value, alpha=True):
        """Initialize toy item with default values."""
        self.name = name
        self.image = self.load_image(image_path, alpha)
        self.happy_value = happy_value
        self.quantity = 1
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
        """Draws the toy item on the screen at the given position."""
        self.rect.topleft = position
        screen.blit(self.image, self.rect)
