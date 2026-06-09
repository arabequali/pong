import pygame
from random import randint, choice


class Paddle:
    def __init__(self, player: int, screen: Surface) -> None:
        self.screen = screen
        self.screen_size = pygame.display.get_window_size()
        self.size_x = self.screen_size[0] // 80
        self.size_y = self.screen_size[1] // 10
        if player == 1:
            self.x = 3 * self.size_x
            self.y = self.screen_size[1] // 2 - self.size_y // 2
        else:
            self.x = 0
            self.y = 0
        self.player_hitbox = pygame.Rect(self.x, self.y, self.size_x, self.size_y)


    def go_up(self) -> None:
        if self.y < 10:
            self.y = 0
        else:
            self.y -= 10


    def go_down(self) -> None:
        if self.y > self.screen_size[1] - self.size_y - 10:
            self.y = self.screen_size[1] - self.size_y
        else:
            self.y += 10


    def draw(self) -> None:
        pygame.draw.rect(self.screen, "black", (self.x, self.y, self.size_x, self.size_y))
