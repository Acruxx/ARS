import sys, pygame
from Vec2 import *
import math
import pdb

from Globals import *


class Car:
    def __init__(self, ang, rad):
        self.ang = ang
        self.rad = rad

        self.img = None

        self.loadImage()
        self.box = self.imgTemplate.get_rect()

        self.pos = Vec2(0,0)

        self.size = Vec2(self.imgTemplate.get_width() * CAR_SCALE, self.imgTemplate.get_height() * CAR_SCALE)

        #changing size
        self.imgTemplate = pygame.transform.scale(self.imgTemplate, (int(self.size.x), int(self.size.y)))

    def loadImage(self):
        self.imgTemplate = pygame.image.load("media/car.png")


    def update(self):
        self.updateGraphics()

    def updateGraphics(self):
        self.img = self.imgTemplate;

        #self.img = pygame.transform.position(img, pos.getTuple())
        self.img = pygame.transform.rotate(self.img, -(self.ang / math.pi * 180 - 90))

        #Calculate position
        self.pos = Vec2(
                BOARD_SIZE / 2 + math.cos(self.ang) * self.rad - self.img.get_width() / 2,
                BOARD_SIZE / 2 + math.sin(self.ang) * self.rad - self.img.get_height() / 2
                )

    def draw(self, screen):
        screen.blit(self.img, (self.pos.x, self.pos.y), self.box)
        #screen.blit(self.img, (0, 0), self.box)
        
    def checkCollision(self, player):
        if getDistance(self.pos, player.pos) < self.size.x / 3:
            return True
        return False


    
    def getAng(self):
        return self.ang

    def setAng(self, ang):
        self.ang = ang;

    def getRad(self):
        return self.rad
    
    def setRad(self, rad):
        self.rad = rad;

