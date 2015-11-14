import pygame
import random
import math

from Vec2 import *
from Globals import *

class Coin:
    def __init__(self):
        self.img = pygame.image.load("media/money.png")
        self.img = pygame.transform.scale(self.img, (50,50))
        self.box = self.img.get_rect()

        self.pos = Vec2(0,0)

        self.reposition()


    def draw(self, screen):
        screen.blit(self.img, self.pos.get_tuple(), self.box)

    def update(self, player):
        if getDistance(self.pos, player.pos) < 50:
            self.reposition()
            player.addScore()

        self.updateGraphics()



    def updateGraphics(self):
        #Calculate position
        self.pos = Vec2(
                BOARD_SIZE / 2 + math.cos(self.ang) * self.rad - self.img.get_width() / 2,
                BOARD_SIZE / 2 + math.sin(self.ang) * self.rad - self.img.get_height() / 2
                )

    def draw(self, screen):
        screen.blit(self.img, (self.pos.x, self.pos.y), self.box)
        #screen.blit(self.img, (0, 0), self.box)

    def reposition(self):
        self.rad = 200 + 150 * random.random()
        self.ang = math.pi * 2 * random.random()

