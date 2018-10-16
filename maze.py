import pygame
from pygame.sprite import Sprite

from image_rect import ImageRect

class Maze(Sprite):
    BRICK_SIZE = 16

    def __init__(self, screen, mazefile, brickfile):
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.bricks = []

        sz = Maze.BRICK_SIZE
        self.brick = ImageRect(screen, brickfile, sz, sz)

        self.deltax = self.deltay = Maze.BRICK_SIZE

        self.build()


    def build(self):
        r = self.brick.rect
        w = r.width
        h = r.height
        dx = self.deltax
        dy = self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'x':
                    self.bricks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))

    def blitme(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)





