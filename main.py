import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Frog Hunt!")

clock = pygame.time.Clock()

player_x = 100
player_y = 100

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    pygame.draw.rect(screen, (100, 200, 100), (player_x, player_y, 50, 50))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()