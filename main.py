import datetime
import subprocess
import os
import pygame

from button import Button
from food import Food
from config import Config
from game_manager import GameManager
from toy import Toy


def change_state(new_state):
    global current_state
    current_state = new_state


def get_pet_sprite(pet):
    state = pet.determine_state()
    LEVEL = pet.level
    current_time = pygame.time.get_ticks()
    if state == "happy":
        index = (current_time // 500) % 3
        if index == 0:   
            return Config.load_image(getattr(Config, f"L{LEVEL}_HAPPY1_PATH"), alpha=True)
        elif index == 1:
            return Config.load_image(getattr(Config, f"L{LEVEL}_HAPPY2_PATH"), alpha=True)
        else:
            return Config.load_image(getattr(Config, f"L{LEVEL}_HAPPY3_PATH"), alpha=True)
    elif state == "unhappy":
        index = (current_time // 500) % 3
        if index == 0:
            return Config.load_image(getattr(Config, f"L{LEVEL}_UNHAPPY1_PATH"), alpha=True)
        elif index == 1:
            return Config.load_image(getattr(Config, f"L{LEVEL}_UNHAPPY2_PATH"), alpha=True)
        else:
            return Config.load_image(getattr(Config, f"L{LEVEL}_UNHAPPY3_PATH"), alpha=True)
    elif state == "asleep":
        index = (current_time // 1000) % 3
        if index == 0:
            return Config.load_image(getattr(Config, f"L{LEVEL}_ASLEEP1_PATH"), alpha=True)
        elif index == 1:
            return Config.load_image(getattr(Config, f"L{LEVEL}_ASLEEP2_PATH"), alpha=True)
        else:
            return Config.load_image(getattr(Config, f"L{LEVEL}_ASLEEP3_PATH"), alpha=True)
    else:
        index = (current_time // 500) % 4
        if index == 0:
            return Config.load_image(getattr(Config, f"L{LEVEL}_IDLE1_PATH"), alpha=True)
        elif index == 1:
            return Config.load_image(getattr(Config, f"L{LEVEL}_IDLE2_PATH"), alpha=True)
        elif index == 2:
            return Config.load_image(getattr(Config, f"L{LEVEL}_IDLE3_PATH"), alpha=True)
        else:
            return Config.load_image(getattr(Config, f"L{LEVEL}_IDLE4_PATH"), alpha=True)

def initialize_buttons():
    """Initialize and return a dictionary of game buttons."""
    # Check if a game save file exists
    save_exists = os.path.exists("game_save.json")

    # Create the "New Game" button
    new_game_button = Button(
        202, 300,
        Config.load_image(Config.NEW_GAME_PATH, alpha=True),
        Config.load_image(Config.NEW_GAME_HOVER_PATH, alpha=True),
        action=start_new_game,
    )
    buttons = {"new_game": new_game_button}

    if save_exists:
        # Create the "Continue" button if a save file exists
        continue_button = Button(
            202, 350,
            Config.load_image(Config.CONTINUE_PATH, alpha=True),
            Config.load_image(Config.CONTINUE_HOVER_PATH, alpha=True),
            action=lambda: change_state("game"),
        )
        buttons["continue"] = continue_button

    # Create secondary buttons for the game scene
    buttons.update({
        "feed": Button(37, 450,
                       Config.load_image(Config.FEED_PATH, alpha=True),
                       Config.load_image(Config.FEED_HOVER_PATH, alpha=True),
                       action=lambda: change_state("feed")
                       ),
        "happy": Button(161, 450,
                        Config.load_image(Config.HAPPY_PATH, alpha=True),
                        Config.load_image(Config.HAPPY_HOVER_PATH, alpha=True),
                        action=lambda: change_state("happy")
                        ),
        "play": Button(300, 450,
                       Config.load_image(Config.PLAY_PATH, alpha=True),
                       Config.load_image(Config.PLAY_HOVER_PATH, alpha=True),
                       action=lambda: change_state("play")
                       ),
        "sleep": Button(410, 450,
                        Config.load_image(Config.SLEEP_PATH, alpha=True),
                        Config.load_image(Config.SLEEP_HOVER_PATH, alpha=True),
                        action=lambda: change_state("sleep")
                        ),
        "back": Button(425, 10,
                       Config.load_image(Config.BACK_PATH, alpha=True),
                       Config.load_image(Config.BACK_HOVER_PATH, alpha=True),
                       action=lambda: change_state("game")
                       ),
        "game1": Button(215, 205,
                        Config.load_image(Config.GAME1_PATH, alpha=True),
                        Config.load_image(Config.GAME1_HOVER_PATH, alpha=True),
                        action=lambda: subprocess.Popen(["python", "food_game.py"])
                        ),
        "game2": Button(215, 250,
                        Config.load_image(Config.GAME2_PATH, alpha=True),
                        Config.load_image(Config.GAME2_HOVER_PATH, alpha=None),
                        action=lambda: None
                        ),
        "x": Button(425, 10,
                    Config.load_image(Config.X_PATH, alpha=True),
                    Config.load_image(Config.X_HOVER_PATH, alpha=True),
                    action=lambda: None
                    ),
        "eat": Button(425, 460,
                      Config.load_image(Config.FEED_PATH, alpha=True),
                      Config.load_image(Config.FEED_HOVER_PATH, alpha=True),
                      action=give_item
                      ),
        "toy": Button(425, 460,
                      Config.load_image(Config.PLAY_PATH, alpha=True),
                      Config.load_image(Config.PLAY_HOVER_PATH, alpha=True),
                      action=give_item
                      ),
        "asleep": Button(425, 460,
                         Config.load_image(Config.SLEEP_PATH, alpha=True),
                         Config.load_image(Config.SLEEP_HOVER_PATH, alpha=True),
                         action=put_pet_to_sleep
                         ),
    })

    return buttons


def start_new_game():
    """Start a new game by clearing the current save file and reinitializing the game state."""
    if os.path.exists("game_save.json"):
        os.remove("game_save.json")
        print("Old save file deleted.")

    global game_manager
    game_manager.create_initial_game_state()

    change_state("init")


def draw_bar(screen, health, max_health, current_state):
    full_bar = None
    empty_bar = None
    bar_width = 0
    if current_state == "game":
        full_bar = Config.load_image(Config.FULL_HEART_PATH, alpha=True)
        empty_bar = Config.load_image(Config.EMPTY_HEART_PATH, alpha=True)
        bar_width = full_bar.get_width() + 18
    elif current_state == "feed":
        full_bar = Config.load_image(Config.FULL_FISH_PATH, alpha=True)
        empty_bar = Config.load_image(Config.EMPTY_FISH_PATH, alpha=True)
        bar_width = full_bar.get_width() + 18
    elif current_state == "happy":
        full_bar = Config.load_image(Config.FULL_PAW_PATH, alpha=True)
        empty_bar = Config.load_image(Config.EMPTY_PAW_PATH, alpha=True)
        bar_width = full_bar.get_width() + 18
    for i in range(max_health):
        heart_x = 15 + i * bar_width
        if i < health:
            screen.blit(full_bar, (heart_x, 10))
        else:
            screen.blit(empty_bar, (heart_x, 10))


def draw_inventory(screen, items, start_x, start_y, columns, cell_size, spacing):
    for index, item in enumerate(items):
        col = index % columns
        row = index // columns
        x = start_x + col * (cell_size + spacing)
        y = start_y + row * (cell_size + spacing)
        item.draw(screen, (x, y))


selected_food = None
selected_toy = None


def give_item():
    global selected_food
    global selected_toy
    if selected_food:
        game_manager.pet.feed(selected_food.hunger_value)
        print(f"Feeding {selected_food.name} increases food by {selected_food.hunger_value}")
        selected_food = None
    elif selected_toy:
        game_manager.pet.play(selected_toy.happy_value)
        print(f"Giving {selected_toy.name} increases happiness by {selected_toy.happy_value}")
        selected_toy = None


def put_pet_to_sleep():
    """Put the pet to sleep, manage its state, and save it."""
    current_hour = datetime.datetime.now().hour

    print(f"Putting the pet to sleep at hour {current_hour}.")
    game_manager.pet.sleep(current_hour)

    change_state("sleep")
    print(f"Pet is now asleep at {current_hour}.")


def handle_selection(mouse_pos, items, current_state):
    global selected_food
    global selected_toy
    for item in items:
        if item.rect.collidepoint(mouse_pos):
            if current_state == "feed":
                selected_food = item
                print(f"Selected {selected_food.name}")
                break
            elif current_state == "happy":
                selected_toy = item
                print(f"Selected {selected_toy.name}")
                break


# Initialize the pygame library
pygame.init()

# Set up the display window based on configurations
screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))

# Set the window title
pygame.display.set_caption("HapPy Hour")

# Create an instance of GameManager and load any existing game data
game_manager = GameManager()

# Load backgrounds
start_background = Config.load_image(Config.BACKGROUND_PATH)
game_background = Config.load_image(Config.BACKGROUND_PATH)
logo = Config.load_image(Config.LOGO_PATH, alpha=True)

# Initialize buttons
buttons = initialize_buttons()

new_game_button = buttons["new_game"]
continue_button = buttons.get("continue", None)
feed_button = buttons["feed"]
happy_button = buttons["happy"]
play_button = buttons["play"]
sleep_button = buttons["sleep"]
back_button = buttons["back"]
eat_button = buttons["eat"]
toy_button = buttons["toy"]
asleep_button = buttons["asleep"]
game1_button = buttons["game1"]
game2_button = buttons["game2"]
x_button = buttons["x"]

# Configure the font
small_font = pygame.font.SysFont(Config.FONT_NAME, Config.FONT_SIZE)

current_state = "main menu"

# Initialize food items
peach = Food("Peach", "Sprites/Food/peach.png", 1, alpha=True)
cherry = Food("Cherry", "Sprites/Food/cherry.png", 2, alpha=True)
fish = Food("Fish", "Sprites/Food/fish.png", 3, alpha=True)
food_items = [peach, cherry, fish]  # List of food items
food_grid = Config.load_image(Config.FOOD_GRID_PATH, alpha=True)

# Initialize toy items
feather = Toy("Feather", "Sprites/Toy/feather.png", 1, alpha=True)
yarn = Toy("Yarn", "Sprites/Toy/yarn.png", 2, alpha=True)
box = Toy("Box", "Sprites/Toy/box.png", 3, alpha=True)
toy_items = [feather, yarn, box]  # List of toy items
toy_grid = Config.load_image(Config.TOY_GRID_PATH, alpha=True)

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

        screen.blit(new_game_button.image, new_game_button.rect)
        if "continue" in buttons:
            screen.blit(continue_button.image, continue_button.rect)
        if logo:
            screen.blit(logo, (10, 10))
        for event in pygame.event.get():
            new_game_button.handle_event(event)
            if "continue" in buttons:
                continue_button.handle_event(event)
            if event.type == pygame.QUIT:
                running = False

    # Handle initial game setup where player names their pet
    elif current_state == "init":
        input_box = pygame.Rect(Config.SCREEN_WIDTH // 2 - 100, Config.SCREEN_HEIGHT // 2 - 25, 200, 50)
        color_inactive = pygame.Color("lightskyblue3")
        color_active = pygame.Color("dodgerblue2")
        color = color_inactive
        active = False
        text = ""
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
                            game_manager.state_valid_for_save = True
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

        draw_bar(screen, game_manager.pet.health, 10, current_state)

        screen.blit(feed_button.image, feed_button.rect)
        screen.blit(happy_button.image, happy_button.rect)
        screen.blit(play_button.image, play_button.rect)
        screen.blit(sleep_button.image, sleep_button.rect)

    elif current_state == "feed":
        screen.fill(Config.GREEN)
        screen.blit(pet_sprite, sprite_position)

        draw_bar(screen, game_manager.pet.food, 5, current_state)

        screen.blit(back_button.image, back_button)

        screen.blit(food_grid, (10, 450))
        draw_inventory(screen, food_items, 20, 460, 5, 50, 10)  # Draw food inventory
        screen.blit(eat_button.image, eat_button.rect)

    elif current_state == "happy":
        screen.fill(Config.YELLOW)
        screen.blit(pet_sprite, sprite_position)

        draw_bar(screen, game_manager.pet.happiness, 5, current_state)

        screen.blit(back_button.image, back_button)

        screen.blit(toy_grid, (10, 450))
        draw_inventory(screen, toy_items, 20, 460, 5, 50, 10)  # Draw toy inventory
        screen.blit(toy_button.image, toy_button.rect)
    elif current_state == "play":
        screen.fill(Config.PURPLE)
        screen.blit(game1_button.image, game1_button)
        screen.blit(game2_button.image, game2_button)
        screen.blit(back_button.image, back_button)

    elif current_state == "sleep":
        screen.fill(Config.GREY)
        screen.blit(pet_sprite, sprite_position)
        screen.blit(back_button.image, back_button)
        screen.blit(asleep_button.image, asleep_button.rect)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Save the game and exit
            game_manager.save_game()
            running = False

        if current_state == "main menu":
            new_game_button.handle_event(event)
            if continue_button:
                continue_button.handle_event(event)
        elif current_state == "game":
            feed_button.handle_event(event)
            happy_button.handle_event(event)
            play_button.handle_event(event)
            sleep_button.handle_event(event)
            back_button.handle_event(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if back_button.rect.collidepoint(pygame.mouse.get_pos()):
                change_state("game")
            if current_state == "feed":
                back_button.handle_event(event)
                eat_button.handle_event(event)

                handle_selection((mouse_x, mouse_y), food_items, current_state)
                # Check if the feed button is clicked to feed the pet
                if eat_button.rect.collidepoint((mouse_x, mouse_y)):
                    give_item()
            elif current_state == "happy":
                back_button.handle_event(event)
                toy_button.handle_event(event)

                handle_selection((mouse_x, mouse_y), toy_items, current_state)
                # Check if the play button is clicked to give toy to the pet
                if eat_button.rect.collidepoint((mouse_x, mouse_y)):
                    give_item()
            elif current_state == "play":
                back_button.handle_event(event)
                game1_button.action()

            elif current_state == "sleep":
                back_button.handle_event(event)
                asleep_button.handle_event(event)
                if asleep_button.rect.collidepoint((mouse_x, mouse_y)):
                    put_pet_to_sleep()

    pygame.display.flip()

pygame.quit()
