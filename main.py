import pygame

from player import Player
from frog import Frog


pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Frog Hunt!")

clock = pygame.time.Clock()

background = pygame.image.load(
    "assets/background/background.png"
).convert()

background = pygame.transform.scale(
    background,
    (WIDTH, HEIGHT)
)

font = pygame.font.Font(
    "assets/fonts/Minecraftia-Regular.ttf",
    12
)

player = Player(100, 100, WIDTH, HEIGHT)

frogs = [
    Frog(200, 200),
    Frog(400, 300),
    Frog(600, 450),
    Frog(300, 500)
]

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_e:

                for frog in frogs:

                    distance_x = abs(player.x - frog.x)
                    distance_y = abs(player.y - frog.y)

                    if distance_x < 80 and distance_y < 80:

                        frogs.remove(frog)
                        break

    player.update(clock)

    for frog in frogs:
        frog.update(clock)

    screen.blit(background, (0, 0))

    for frog in frogs:

        frog.draw(screen)

        distance_x = abs(player.x - frog.x)
        distance_y = abs(player.y - frog.y)

        if distance_x < 80 and distance_y < 80:

            text = font.render(
                "Pressione E",
                True,
                (255, 255, 255)
            )

            text_rect = text.get_rect(
                center=(
                    frog.x + frog.idle[0].get_width() // 2,
                    frog.y - 15
                )
            )

            screen.blit(
                text,
                text_rect
            )

    player.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()