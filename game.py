import pygame
from pygame.sprite import Group

from event_loop import EventLoop
from maze import Maze
from pacman import Pacman
from expandfile import ExpandFile


class Game:
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((900, 1000))
        pygame.display.set_caption("Pacman Portal")

        self.clock = pygame.time.Clock()

        self.expandfile = ExpandFile('mazefile.txt', expandBy=6)

        self.maze = Maze(self.screen, 'mazefile_expanded.txt', 'brick', 'orangeportal', 'blueportal', 'shield', 'point')

        self.pacman = Pacman(self.screen)


    def play(self):
        pacman = self.pacman
        maze = self.maze

        eloop = EventLoop(status=False)

        while not eloop.finished:
            eloop.check_events(pacman)
            eloop.update_screen(pacman)
            pacman.update(maze)
            self.update_screen()

    def update_screen(self):
        self.screen.fill(Game.BLACK)
        self.maze.blitme()
        self.pacman.blitme()

        pygame.display.flip()
        self.clock.tick(120)


game = Game()
game.play()
