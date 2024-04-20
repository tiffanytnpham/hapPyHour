# Import the pygame module
import pygame
import os
from pet import Pet
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    K_RETURN,
    K_BACKSPACE,
    QUIT,
    MOUSEBUTTONDOWN,
)

# Initialize pygame
pygame.init()

# Screen width and height
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512

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
game_background_path = "back.jpg"
game_background = None
if os.path.exists(game_background_path):
  game_background = pygame.image.load(game_background_path).convert()
else:
  print("Game background image not found:", game_background_path)

# Load the logo
logo_path = "logo.png"
logo = pygame.image.load(logo_path).convert_alpha() if os.path.exists(
    logo_path) else None
logo_position = (10, 10)

# Start button properties
start_button_color = PINK
start_button_position = (SCREEN_WIDTH / 2 - 70, 350, 140, 50)
start_button_text = "Start!"

# Initialize Pet
pet = Pet()

# Game state
current_state = "main menu"


# Function to draw buttons
def draw_button(text, position, start_button_color):
  pygame.draw.rect(screen, start_button_color, position)  # Draw the button
  text_render = small_font.render(text, True, WHITE)
  text_rect = text_render.get_rect(center=(position[0] + position[2] / 2,
                                           position[1] + position[3] / 2))
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

    # Use logo for main menu
    if logo:
      screen.blit(logo, logo_position)

  #Initializing State
  elif current_state == "init":
    global pet_name
    init_running = True
    input_box = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 25,
                            200, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()

    while init_running:
      screen.fill(PINK)
      prompt_text = small_font.render("Name your pet!", True, (0, 0, 0))
      screen.blit(prompt_text,
                  (SCREEN_WIDTH // 2 - prompt_text.get_width() // 2,
                   SCREEN_HEIGHT // 2 - 100))
      #Event Handling inside init
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()
        if event.type == MOUSEBUTTONDOWN:
          if input_box.collidepoint(event.pos):
            active = not active
          else:
            active = False
          color = color_active if active else color_inactive
        if event.type == KEYDOWN:
          if active:
            if event.key == K_RETURN:
              print("Return key pressed. Name: ", text)
              pet.set_name(text)
              current_state = "game"
              print("current_state", current_state)
              init_running = False
            elif event.key == K_ESCAPE:
              pygame.quit()
              quit()
            elif event.key == K_BACKSPACE:
              text = text[:-1]
            else:
              text += event.unicode
        pygame.draw.rect(screen, color, input_box, 2)
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface,
                    (input_box.x + input_box.width // 2 -
                     txt_surface.get_width() // 2, input_box.y +
                     input_box.height // 2 - txt_surface.get_height() // 2))
        pygame.display.flip()
        clock.tick(30)
  #Game State
  elif current_state == "game":
    # Use game_background for the game screen
    if game_background:
      screen.blit(game_background, (0, 0))
    else:
      game_screen_text = small_font.render('Game Screen - Press ESC to quit',
                                           True, PINK)
      screen.blit(game_screen_text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 30))

    # Display pet information
    pet_info_text = f"Name: {pet.name}, Food: {pet.food}, Happiness: {pet.happiness}, Health: {pet.health}"
    pet_info_render = small_font.render(pet_info_text, True, WHITE)
    screen.blit(pet_info_render, (10, 10))
  # Event handling
  for event in pygame.event.get():
    if event.type == QUIT:
      running = False
    elif event.type == KEYDOWN:
      if event.key == K_ESCAPE:  # Check if the Escape key was pressed
        running = False
    elif event.type == MOUSEBUTTONDOWN:
      mouse_pos = event.pos  # Gets the mouse position
      if (start_button_position[0] <= mouse_pos[0] <=
          start_button_position[0] + start_button_position[2]
          and start_button_position[1] <= mouse_pos[1] <=
          start_button_position[1] + start_button_position[3]):
        if current_state == "main menu":  # Change to the game screen if start button pressed
          current_state = "init"

  pygame.display.flip()

pygame.quit()
