import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(f"Feed your pet as much as you can before the clock runs out!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (205, 133, 63)

font = pygame.font.SysFont(None, 40)

pet_image = pygame.image.load("Sprites/Level2/pet.png")
pet_image = pygame.transform.scale(pet_image, (100, 100))
pet_rect = pet_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
PET_SPEED = 5

food_images = [pygame.image.load("Sprites/Food/peach.png"),
               pygame.image.load("Sprites/Food/fish.png"),
               pygame.image.load("Sprites/Food/cherry.png")]

FOOD_SIZE = 40  
foods = []

for _ in range(30):
    food_image = random.choice(food_images)
    food_rect = food_image.get_rect(center=(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)))
    foods.append((food_image, food_rect))

score = 0

clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
time_limit = 10

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pet_rect.move_ip(-PET_SPEED, 0)
    if keys[pygame.K_RIGHT]:
        pet_rect.move_ip(PET_SPEED, 0)
    if keys[pygame.K_UP]:
        pet_rect.move_ip(0, -PET_SPEED)
    if keys[pygame.K_DOWN]:
        pet_rect.move_ip(0, PET_SPEED)

    pet_rect.clamp_ip(screen.get_rect())

    screen.blit(pet_image, pet_rect)

    for food_image, food_rect in foods:
        screen.blit(food_image, food_rect)

    food_to_remove = []
    for food_image, food_rect in foods:
        if pet_rect.colliderect(food_rect):
            food_to_remove.append((food_image, food_rect))
            score += 1

    for food_item in food_to_remove:
        foods.remove(food_item)

    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    current_time = pygame.time.get_ticks()
    time_elapsed = (current_time - start_time) // 1000

    timer_text = font.render("Time: " + str(max(time_limit - time_elapsed, 0)), True, BLACK)
    screen.blit(timer_text, (WIDTH - 120, 10))

    if time_elapsed >= time_limit:
        running = False

    pygame.display.flip()
    clock.tick(60)

game_over_text = font.render("Well done!", True, RED)
screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 20))
final_score_text = font.render("Final Score: " + str(score), True, BLACK)
screen.blit(final_score_text, (WIDTH // 2 - 120, HEIGHT // 2 + 20))
pygame.display.flip()

pygame.time.wait(2000)

pygame.quit()