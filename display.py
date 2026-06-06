import pygame
from pygame._sdl2 import Window
import os


class Display:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_size = pygame.display.get_window_size()
        self.start_button = pygame.image.load(os.path.join("images", "start_text.png"))
        self.start_size = (self.screen_size[0] / 2, self.screen_size[1] / 8)
        self.start_button = pygame.transform.scale(self.start_button, self.start_size)
        self.start_pos = (self.screen_size[0] / 2 - self.start_size[0] / 2, self.screen_size[1] / 1.1 - self.start_size[1])


    def start(self) -> None:
        pygame.display.set_caption("Pong")

        pygame.init()
        clock = pygame.time.Clock()

        running = True
        show_start = True
        start_count = 0
        in_menu = True
        players_size = (self.screen_size[0] / 80, self.screen_size[1] / 10)
        player1_pos = [0 + 3 * players_size[0], self.screen_size[1] / 2 - players_size[1] / 2]
        
        while running:
            # Events management (alt+f4, button pressed, etc...)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if in_menu:
                        in_menu = False

            self.screen.fill("gray30")
            if in_menu:
                if show_start:
                    self.screen.blit(self.start_button, self.start_pos)
                if 0 < start_count < 30:
                    start_count += 1
                elif start_count == 0:
                    start_count += 1
                    show_start = True
                elif -30 <= start_count < 0:
                    start_count += 1
                    show_start = False
                else:
                    start_count = -30
            else:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    if player1_pos[1] < 10:
                        player1_pos[1] = 0
                    else:
                        player1_pos[1] -= 10
                if keys[pygame.K_DOWN]:
                    if player1_pos[1] > self.screen_size[1] - players_size[1] - 10:
                        player1_pos[1] = self.screen_size[1] - players_size[1]
                    else:
                        player1_pos[1] += 10
                pygame.draw.rect(self.screen, "black", (player1_pos[0], player1_pos[1], players_size[0], players_size[1]))

            # flip() the display to put in on screen
            pygame.display.flip()

            # Limit the display to 60 FPS
            clock.tick(60)
        
        pygame.quit()


if __name__ == '__main__':
    Display().start()
