import pygame


class EndGame:

    def __init__(
        self,
        width,
        height,
        frogs_caught,
        game_time
    ):

        self.width = width
        self.height = height

        self.frogs_caught = frogs_caught
        self.game_time = game_time

        self.background = pygame.image.load(
            "assets/background/background.png"
        ).convert()

        self.background = pygame.transform.scale(
            self.background,
            (self.width, self.height)
        )

        self.font = pygame.font.Font(
            "assets/fonts/Minecraftia-Regular.ttf",
            16
        )

        self.title_font = pygame.font.Font(
            "assets/fonts/Minecraftia-Regular.ttf",
            28
        )

        if self.frogs_caught == 0:

            self.animation_sheet = pygame.image.load(
                "assets/player/bea_sad.png"
            ).convert_alpha()

        else:

            self.animation_sheet = pygame.image.load(
                "assets/player/bea_celebrate.png"
            ).convert_alpha()

        self.frame_width = self.animation_sheet.get_width() // 4
        self.frame_height = self.animation_sheet.get_height()

        self.frames = []

        for i in range(4):

            frame = self.animation_sheet.subsurface(
                (
                    i * self.frame_width,
                    0,
                    self.frame_width,
                    self.frame_height
                )
            )

            frame = pygame.transform.smoothscale(
                frame,
                (
                    int(self.frame_width * 0.25),
                    int(self.frame_height * 0.25)
                )
            )

            self.frames.append(frame)

        self.current_frame = 0

        self.animation_sequence = [0, 1, 2, 1, 0]
        self.sequence_index = 0

        self.animation_timer = 0
        
        if self.frogs_caught == 0:
            self.animation_speed = 250
        else:
            self.animation_speed = 180

        self.selected_option = 0

        self.options = [
            "Jogar Novamente",
            "Sair"
        ]

    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                self.selected_option -= 1

                if self.selected_option < 0:
                    self.selected_option = len(self.options) - 1

            elif event.key == pygame.K_DOWN:
                self.selected_option += 1

                if self.selected_option >= len(self.options):
                    self.selected_option = 0

            elif event.key == pygame.K_RETURN:

                if self.selected_option == 0:
                    return "game"

                if self.selected_option == 1:
                    return "quit"

        return None

    def update(self, clock):

        delta_time = clock.get_time()

        self.animation_timer += delta_time

        if self.sequence_index == 0:
            frame_duration = 500

        elif self.sequence_index == 2:
            frame_duration = 400

        elif self.sequence_index == 4:
            frame_duration = 500

        else:
            frame_duration = self.animation_speed

        if self.animation_timer >= frame_duration:

            self.animation_timer = 0

            self.sequence_index += 1

            if self.sequence_index >= len(self.animation_sequence):
                self.sequence_index = 0

            self.current_frame = self.animation_sequence[
                self.sequence_index
            ]

    def draw_text_with_outline(
        self,
        screen,
        text,
        font,
        center,
        text_color,
        outline_color=(80, 60, 40)
    ):

        outline = font.render(
            text,
            True,
            outline_color
        )

        text_surface = font.render(
            text,
            True,
            text_color
        )

        text_rect = text_surface.get_rect(
            center=center
        )

        outline_positions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for offset_x, offset_y in outline_positions:

            outline_rect = text_rect.move(
                offset_x,
                offset_y
            )

            screen.blit(
                outline,
                outline_rect
            )

        screen.blit(
            text_surface,
            text_rect
        )

    def draw_button(
        self,
        screen,
        text,
        center,
        selected
    ):

        button_width = 240
        button_height = 55

        button_rect = pygame.Rect(
            0,
            0,
            button_width,
            button_height
        )

        button_rect.center = center

        if selected:
            button_color = (170, 125, 70)
            border_color = (255, 220, 120)
        else:
            button_color = (120, 85, 50)
            border_color = (80, 55, 35)

        pygame.draw.rect(
            screen,
            border_color,
            button_rect
        )

        inner_rect = button_rect.inflate(
            -6,
            -6
        )

        pygame.draw.rect(
            screen,
            button_color,
            inner_rect
        )

        if selected:

            arrow = self.font.render(
                ">",
                True,
                (255, 235, 150)
            )

            arrow_rect = arrow.get_rect(
                center=(
                    button_rect.left + 25,
                    button_rect.centery
                )
            )

            screen.blit(
                arrow,
                arrow_rect
            )

        self.draw_text_with_outline(
            screen,
            text,
            self.font,
            (
                button_rect.centerx + 8
                if selected
                else button_rect.centerx,
                button_rect.centery
            ),
            (255, 245, 210)
        )

    def draw(self, screen):

        screen.blit(
            self.background,
            (0, 0)
        )

        self.draw_text_with_outline(
            screen,
            "Fim de jogo!",
            self.title_font,
            (
                self.width // 2,
                85
            ),
            (255, 235, 150)
        )

        frame = self.frames[self.current_frame]

        frame_rect = frame.get_rect(
            center=(
                self.width // 2,
                205
            )
        )

        screen.blit(
            frame,
            frame_rect
        )

        self.draw_text_with_outline(
            screen,
            f"Sapinhos: {self.frogs_caught}",
            self.font,
            (
                self.width // 2,
                335
            ),
            (255, 245, 210)
        )

        seconds = int(self.game_time / 1000)

        minutes = seconds // 60
        seconds = seconds % 60

        time_text = f"Tempo: {minutes:02d}:{seconds:02d}"

        self.draw_text_with_outline(
            screen,
            time_text,
            self.font,
            (
                self.width // 2,
                375
            ),
            (255, 245, 210)
        )

        self.draw_button(
            screen,
            "Jogar Novamente",
            (
                self.width // 2,
                465
            ),
            self.selected_option == 0
        )

        self.draw_button(
            screen,
            "Sair",
            (
                self.width // 2,
                535
            ),
            self.selected_option == 1
        )