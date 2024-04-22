import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image, pressed_image, hover_image=None, action=None):
        super().__init__()
        self.image = image
        self.pressed_image = pressed_image
        self.hover_image = hover_image if hover_image else image
        self.original_image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.action = action
        self.pressed = False

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image = self.hover_image
        else:
            self.image = self.original_image

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.image = self.pressed_image
            self.pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.pressed and self.rect.collidepoint(event.pos) and self.action:
                self.action()
            self.image = self.original_image if not self.rect.collidepoint(pygame.mouse.get_pos()) else self.hover_image
            self.pressed = False

