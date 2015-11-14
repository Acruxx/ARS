import sys, pygame
from InputManager import *
from car import *
from Player import *
from GhostTrack import *
import random

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
currentOffset = 0;


oldCars = []
oldTracks = []
oldOffsets = []

doneLaps = 0

def restartGame():
    oldTracks.append(currentTrack)
    oldOffsets.append(currentOffset)

    #Restart the game and spawn some stuff
    oldCars.append(Car(0, 200))

    for track in oldTracks:
        track.reset_count()

    startGame()
    

def startGame():
    currentOffset = random.random() * math.pi * 2
    currentTrack = GhostTrack()

    print(currentTrack.list_size)

    player.setAng(currentOffset);


def main():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            
            inputManager.onEvent(event);
    
        player.update(inputManager);
    
        currentTrack.add_pos(player.getAng(), player.getRad())
    
        print(currentTrack.list_size)
    
        if(player.getAng() > math.pi * 2):
            doneLaps += 1
            player.setAng(player.getAng() - math.pi * 2)
    
        if doneLaps == 2:
            restartGame()
            doneLaps = 0
    
        for i in range(0, len(oldCars)):
            oldCars[i].setAng(oldTracks[i].get_next_pos()[0])
            oldCars[i].setRad(oldTracks[i].get_next_pos()[1] + oldOffsets[i])
            oldCars[i].update()
    
        screen.fill(black)
        screen.blit(roundaboutImage, roundaboutRect)
        player.draw(screen);
    
        for car in oldCars:
            car.draw(screen)
    
        pygame.display.flip()

startGame()
main()
