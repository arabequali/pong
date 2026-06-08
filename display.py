from paddle import Paddle
from ball import Ball
import pygame, os, random
from pygame._sdl2 import Window


class Display:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_size = pygame.display.get_window_size()
        self.start_text = pygame.image.load(os.path.join("images", "start_text.png"))
        self.start_size = (self.screen_size[0] / 2, self.screen_size[1] / 8)
        self.start_text = pygame.transform.scale(self.start_text, self.start_size)
        self.start_pos = (self.screen_size[0] / 2 - self.start_size[0] / 2, self.screen_size[1] / 1.1 - self.start_size[1])


    def start(self) -> None:
        pygame.display.set_caption("Pong")

        pygame.init()
        clock = pygame.time.Clock()

        running = True
        show_start = True
        start_count = 0
        in_menu = True

        player1 = Paddle(1, self.screen)
        player2 = Paddle(2, self.screen)
        ball = Ball(self.screen, player1, player2)

        while running:
            # Events management (alt+f4, key pressed, etc...)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if in_menu:
                        in_menu = False

            self.screen.fill("gray30")
            if in_menu:
                if show_start:
                    self.screen.blit(self.start_text, self.start_pos)
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
                ball.movement_x()
                ball.movement_y()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    player1.go_up()
                if keys[pygame.K_DOWN]:
                    player1.go_down()
                player1.draw()
                ball.draw()

            # flip() the display to put in on screen
            pygame.display.flip()

            # Limit the display to 30 FPS
            clock.tick(30)
        
        pygame.quit()


if __name__ == '__main__':
    Display().start()
