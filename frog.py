import pygame


class Frog:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.scale = 0.18

        self.current_frame = 0
        self.animation_timer = 0

        self.frame_durations = [
            2000,
            500,
            800,
            1200
        ]

        self.sprite_sheet = pygame.image.load(
            "assets/frog/frog_spritesheet.png"
        ).convert_alpha()

        self.idle = []
        self.walk = []
        self.action = []

        self.load_sprites()

    def load_sprites(self):

        idle_rects = [
            (174, 123, 201, 203),
            (500, 123, 202, 202),
            (824, 123, 200, 202),
            (1159, 121, 200, 208)
        ]

        walk_rects = [
            (65, 424, 198, 176),
            (308, 424, 204, 173),
            (547, 424, 204, 176),
            (802, 429, 196, 171),
            (1046, 428, 200, 173),
            (1281, 428, 206, 169)
        ]

        action_rects = [
            (174, 773, 207, 162),
            (494, 702, 239, 212),
            (802, 682, 214, 212),
            (1153, 781, 200, 159)
        ]

        for rect in idle_rects:

            frame = self.sprite_sheet.subsurface(rect).copy()

            width = int(frame.get_width() * self.scale)
            height = int(frame.get_height() * self.scale)

            frame = pygame.transform.scale(
                frame,
                (width, height)
            )

            self.idle.append(frame)

        for rect in walk_rects:

            frame = self.sprite_sheet.subsurface(rect).copy()

            width = int(frame.get_width() * self.scale)
            height = int(frame.get_height() * self.scale)

            frame = pygame.transform.scale(
                frame,
                (width, height)
            )

            self.walk.append(frame)

        for rect in action_rects:

            frame = self.sprite_sheet.subsurface(rect).copy()

            width = int(frame.get_width() * self.scale)
            height = int(frame.get_height() * self.scale)

            frame = pygame.transform.scale(
                frame,
                (width, height)
            )

            self.action.append(frame)

    def update(self, clock):

        self.animation_timer += clock.get_time()

        if self.animation_timer >= self.frame_durations[self.current_frame]:

            self.animation_timer = 0

            self.current_frame += 1

            if self.current_frame >= len(self.idle):

                self.current_frame = 0

    def draw(self, screen):

        screen.blit(
            self.idle[self.current_frame],
            (self.x, self.y)
        )