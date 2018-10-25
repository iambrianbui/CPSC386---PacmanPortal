import pygame
from pygame.sprite import Sprite
from image_rect import ImageRect

class Ghost():
    def __init__(self, screen):
        super(Ghost, self).__init__()
        self.screen = screen

        self.image = ImageRect(screen, 'clearGhost', 128, 128)
        self.rect = self.image.rect
        self.x, self.y = 300, 360
        #  Type of ghost this is
        self.type = 0

    def prep_ghost(self):
        if self.type == 0:
            self.image = pygame.image.load("images/redGhost.png")

    def blit(self):
        self.screen.blit(self.image, self.rect)