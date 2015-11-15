import pygame
import random
import math

from Vec2 import *
from Globals import *

class Coin:
    pickupSound = None
    def __init__(self):
        self.img = pygame.image.load("media/money.png")
        self.img = pygame.transform.scale(self.img, (50,50))
        self.box = self.img.get_rect()

        self.pos = Vec2(0,0)

        self.reposition()

        self.pickupSound = pygame.mixer.Sound("media/Pickup_Coin.wav")


    def draw(self, screen):
        screen.blit(self.img, self.pos.get_tuple(), self.box)

    def update(self, player):
        if getDistance(self.pos - Vec2(self.img.get_width(), self.img.get_height()), player.pos) < 50:
            self.reposition()
            player.addScore()

            self.pickupSound.play()

        self.updateGraphics()



    def updateGraphics(self):
        #Calculate position
        self.pos = Vec2(
                BOARD_SIZE / 2 + math.cos(self.ang) * self.rad,
                BOARD_SIZE / 2 + math.sin(self.ang) * self.rad
                )

    def draw(self, screen):
        screen.blit(self.img, (self.pos + screenshaker.offset - Vec2(self.img.get_width(), self.img.get_height()) / 2).getTuple(), self.box)


    def reposition(self):
        self.rad = 200 + 150 * random.random()
        self.ang = math.pi * 2 * random.random()

