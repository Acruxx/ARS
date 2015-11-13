import sys, pygame
from Vec2 import *
import math

CAR_SCALE = 0.3;

BOARD_SIZE = 720

MOVE_SPEED = 3

class Car:
    def __init__(self, ang, rad):
        self.ang = ang
        self.rad = rad

        self.img = None

        self.imgTemplate = pygame.image.load("media/car.png")
        self.box = self.imgTemplate.get_rect()

        self.pos = Vec2(0,0)

        self.size = Vec2(self.imgTemplate.get_width() * CAR_SCALE, self.imgTemplate.get_height() * CAR_SCALE)

        #changing size
        self.imgTemplate = pygame.transform.scale(self.imgTemplate, (int(self.size.x), int(self.size.y)))

    def update(self, inputManager):
        if(inputManager.moveLeft):
            self.rad += MOVE_SPEED
        if(inputManager.moveRight):
            self.rad -= MOVE_SPEED

        self.img = self.imgTemplate;
        self.ang += 0.02

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
        


