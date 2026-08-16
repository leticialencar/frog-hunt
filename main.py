import pygame
import random

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
    Frog(150, 180),
    Frog(350, 250),
    Frog(550, 180),
    Frog(250, 450),
    Frog(650, 450)
]

min_frogs = 3
max_frogs = 8

spawn_timer = 0
spawn_interval = 3000


def create_frog():

    for _ in range(100):

        x = random.randint(50, WIDTH - 100)
        y = random.randint(50, HEIGHT - 120)

        distance_x = abs(player.x - x)
        distance_y = abs(player.y - y)

        if distance_x < 150 and distance_y < 150:
            continue

        valid_position = True

        for frog in frogs:

            distance_x = abs(frog.x - x)
            distance_y = abs(frog.y - y)

            if distance_x < 100 and distance_y < 100:
                valid_position = False
                break

        if valid_position:
            return Frog(x, y)

    return None


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

    spawn_timer += clock.get_time()

    if (
        len(frogs) <= min_frogs
        and spawn_timer >= spawn_interval
        and len(frogs) < max_frogs
    ):

        spawn_timer = 0

        amount = random.randint(1, 2)

        for _ in range(amount):

            if len(frogs) >= max_frogs:
                break

            new_frog = create_frog()

            if new_frog:
                frogs.append(new_frog)

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