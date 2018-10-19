import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group

from image_rect import ImageRect


class Pacman(Sprite):

    def __init__(self, screen):
        super(Pacman, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.pacimg = ImageRect(screen, 'pacman', 32, 32)
        self.rect = self.pacimg.rect

        #  Movement flag
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        self.movement_switches = 0
        self.can_warp = True

        self.pacimg.rect.centerx = self.screen_rect.centerx - 4
        #self.pacimg.rect.bottom = self.screen_rect.bottom - 124
        self.pacimg.rect.top = self.screen_rect.top + 128

    def blitme(self):
        self.screen.blit(self.pacimg.image, self.pacimg.rect)

    def update(self, maze, gamestats, pacmanGroup):
        self.check_collision(maze, gamestats, pacmanGroup)
        if self.moving_up or self.moving_down:
            self.handle_movement()
        elif self.moving_left or self.moving_right:
            self.handle_movement()

    #  Make better
    def check_collision(self, maze, gamestats, pacmanGroup):
        for nrow in range(len(maze.bricks)):
            if self.rect.colliderect(maze.bricks[nrow]):
                if self.moving_up:
                    self.rect.top = maze.bricks[nrow].bottom + 8
                    self.moving_up = False
                elif self.moving_down:
                    self.rect.bottom = maze.bricks[nrow].top - 8
                    self.moving_down = False
                elif self.moving_left:
                    self.rect.left = maze.bricks[nrow].right + 8
                    self.moving_left = False
                elif self.moving_right:
                    self.rect.right = maze.bricks[nrow].left - 8
                    self.moving_right = False
        self.handle_warp(maze)
        if pygame.sprite.groupcollide(pacmanGroup, maze.points, False, True):
            print("yeet")




    def handle_warp(self, maze):
        if self.rect.colliderect(maze.orangeportal) and self.can_warp:
            if maze.blueportal.height < maze.blueportal.width:
                self.rect.right = maze.blueportal.rect.left
                self.moving_up = self.moving_down = False
                self.moving_left = True
                self.can_warp = False
                self.handle_warp_delay()

        if self.rect.colliderect(maze.blueportal) and self.can_warp:
            if maze.orangeportal.height >= maze.orangeportal.width:
                self.rect.top = maze.orangeportal.rect.bottom
                self.moving_left = self.moving_right = False
                self.moving_down = True
                self.can_warp = False
                self.handle_warp_delay()


    def handle_movement(self):
        if self.moving_up and self.pacimg.rect.top > self.screen_rect.top:
            self.pacimg.rect.centery -= 5
        if self.moving_down and self.pacimg.rect.bottom < self.screen_rect.bottom:
            self.pacimg.rect.centery += 5
        if self.moving_left and self.pacimg.rect.left > self.screen_rect.left:
                self.pacimg.rect.centerx -= 5
        if self.moving_right and self.pacimg.rect.right < self.screen_rect.right:
                self.pacimg.rect.centerx += 5

    def handle_warp_delay(self):
        start_time = pygame.time.get_ticks()
        end_time = start_time + 400
        while start_time < end_time:
            start_time += 1
        self.can_warp = True
