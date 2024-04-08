# Import the pygame module
import pygame
import os

# Only import what you need from pygame.locals
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
)

# Initialize pygame
pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 360

# Colors
WHITE = (255, 255, 255)
PINK = (225, 158, 176)
BLUE = (212, 223, 230)

# Font
small_font = pygame.font.SysFont("sunnyspellsregular", 20)

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("HapPy Hour")

# Load the start background image
start_background_path = "back.jpg"
start_background = None
if os.path.exists(start_background_path):
    start_background = pygame.image.load(start_background_path).convert()
else:
    print("Start background image not found:", start_background_path)

# Load the game background image
game_background_path = "back2.jpg"
game_background = None
if os.path.exists(game_background_path):
    game_background = pygame.image.load(game_background_path).convert()
else:
    print("Game background image not found:", game_background_path)

# Start button properties
start_button_color = PINK
start_button_position = (SCREEN_WIDTH / 2 - 70, SCREEN_HEIGHT / 2 - 25, 140, 50)
start_button_text = "Start!"

# Game state
current_state = "main menu"


# Function to draw the start button
def draw_button(text, position, start_button_color):
    pygame.draw.rect(screen, start_button_color, position)  # Draw the button
    text_render = small_font.render(text, True, WHITE)
    text_rect = text_render.get_rect(center=(position[0] + position[2] / 2, position[1] + position[3] / 2))
    screen.blit(text_render, text_rect)


# Main game loop
running = True
while running:
    # Clear the screen for the current frame
    screen.fill(BLUE)  # Default color fill

    if current_state == "main menu":
        # Use start_background for the main menu
        if start_background:
            screen.blit(start_background, (0, 0))
        draw_button(start_button_text, start_button_position, start_button_color)

    elif current_state == "game":
        # Use game_background for the game screen
        if game_background:
            screen.blit(game_background, (0, 0))
        else:
            game_screen_text = small_font.render('Game Screen - Press ESC to quit', True, PINK)
            screen.blit(game_screen_text, (20, 20))
    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:  # Check if the Escape key was pressed
                running = False
        elif event.type == MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # Gets the mouse position
            if (start_button_position[0] <= mouse_pos[0] <= start_button_position[0] + start_button_position[2]
                    and start_button_position[1] <= mouse_pos[1] <= start_button_position[1] + start_button_position[3]):
                if current_state == "main menu":  # Change to the game screen if start button pressed
                    current_state = "game"

    pygame.display.flip()

pygame.quit()
