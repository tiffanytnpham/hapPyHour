import pygame
import random
import time
from config import Config

pygame.init()

WIDTH = 800
HEIGHT = 800
FPS = 60
ROWS = 4
COLUMNS = 4
matched_pairs = 0
new_board = True
spaces = []
first_guess = None
second_guess = None
score = 0
delay = 1 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Find the matching pairs!")

#Loading all the sprites for the cards
sprite1 = pygame.image.load('Sprites/Food/cherry.png').convert_alpha()
sprite2 = pygame.image.load('Sprites/Food/fish.png').convert_alpha()
sprite3 = pygame.image.load('Sprites/Toy/ball.png').convert_alpha()
sprite4 = pygame.image.load('Sprites/Toy/feather.png').convert_alpha()
sprite5 = pygame.image.load('Sprites/Toy/yarn.png').convert_alpha()
sprite6 = pygame.image.load('Sprites/Toy/box.png').convert_alpha()
sprite7 = pygame.image.load('Sprites/Food/peach.png').convert_alpha()
sprite8 = pygame.image.load('Sprites/Bars/full_paw.png').convert_alpha()

sprites = [sprite1, sprite2, sprite3, sprite4, sprite5, sprite6, sprite7, sprite8] * 2
random.shuffle(sprites)

#Define card attributes
CARD_WIDTH = WIDTH // COLUMNS
CARD_HEIGHT = HEIGHT // ROWS
CARD_PADDING = 15
card_rects = [[pygame.Rect(x * CARD_WIDTH + CARD_PADDING, y * CARD_HEIGHT + CARD_PADDING,
                            CARD_WIDTH - 2 * CARD_PADDING, CARD_HEIGHT - 2 * CARD_PADDING)
               for y in range(ROWS)] for x in range(COLUMNS)]

#Create a dictionary of the matched cards
matched = {(x, y): False for x in range(COLUMNS) for y in range(ROWS)}

font = pygame.font.SysFont(None, 36)

#game loop
running = True
while running:
    screen.fill(Config.GREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            column = x // CARD_WIDTH
            row = y // CARD_HEIGHT
            if not (0 <= column < COLUMNS and 0 <= row < ROWS):
                continue
            if not matched[(column, row)]:
                if first_guess is None:
                    first_guess = (column, row) #first guess
                elif second_guess is None and (column, row) != first_guess: #second guess
                    second_guess = (column, row)
                    score += 1
    #Draw the cards in a grid (4x4)
    for x in range(COLUMNS):
        for y in range(ROWS):
            rect = card_rects[x][y]
            pygame.draw.rect(screen, (0, 0, 0), rect, 2, 40)
            if (x, y) in matched and matched[(x, y)]:
                sprite = pygame.transform.scale(sprites[y * COLUMNS + x], (rect.width // 2, rect.height // 2))
                sprite_rect = sprite.get_rect(center=rect.center)
                screen.blit(sprite, sprite_rect)
            elif (x, y) == first_guess or (x, y) == second_guess:
                sprite = pygame.transform.scale(sprites[y * COLUMNS + x], (rect.width // 2, rect.height // 2))
                sprite_rect = sprite.get_rect(center=rect.center)
                screen.blit(sprite, sprite_rect)

    pygame.display.flip()

    #Check if the player successfully matched cards
    if first_guess is not None and second_guess is not None:
        sprite1_index = first_guess[1] * COLUMNS + first_guess[0]
        sprite2_index = second_guess[1] * COLUMNS + second_guess[0]
        if sprites[sprite1_index] == sprites[sprite2_index]:
            matched[first_guess] = True
            matched[second_guess] = True
            matched_pairs += 1

        time.sleep(delay)   #Add a delay before the cards close
        first_guess = None
        second_guess = None

    #If all the pairs were matched, the game is over
    if matched_pairs == (ROWS * COLUMNS) // 2:
        running = False

#Score
score_text = font.render(f"Well Done! Attempts: {score}", True, (0, 0, 0))
score_text_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(score_text, score_text_rect)

#Write score to file
with open("matching_game_score.txt", "w") as f:
    f.write(str(score))

pygame.display.flip()

pygame.time.wait(3000)

pygame.quit()
