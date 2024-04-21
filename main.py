import pygame
import os
from pet import Pet
from config import Config
from gamemanager import GameManager

# Initialize the pygame library
pygame.init()

# Setup the display window based on configurations
screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))

# Set the window title
pygame.display.set_caption("HapPy Hour")

# Create an instance of GameManager and load any existing game data
game_manager = GameManager()
game_manager.load_game()

# Load backgrounds
start_background = Config.load_image(Config.BACKGROUND_PATH)
game_background = Config.load_image(Config.BACKGROUND_PATH)
logo = Config.load_image(Config.LOGO_PATH, alpha=True)

# Configure the font
small_font = pygame.font.SysFont(Config.FONT_NAME, Config.FONT_SIZE)

# Determine the initial game state based on whether data was loaded
current_state = "main menu" if not game_manager.game_loaded else "game"

def draw_button(text, position, button_color):
    """Draw a button with text centered."""
    button_rect = pygame.Rect(position)
    pygame.draw.rect(screen, button_color, button_rect)
    text_render = small_font.render(text, True, Config.WHITE)
    text_rect = text_render.get_rect(center=button_rect.center)
    screen.blit(text_render, text_rect)

# Main game loop
running = True
while running:
    screen.fill(Config.BLUE)

    # Render main menu
    if current_state == "main menu":
        if start_background:
            screen.blit(start_background, (0, 0))
        draw_button(Config.START_BUTTON_TEXT, Config.START_BUTTON_POSITION, Config.START_BUTTON_COLOR)
        if logo:
            screen.blit(logo, (10, 10))

    # Handle initial game setup where player names their pet
    elif current_state == "init":
        input_box = pygame.Rect(Config.SCREEN_WIDTH // 2 - 100, Config.SCREEN_HEIGHT // 2 - 25, 200, 50)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''
        font = pygame.font.Font(None, 32)
        clock = pygame.time.Clock()

        # Loop to handle input events for naming the pet
        init_running = True
        while init_running:
            screen.fill(Config.PINK)  # Set the background for the input screen
            prompt_text = small_font.render("Name your pet!", True, (0, 0, 0))
            screen.blit(prompt_text, (Config.SCREEN_WIDTH // 2 - prompt_text.get_width() // 2, Config.SCREEN_HEIGHT // 2 - 100))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            game_manager.pet.set_name(text)
                            game_manager.save_game()
                            current_state = "game"
                            init_running = False
                        elif event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            quit()
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
            pygame.draw.rect(screen, color, input_box, 2)
            txt_surface = font.render(text, True, color)
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            pygame.display.flip()
            clock.tick(30)

    # Display game state with pet information
    elif current_state == "game":
        if game_background:
            screen.blit(game_background, (0, 0))
        pet_info_text = f"Name: {game_manager.pet.name}, Food: {game_manager.pet.food}, Happiness: {game_manager.pet.happiness}, Health: {game_manager.pet.health}"
        pet_info_render = small_font.render(pet_info_text, True, Config.WHITE)
        screen.blit(pet_info_render, (10, 10))

    # General event handling for the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_manager.save_game()
            running = False
        elif event.type == pygame.USEREVENT + 1:
            game_manager.handle_event(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if Config.START_BUTTON_POSITION.collidepoint(mouse_pos):
                if current_state == "main menu":
                    current_state = "init"  # Change to initialization state

    pygame.display.flip()

pygame.quit()
