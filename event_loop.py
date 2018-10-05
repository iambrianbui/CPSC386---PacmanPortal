import sys
import pygame


class EventLoop:

    def __init__(self, status):
        self.finished = status

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()