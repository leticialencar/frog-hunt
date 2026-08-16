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

        self.small_font = pygame.font.Font(
            "assets/fonts/Minecraftia-Regular.ttf",
            12
        )

        self.title_font = pygame.font.Font(
            "assets/fonts/Minecraftia-Regular.ttf",
            24
        )

        if self.frogs_caught == 0:
            self.animation_sheet = pygame.image.load(
                "assets/player/bea_sad.png"
            ).convert_alpha()
        else:
            self.animation_sheet = pygame.image.load(
                "assets/player/bea_celebrate.png"
            ).convert_alpha()

        self.frame_width = (
            self.animation_sheet.get_width() // 4
        )

        self.frame_height = (
            self.animation_sheet.get_height()
        )

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

        self.animation_sequence = [
            0,
            1,
            2,
            1,
            0
        ]

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
                    self.selected_option = (
                        len(self.options) - 1
                    )

            elif event.key == pygame.K_DOWN:

                self.selected_option += 1

                if self.selected_option >= len(
                    self.options
                ):
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

            if self.sequence_index >= len(
                self.animation_sequence
            ):
                self.sequence_index = 0

            self.current_frame = (
                self.animation_sequence[
                    self.sequence_index
                ]
            )

    def draw_text_with_outline(
        self,
        screen,
        text,
        font,
        center,
        text_color=(255, 255, 255),
        outline_color=(60, 45, 30)
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

    def draw_panel(self, screen):

        panel_width = 440
        panel_height = 520

        panel = pygame.Surface(
            (
                panel_width,
                panel_height
            ),
            pygame.SRCALPHA
        )

        panel.fill(
            (35, 25, 18, 180)
        )

        panel_rect = panel.get_rect(
            center=(
                self.width // 2,
                self.height // 2
            )
        )

        screen.blit(
            panel,
            panel_rect
        )

        return panel_rect

    def draw_option(
        self,
        screen,
        text,
        center,
        selected
    ):

        if selected:

            text_color = (255, 230, 150)

            arrow = self.font.render(
                ">",
                True,
                (255, 230, 150)
            )

            arrow_rect = arrow.get_rect(
                midright=(
                    center[0] - 125,
                    center[1]
                )
            )

            screen.blit(
                arrow,
                arrow_rect
            )

        else:

            text_color = (255, 255, 255)

        self.draw_text_with_outline(
            screen,
            text,
            self.font,
            center,
            text_color
        )

    def draw(self, screen):

        screen.blit(
            self.background,
            (0, 0)
        )

        panel_rect = self.draw_panel(
            screen
        )

        if self.frogs_caught == 0:
            title = "Fim de jogo..."
        else:
            title = "Fim de jogo!"

        self.draw_text_with_outline(
            screen,
            title,
            self.title_font,
            (
                self.width // 2,
                panel_rect.top + 45
            ),
            (255, 255, 255)
        )

        frame = self.frames[
            self.current_frame
        ]

        frame_rect = frame.get_rect(
            center=(
                self.width // 2,
                panel_rect.top + 160
            )
        )

        screen.blit(
            frame,
            frame_rect
        )

        stats_y = panel_rect.top + 275

        self.draw_text_with_outline(
            screen,
            f"Sapinhos: {self.frogs_caught}",
            self.font,
            (
                self.width // 2,
                stats_y
            ),
            (255, 255, 255)
        )

        seconds = int(
            self.game_time / 1000
        )

        minutes = seconds // 60
        seconds = seconds % 60

        time_text = (
            f"Tempo: {minutes:02d}:{seconds:02d}"
        )

        self.draw_text_with_outline(
            screen,
            time_text,
            self.font,
            (
                self.width // 2,
                stats_y + 35
            ),
            (255, 255, 255)
        )

        if self.frogs_caught == 0:
            message = "Nenhum sapinho dessa vez."
        else:
            message = "Obrigado por jogar!"

        self.draw_text_with_outline(
            screen,
            message,
            self.small_font,
            (
                self.width // 2,
                stats_y + 75
            ),
            (255, 255, 255)
        )

        separator_y = panel_rect.top + 385

        pygame.draw.line(
            screen,
            (180, 160, 120),
            (
                panel_rect.left + 70,
                separator_y
            ),
            (
                panel_rect.right - 70,
                separator_y
            ),
            1
        )

        self.draw_option(
            screen,
            "Jogar Novamente",
            (
                self.width // 2,
                panel_rect.top + 430
            ),
            self.selected_option == 0
        )

        self.draw_option(
            screen,
            "Sair",
            (
                self.width // 2,
                panel_rect.top + 480
            ),
            self.selected_option == 1
        )