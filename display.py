from paddle import Paddle
import pygame, os, random
from pygame._sdl2 import Window


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

        player1 = Paddle(1, self.screen)

        ball_size = (self.screen_size[0] / 100)
        ball_pos = [self.screen_size[0] / 2 - ball_size / 2, self.screen_size[1] / 2 - ball_size / 2]
        dx, dy = random.randint(-10, -5), random.choice([i for i in range(-10, 10) if i])
        
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
                if self.screen_size[0] - ball_size - dx > ball_pos[0] > ball_size:
                    pass
                elif dx > 0:
                    dx = random.randint(-10, -5)
                else:
                    dx = random.randint(5, 10)
                if self.screen_size[1] - ball_size > ball_pos[1] > ball_size:
                    pass
                elif dy > 0:
                    dy = random.randint(-10, -5)
                else:
                    dy = random.randint(5, 10)
                ball_pos[0] += dx
                ball_pos[1] += dy
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    player1.go_up()
                if keys[pygame.K_DOWN]:
                    player1.go_down()
                player1.draw()
                pygame.draw.circle(self.screen, "black", (ball_pos[0], ball_pos[1]), ball_size)

            # flip() the display to put in on screen
            pygame.display.flip()

            # Limit the display to 30 FPS
            clock.tick(30)
        
        pygame.quit()


if __name__ == '__main__':
    Display().start()
