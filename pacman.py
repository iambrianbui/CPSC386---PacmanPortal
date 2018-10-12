import pygame

from image_rect import ImageRect


class Pacman:

    def __init__(self, screen):
        super(Pacman, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.pacimg = ImageRect(screen, 'pacman', 32, 32)

        #  Movement flag
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        self.pacimg.rect.centerx = self.screen_rect.centerx - 4
        self.pacimg.rect.bottom = self.screen_rect.bottom - 124

    def blitme(self):
        self.screen.blit(self.pacimg.image, self.pacimg.rect)

    def update(self):
        if self.moving_up and self.pacimg.rect.top > self.screen_rect.top:
            self.pacimg.center -= 1
        if self.moving_down and self.pacimg.rect.bottom > self.screen_rect.bottom:
            self.pacimg.center += 1
