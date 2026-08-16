import pygame

from game import Game
from end_game import EndGame


pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Frog Hunt!"
)

clock = pygame.time.Clock()

game = Game(
    WIDTH,
    HEIGHT
)

end_game = None

current_screen = "game"

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        elif current_screen == "game":

            game.handle_event(event)

        elif current_screen == "end_game":

            result = end_game.handle_event(event)

            if result == "game":

                game = Game(
                    WIDTH,
                    HEIGHT
                )

                end_game = None
                current_screen = "game"

            elif result == "quit":

                running = False

    if current_screen == "game":

        game.update(clock)

        if game.is_finished():

            end_game = EndGame(
                WIDTH,
                HEIGHT,
                game.frogs_caught,
                game.game_time
            )

            current_screen = "end_game"

        else:

            game.draw(screen)

    elif current_screen == "end_game":

        end_game.update(clock)
        end_game.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()