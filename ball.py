import pygame
import sys
from random import randint, choice
from paddle import Paddle


class Ball:
    def __init__(self, screen: Surface, player1: Paddle, player2: Paddle) -> None:
        self.screen = screen
        self.screen_size = pygame.display.get_window_size()
        self.size = self.screen_size[0] / 100
        self.x = self.screen_size[0] // 2 - self.size // 2
        self.y = self.screen_size[1] // 2 - self.size // 2
        self.dx = randint(-10, -5)
        self.dy = choice([i for i in range(-10, 10) if i])
        self.player1 = player1
        self.player2 = player2


    def movement_x(self) -> None:
        if not self.collide_paddle():
            if not (self.screen_size[0] - self.size - self.dx > self.x > self.size):
                if self.dx > 0:
                    self.dx = randint(-10, -5)
                elif self.dx < 0:
                    sys.exit()
        self.x += self.dx


    def movement_y(self) -> None:
        if not (self.screen_size[1] - self.size - self.dy > self.y > self.size):
            if self.dy > 0:
                self.dy = randint(-10, -1)
            elif self.dy < 0:
                self.dy = randint(1, 10)
        self.y += self.dy


    def collide_paddle(self) -> bool:
        if self.dx < 0:
            width_player = [x for x in range(self.player1.x - self.dx, self.player1.x + self.player1.size_x - self.dx)]
            height_player = [y for y in range(self.player1.y, self.player1.y + self.player1.size_y)]
            if self.x in width_player and self.y in height_player:
                self.dx = randint(5, 10)
                return True
        elif self.dx > 0:
            pass
        return False


    def draw(self) -> None:
        pygame.draw.circle(self.screen, "black", (self.x, self.y), self.size)
