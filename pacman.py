import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group

from image_rect import ImageRect


class Pacman(Sprite):

    def __init__(self, screen):
        super(Pacman, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.pacimg = ImageRect(screen, 'pacman', 32, 32)
        self.rect = self.pacimg.rect

        #  Movement flag
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        self.pacimg.rect.centerx = self.screen_rect.centerx - 4
        self.pacimg.rect.bottom = self.screen_rect.bottom - 124



    def blitme(self):
        self.screen.blit(self.pacimg.image, self.pacimg.rect)

    def update(self, maze):
        self.check_collision(maze)
        if self.moving_up and self.pacimg.rect.top > self.screen_rect.top:
            self.pacimg.rect.centery -= 1
        if self.moving_down and self.pacimg.rect.bottom < self.screen_rect.bottom:
            self.pacimg.rect.centery += 1
        if self.moving_left and self.pacimg.rect.left > self.screen_rect.left:
            self.pacimg.rect.centerx -= 1
        if self.moving_right and self.pacimg.rect.right < self.screen_rect.right:
            self.pacimg.rect.centerx += 1

    def check_collision(self, maze):
        for nrow in range(len(maze.bricks)):
            if self.rect.colliderect(maze.bricks[nrow]):
                if self.moving_up:
                    self.rect.top = maze.bricks[nrow].bottom + 1
                elif self.moving_down:
                    self.rect.bottom = maze.bricks[nrow].top - 1
                elif self.moving_left:
                    self.rect.left = maze.bricks[nrow].right + 1
                elif self.moving_right:
                    self.rect.left = maze.bricks[nrow].right - 1


