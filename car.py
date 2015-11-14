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
        self.turnLeftImgTemplate = pygame.image.load("media/turnLeft.png")
        self.turnRightImgTemplate = pygame.image.load("media/turnRight.png")

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
        self.turnRightImgTemplate = pygame.transform.scale(self.turnRightImgTemplate, (int(self.size.x), int(self.size.y)))
        self.turnLeftImgTemplate = pygame.transform.scale(self.turnLeftImgTemplate, (int(self.size.x), int(self.size.y)))

        self.breaking = False
        self.turning = 0

    def loadImage(self):
        self.imgTemplate = pygame.image.load("media/car.png")

    
    def onMaxRadius(self):
        pass
    def onMinRadius(self):
        pass


    def update(self):
        if(self.rad > MAX_RAD + MIN_RAD):
            self.rad = MAX_RAD + MIN_RAD
            self.onMaxRadius()
        elif(self.rad < MIN_RAD):
            self.rad = MIN_RAD
            self.onMinRadius()

        self.updateGraphics()

    def updateGraphics(self):

        self.currAngle = -(self.ang + math.pi / 2)
        self.calculateOffsetAngle()

        #self.offsetAngle = math.pi / 3

        #self.img = pygame.transform.position(img, pos.getTuple())
        self.img = self.rotateImage(self.imgTemplate)
        self.breakImg = self.rotateImage(self.breakImgTemplate)
        self.turnRightImg = self.rotateImage(self.turnRightImgTemplate)
        self.turnLeftImg = self.rotateImage(self.turnLeftImgTemplate)

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

        if self.turning == -1:
            screen.blit(self.turnRightImg, (self.pos.x, self.pos.y), self.box)
        elif self.turning == 1:
            screen.blit(self.turnLeftImg, (self.pos.x, self.pos.y), self.box)

        
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

    def rotateImage(self, image):
        return pygame.transform.rotate(image, (self.offsetAngle + math.pi) / math.pi * 180)
    
    def getAng(self):
        return self.ang

    def setAng(self, ang):
        self.ang = ang;

    def getRad(self):
        return self.rad
    
    def setRad(self, rad):
        self.rad = rad;


