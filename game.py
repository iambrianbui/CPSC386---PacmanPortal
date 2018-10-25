import pygame
from pygame.sprite import Group

from event_loop import EventLoop
from maze import Maze
from ghost import Ghost
from pacman import Pacman
from expandfile import ExpandFile
from game_stats import GameStats


class Game:
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((900, 1000))
        pygame.display.set_caption("Pacman Portal")

        self.clock = pygame.time.Clock()

        self.expandfile = ExpandFile('mazefile.txt', expandBy=6)

        self.maze = Maze(self.screen, 'mazefile_expanded.txt', 'brick', 'orangeportal', 'blueportal', 'shield', 'point')

        self.gamestats = GameStats()

        self.pacmanGroup = Group()
        self.pacman = Pacman(self.screen)
        self.pacmanGroup.add(self.pacman)

    def play(self):
        pacman = self.pacman
        maze = self.maze
        ghost = []
        for i in range(1):
            g = Ghost(self.screen)
            g.type = i
            g.x += 30 * i
            g.prep_ghost()
            ghost.append(g)

        eloop = EventLoop(status=False)

        while not eloop.finished:
            eloop.check_events(pacman)
            eloop.update_screen(pacman)
            pacman.update(maze, self.gamestats, self.pacmanGroup)
            for i in range(1):
                ghost[i].blit()
            self.update_screen()

    def update_screen(self):
        self.screen.fill(Game.BLACK)
        self.maze.blitme()
        self.pacman.blitme()

        pygame.display.flip()
        self.clock.tick(120)


game = Game()
game.play()
