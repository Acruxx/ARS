import sys, pygame
from InputManager import *

pygame.init()

size = width, height = 720, 720
speed = [0.2, 0.2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

roundaboutImage = pygame.image.load("media/roundabout.png")
#roundabout = pygame.image.load("ball.gif")
roundaboutRect = roundaboutImage.get_rect()

roundaboutImage = pygame.transform.scale(roundaboutImage, (720,720));

inputManager = InputManager()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
        inputManager.onEvent(event);
        
    screen.fill(black)
    screen.blit(roundaboutImage, roundaboutRect)
    pygame.display.flip()
