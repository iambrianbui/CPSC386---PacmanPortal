import pygame

from image_rect import ImageRect

class Maze:

    def __init__(self, screen, mazefile, brickfile):
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()


        self.bricks = []
        sz = 4
        self.brick = ImageRect(screen, brickfile, sz, sz)

