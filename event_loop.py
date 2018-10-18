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

    def update_screen(self, pacman):
        pacman.blitme()

def check_keydown_events(event, pacman):
    if event.key == pygame.K_w or event.key == pygame.K_UP:
        pacman.movement_switches += 1
        if pacman.movement_switches == 1:
            pacman.moving_up = True
            pacman.moving_left = False
            pacman.moving_right = False
            pacman.moving_down = False
    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
        pacman.movement_switches += 1
        if pacman.movement_switches == 1:
            pacman.moving_up = False
            pacman.moving_left = False
            pacman.moving_right = False
            pacman.moving_down = True
    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
        pacman.movement_switches += 1
        if pacman.movement_switches == 1:
            pacman.moving_up = False
            pacman.moving_left = True
            pacman.moving_right = False
            pacman.moving_down = False
    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        pacman.movement_switches += 1
        if pacman.movement_switches == 1:
            pacman.moving_up = False
            pacman.moving_left = False
            pacman.moving_right = True
            pacman.moving_down = False

def check_keyup_events(event, pacman):
    if event.key == pygame.K_w or event.key == pygame.K_UP:
        pacman.movement_switches -= 1
    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
        pacman.movement_switches -= 1
    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
        pacman.movement_switches -= 1
    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        pacman.movement_switches -= 1

