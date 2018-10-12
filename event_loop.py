import sys
import pygame


class EventLoop:

    def __init__(self, status):
        self.finished = status

    @staticmethod
    def check_events(pacman):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, pacman)

            elif event.type == pygame.KEYUP:
                check_keyup_events(event, pacman)

    def check_keydown_events(event, pacman):
        if event.key == pygame.K_w:
            pacman.moving_up = True

    def check_keyup_events(event, pacman):
        if event.key == pygame.K_w:
            pacman.moving_down = False

    def update_screen(self, pacman):
        pacman.blitme()
