import pygame
import random
# Initialize Pygame
pygame.init()

# Set up the display
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Basic Pygame Game")

# Define colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
font = pygame.font.Font(None, 36)

circle_x = SCREEN_WIDTH // 2
circle_y = 370
circle_radius = 30
circle_speed = 1

apple_x = random.randint(0, SCREEN_WIDTH)
apple_y = 0
apple_radius = 15
circle_speed = .5
round = 1
# Game loop control variable
running = True



def gameend():
    screen.fill(WHITE)
    scoretext = font.render(f"Round: {round}", True, BLACK)
# Main game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen (fill it with white)
    screen.fill(WHITE)
    for i in range(round):
        pygame.draw.circle(screen, RED, (apple_x, apple_y), apple_radius)

    scoretext = font.render(f"Round: {round}", True, BLACK)
    gameovertext = font.render(f"Game Over", True, RED)
    apple_y += circle_speed
    #check collisions of the circle and the apple
    if circle_x - circle_radius < apple_x < circle_x + circle_radius and circle_y - circle_radius < apple_y < circle_y + circle_radius:
        circle_speed += .01
        apple_x = random.randint(0, SCREEN_WIDTH)
        apple_y = 0
        round += 1


    if apple_y > SCREEN_HEIGHT:
        screen.fill(WHITE)
        screen.blit(gameovertext, (250, 150))
        screen.blit(scoretext, (250, 175))
    screen.blit(scoretext, (10, 10))
    pygame.draw.circle(screen, BLACK, (circle_x, circle_y), circle_radius)
    if pygame.key.get_pressed()[pygame.K_a]:
        if circle_x > circle_radius - 0:
            circle_x -= circle_speed
    if pygame.key.get_pressed()[pygame.K_d]:
        if circle_x + circle_radius > SCREEN_WIDTH:
            circle_x -= circle_speed
        circle_x += circle_speed
    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
