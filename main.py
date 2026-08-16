import pygame

from game import Game


pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Frog Hunt!")

clock = pygame.time.Clock()

game = Game(WIDTH, HEIGHT)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        game.handle_event(event)

    game.update(clock)

    game.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()