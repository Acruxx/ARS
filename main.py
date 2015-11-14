import sys, pygame
from InputManager import *
from car import *
from Player import *
from GhostTrack import *

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

player = Player(0, 200);

currentTrack = GhostTrack();

doneLaps = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
        inputManager.onEvent(event);

    player.update(inputManager);

    if(player.getAng() > math.pi * 2):
        doneLaps += 1
        player.setAng(player.getAng() - math.pi * 2)


    screen.fill(black)
    screen.blit(roundaboutImage, roundaboutRect)
    player.draw(screen);
    pygame.display.flip()
