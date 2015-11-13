import sys, pygame
from InputManager import *
from car import *

pygame.init()

BOARD_SIZE = 720

size = width, height = BOARD_SIZE, BOARD_SIZE
speed = [0.2, 0.2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

roundaboutImage = pygame.image.load("media/roundabout.png")
#roundabout = pygame.image.load("ball.gif")
roundaboutRect = roundaboutImage.get_rect()

roundaboutImage = pygame.transform.scale(roundaboutImage, (BOARD_SIZE,BOARD_SIZE));

inputManager = InputManager()

car = Car(0, 200);

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
        inputManager.onEvent(event);

    car.update(inputManager);

    screen.fill(black)
    screen.blit(roundaboutImage, roundaboutRect)
    car.draw(screen);
    pygame.display.flip()
