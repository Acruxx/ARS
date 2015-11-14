import sys, pygame
from Vec2 import *
import math
import pdb

from Globals import *


class Car:
    def __init__(self, ang, rad):
        self.ang = ang
        self.rad = rad
        self.offsetAngle = 0

        self.img = None

        self.loadImage()

        self.breakImgTemplate = pygame.image.load("media/breakLights.png")

        self.box = self.imgTemplate.get_rect()

        self.pos = Vec2(0,0)

        self.truePos = Vec2(0,0)
        self.oldTruePos = Vec2(0,0)

        self.velVector = Vec2(0,0)
        self.oldVel = Vec2(0,0)

        self.size = Vec2(self.imgTemplate.get_width() * CAR_SCALE, self.imgTemplate.get_height() * CAR_SCALE)

        #changing size
        self.imgTemplate = pygame.transform.scale(self.imgTemplate, (int(self.size.x), int(self.size.y)))
        self.breakImgTemplate = pygame.transform.scale(self.breakImgTemplate, (int(self.size.x), int(self.size.y)))

        self.breaking = False

    def loadImage(self):
        self.imgTemplate = pygame.image.load("media/car.png")


    def update(self):
        self.updateGraphics()

    def updateGraphics(self):
        self.img = self.imgTemplate;
        self.breakImg = self.breakImgTemplate

        self.currAngle = -(self.ang + math.pi / 2)
        self.calculateOffsetAngle()

        #self.offsetAngle = math.pi / 3

        #self.img = pygame.transform.position(img, pos.getTuple())
        self.img = pygame.transform.rotate(self.img, (self.offsetAngle + math.pi) / math.pi * 180)
        self.breakImg = pygame.transform.rotate(self.breakImg, (self.offsetAngle + math.pi) / math.pi * 180)

        self.oldTruePos = self.truePos
        self.truePos = Vec2(
                BOARD_SIZE / 2 + math.cos(self.ang) * self.rad,
                BOARD_SIZE / 2 + math.sin(self.ang) * self.rad
                )

        #Calculate position
        self.pos = self.truePos - Vec2(
                    self.img.get_width() / 2,
                    self.img.get_height() / 2
                )


    def draw(self, screen):
        screen.blit(self.img, (self.pos.x, self.pos.y), self.box)
        #screen.blit(self.img, (0, 0), self.box)

        if self.breaking:
            screen.blit(self.breakImg, (self.pos.x, self.pos.y), self.box)

        
    def checkCollision(self, player):
        if getDistance(self.pos, player.pos) < self.size.x / 3:
            return True
        return False

    def calculateOffsetAngle(self):
        self.oldVel = self.velVector

        #Calculate the vector between the old and new position
        self.velVector = self.truePos - self.oldTruePos

        velAngle = self.velVector.getAngle()

        self.offsetAngle = -velAngle

        #print self.pos, self.oldPos, velVector


    
    def getAng(self):
        return self.ang

    def setAng(self, ang):
        self.ang = ang;

    def getRad(self):
        return self.rad
    
    def setRad(self, rad):
        self.rad = rad;

