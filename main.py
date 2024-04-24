import pygame
import os

from button import Button
from pet import Pet
from config import Config
from gamemanager import GameManager


def change_state(new_state):
    global current_state
    current_state = new_state


def get_pet_sprite(pet):
    state = pet.determine_state()
    current_time = pygame.time.get_ticks()

    if state == 'happy':
        index = (current_time // 500) % 3
        if index == 0:
            return Config.load_image(Config.HAPPY1_PATH, alpha=True)
        elif index == 1:
            return Config.load_image(Config.HAPPY2_PATH, alpha=True)
        else:
            return Config.load_image(Config.HAPPY3_PATH, alpha=True)
    elif state == 'unhappy':
        index = (current_time // 500) % 3
        if index == 0:
            return Config.load_image(Config.UNHAPPY1_PATH, alpha=True)
        elif index == 1:
            return Config.load_image(Config.UNHAPPY2_PATH, alpha=True)
        else:
            return Config.load_image(Config.UNHAPPY3_PATH, alpha=True)
    else:
        index = (current_time // 500) % 4
        if index == 0:
            return Config.load_image(Config.IDLE1_PATH, alpha=True)
        elif index == 1:
            return Config.load_image(Config.IDLE2_PATH, alpha=True)
        elif index == 2:
            return Config.load_image(Config.IDLE3_PATH, alpha=True)
        else:
            return Config.load_image(Config.IDLE4_PATH, alpha=True)


# Initialize the pygame library
pygame.init()

# Setup the display window based on configurations
screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))

# Set the window title
pygame.display.set_caption("HapPy Hour")

# Create an instance of GameManager and load any existing game data
game_manager = GameManager()

# Load backgrounds
start_background = Config.load_image(Config.BACKGROUND_PATH)
game_background = Config.load_image(Config.BACKGROUND_PATH)
logo = Config.load_image(Config.LOGO_PATH, alpha=True)

# Main menu buttons
continue_normal = Config.load_image(Config.CONTINUE_PATH, alpha=True)
continue_hover = Config.load_image(Config.CONTINUE_HOVER_PATH, alpha=True)

# Game scene buttons
feed_normal = Config.load_image(Config.FEED_PATH, alpha=True)
feed_hover = Config.load_image(Config.FEED_HOVER_PATH, alpha=True)
happy_normal = Config.load_image(Config.HAPPY_PATH, alpha=True)
happy_hover = Config.load_image(Config.HAPPY_HOVER_PATH, alpha=True)
play_normal = Config.load_image(Config.PLAY_PATH, alpha=True)
play_hover = Config.load_image(Config.PLAY_HOVER_PATH, alpha=True)
sleep_normal = Config.load_image(Config.SLEEP_PATH, alpha=True)
sleep_hover = Config.load_image(Config.SLEEP_HOVER_PATH, alpha=True)
back_normal = Config.load_image(Config.BACK_PATH, alpha=True)
back_hover = Config.load_image(Config.BACK_HOVER_PATH, alpha=True)



start_button = Button(202, 300, continue_normal, continue_hover, action=lambda: change_state('innit'))
feed_button = Button(37, 450, feed_normal, feed_hover, action=lambda: change_state('feed'))
happy_button = Button(161, 450, happy_normal, happy_hover, action=lambda: change_state('happy'))
play_button = Button(300, 450, play_normal, play_hover, action=lambda: change_state('play'))
sleep_button = Button(410, 450, sleep_normal, sleep_hover, action=lambda: change_state('sleep'))
back_button = Button(425, 10, back_normal, back_hover, action=lambda: change_state('game'))


# Configure the font
small_font = pygame.font.SysFont(Config.FONT_NAME, Config.FONT_SIZE)

# Determine the initial game state based on whether data was loaded
current_state = "main menu" if not game_manager.game_loaded else "game"

# Main game loop
running = True
while running:
    screen.fill(Config.BLUE)

    pet_sprite = get_pet_sprite(game_manager.pet)
    sprite_position = (Config.SCREEN_WIDTH // 2 - pet_sprite.get_width() // 2,
                       Config.SCREEN_HEIGHT // 2 - pet_sprite.get_height() // 2)

    # Render main menu
    if current_state == "main menu":
        if start_background:
            screen.blit(start_background, (0, 0))
        start_button.update()
        screen.blit(start_button.image, start_button.rect)
        if logo:
            screen.blit(logo, (10, 10))
        # Check for button press to switch to initialization state
        for event in pygame.event.get():
            start_button.handle_event(event)  # Handle button events
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.rect.collidepoint(mouse_pos):
                    current_state = "init"

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
            screen.blit(prompt_text,
                        (Config.SCREEN_WIDTH // 2 - prompt_text.get_width() // 2, Config.SCREEN_HEIGHT // 2 - 100))
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
        screen.blit(pet_sprite, sprite_position)

        pet_info_text = f"Name: {game_manager.pet.name}, Food: {game_manager.pet.food}, Happiness: {game_manager.pet.happiness}, Health: {game_manager.pet.health}"
        pet_info_render = small_font.render(pet_info_text, True, Config.WHITE)
        screen.blit(pet_info_render, (10, 10))

        feed_button.update()
        happy_button.update()
        play_button.update()
        sleep_button.update()
        back_button.update()

        screen.blit(feed_button.image, feed_button.rect)
        screen.blit(happy_button.image, happy_button.rect)
        screen.blit(play_button.image, play_button.rect)
        screen.blit(sleep_button.image, sleep_button.rect)


    elif current_state == "feed":
        screen.fill(Config.GREEN)
        screen.blit(pet_sprite, sprite_position)

        pet_info_text = f"Food: {game_manager.pet.food}"
        pet_info_render = small_font.render(pet_info_text, True, Config.WHITE)
        screen.blit(pet_info_render, (10, 10))

        back_button.update()
        screen.blit(back_button.image, back_button)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_button.rect.collidepoint(pygame.mouse.get_pos()):
                change_state("game")

    elif current_state == "happy":
        screen.fill(Config.YELLOW)
        screen.blit(pet_sprite, sprite_position)

        pet_info_text = f"Happiness: {game_manager.pet.happiness}, Health: {game_manager.pet.health}"
        pet_info_render = small_font.render(pet_info_text, True, Config.WHITE)
        screen.blit(pet_info_render, (10, 10))

        back_button.update()
        screen.blit(back_button.image, back_button)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_button.rect.collidepoint(pygame.mouse.get_pos()):
                change_state("game")

    elif current_state == "play":
        screen.fill(Config.PURPLE)
        screen.blit(pet_sprite, sprite_position)

        back_button.update()
        screen.blit(back_button.image, back_button)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_button.rect.collidepoint(pygame.mouse.get_pos()):
                change_state("game")

    elif current_state == "sleep":
        screen.fill(Config.GREY)
        screen.blit(pet_sprite, sprite_position)

        back_button.update()
        screen.blit(back_button.image, back_button)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_button.rect.collidepoint(pygame.mouse.get_pos()):
                change_state("game")

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Save the game and exit
            game_manager.save_game()
            running = False
        if current_state == "main menu":
            start_button.handle_event(event)
        elif current_state == "game":
            feed_button.handle_event(event)
            happy_button.handle_event(event)
            play_button.handle_event(event)
            sleep_button.handle_event(event)
            back_button.handle_event(event)

    pygame.display.flip()

pygame.quit()
