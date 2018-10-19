import pygame
from pygame.sprite import Sprite

from image_rect import ImageRect

class Point(Sprite):

    def __init__(self, screen):
        super(Point, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = ImageRect(screen, 'point', 4, 4)
        self.rect = self.image.rect

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blit(self):
        self.screen.blit(self.image.image, self.image.rect)
