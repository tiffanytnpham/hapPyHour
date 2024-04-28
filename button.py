import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image, pressed_image, action=None):
        super().__init__()
        self.pressed = None
        self.original_image = image
        self.pressed_image = pressed_image
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.action = action
        self.clicked = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.image = self.pressed_image
            self.pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.pressed and self.rect.collidepoint(event.pos) and self.action:
                self.action()
            self.image = self.original_image if not self.rect.collidepoint(
                pygame.mouse.get_pos()) else self.pressed_image
            self.image = self.original_image
            self.pressed = False
