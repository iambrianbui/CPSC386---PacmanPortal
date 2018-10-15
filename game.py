import pygame

from event_loop import EventLoop
from maze import Maze
from pacman import Pacman


class Game:
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pacman Portal")

        self.maze = Maze(self.screen, 'mazefile.txt', 'brick')

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


game = Game()
game.play()
