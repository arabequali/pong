import pygame
from random import randint, choice
from paddle import Paddle


class Ball:
    def __init__(self, screen: Surface, player1: Paddle, player2: Paddle) -> None:
        self.screen = screen
        self.screen_size = pygame.display.get_window_size()
        self.size = self.screen_size[0] / 100
        self.x = self.screen_size[0] / 2 - self.size / 2
        self.y = self.screen_size[1] / 2 - self.size / 2
        self.dx = randint(-10, -5)
        self.dy = choice([i for i in range(-10, 10) if i])
        self.player1 = player1
        self.player2 = player2


    def movement_x(self) -> None:
        if not collide_paddle():
            if not (self.screen_size[0] - self.size - self.dx > self.x > self.size):
                if self.dx > 0:
                    self.dx = randint(-10, -5)
                elif self.dx < 0:
                    self.dx = randint(5, 10)
        self.x += self.dx


    def movement_y(self) -> None:
        if not (self.screen_size[1] - self.size - self.dy > self.y > self.size):
            if self.dy > 0:
                self.dy = randint(-10, -1)
            elif self.dy < 0:
                self.dy = randint(1, 10)
        self.y += self.dy


    def collide_paddle(self) -> bool:
        ball_vector_center = pygame.math.Vector2(self.x, self.y)
        if self.dx < 0:
            corner_player = [self.player1.bottomleft, self.player1.bottomright, self.player1.topleft, self.player1.topright]
            if [p for p in corner_player if pygame.math.Vector2(*p).distance_to(ball_vector_center) <= self.size]:
                self.dx = randint(5, 10)
                return True
        elif self.dx > 0:
            pass
        else:
            return False


    def draw(self) -> None:
        pygame.draw.circle(self.screen, "black", (self.x, self.y), self.size)
