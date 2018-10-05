import pygame

from image_rect import ImageRect

class Pacman:


    def __init__(self, screen):
        super(Pacman, self).__init__()
        self.screen = screen

        self.pacimg = ImageRect(screen, 'pacman', 16, 16)

        #  Movement flag
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False


    def blitme(self):
        self.screen.blit(self.pacimg.image, self.pacimg.rect)