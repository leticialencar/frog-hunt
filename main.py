import pygame

from player import Player


pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Frog Hunt!")

clock = pygame.time.Clock()

player = Player(100, 100, WIDTH, HEIGHT)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    player.update(clock)

    screen.fill((30, 30, 30))

    player.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()