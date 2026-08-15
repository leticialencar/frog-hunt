import pygame


class Player:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.speed = 4

        self.current_frame = 0
        self.animation_timer = 0

        self.frame_durations = [
            2000,
            700
        ]

        sprite_sheet = pygame.image.load(
            "assets/player/bea_spritesheet.png"
        ).convert_alpha()

        frame_width = 200
        frame_height = 218

        self.idle_front = []

        for i in range(2):

            frame = sprite_sheet.subsurface(
                pygame.Rect(
                    i * frame_width,
                    0,
                    frame_width,
                    frame_height
                )
            )

            frame = pygame.transform.scale(
                frame,
                (100, 109)
            )

            self.idle_front.append(frame)

    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed

        self.x = max(0, min(self.x, 800 - 100))
        self.y = max(0, min(self.y, 600 - 109))

    def update(self, clock):

        self.move()

        self.animation_timer += clock.get_time()

        if self.animation_timer >= self.frame_durations[self.current_frame]:

            self.animation_timer = 0

            self.current_frame += 1

            if self.current_frame >= len(self.idle_front):
                self.current_frame = 0

    def draw(self, screen):

        screen.blit(
            self.idle_front[self.current_frame],
            (self.x, self.y)
        )