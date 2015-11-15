import sys, pygame
from InputManager import *
from car import *
from Player import *
from GhostTrack import *
from GhostCar import *
from Coin import *
import random
import time

pygame.init()

STATE_MENU = 0
STATE_GAME = 1
STATE_COUNTDOWN = 2

class Game:
    def __init__(self):
        self.BOARD_SIZE = 720
        
        self.size = width, height = self.BOARD_SIZE, self.BOARD_SIZE
        self.speed = [0.2, 0.2]
        self.black = 0, 0, 0
        
        self.screen = pygame.display.set_mode(self.size)
        self.roundaboutImage = pygame.image.load("media/roundabout.png")
        #roundabout = pygame.image.load("ball.gif")
        self.readyImg = pygame.image.load("media/readyScreen.png")
        
        self.roundaboutImage = pygame.transform.scale(self.roundaboutImage, self.size);
        self.readyImg = pygame.transform.scale(self.readyImg, self.size);

        self.roundaboutRect = self.roundaboutImage.get_rect()
        self.readyBox = self.readyImg.get_rect()
        
        self.inputManager = InputManager()
        
        self.player = Player(0, 200);
        
        self.currentTrack = GhostTrack();
        self.currentOffset = 0
        
        self.oldCars = []
        self.oldTracks = []
        self.oldOffsets = []
        
        self.doneLaps = 0

        self.framesToRun = 1000

        self.waves = 0

        self.state = STATE_MENU

    
    def restartGame(self):
        self.oldTracks.append(self.currentTrack)
        self.oldOffsets.append(self.currentOffset)
    
        #Restart the game and spawn some stuff
        self.oldCars.append(GhostCar())
    
        for track in self.oldTracks:
            track.reset_count()
    
        self.startGame()

        
    
    def startGame(self):
        self.currentOffset = random.random() * math.pi * 2
        self.currentTrack = GhostTrack()

        self.player.resetCar();
        self.player.setAng(self.currentOffset);

        self.currentFrame = 0

        self.state = STATE_COUNTDOWN
        self.startTime = time.time()
        
        self.waves += 1

        self.coin = Coin()
    
    
    def main(self):
        while 1:
            self.screen.fill(self.black)

            if self.state == STATE_GAME:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: sys.exit()
                    
                    self.inputManager.onEvent(event);
        
                self.player.update(self.inputManager);
        
                self.currentTrack.add_pos(self.player.getAng(), self.player.getRad())

                self.currentFrame += 1
        
                if self.currentFrame >= self.framesToRun:
                    self.restartGame()
        
                for i in range(0, len(self.oldCars)):
                    oldPos = self.oldTracks[i].get_next_pos()

                    self.oldCars[i].setAng(oldPos[0])
                    self.oldCars[i].setRad(oldPos[1] + self.oldOffsets[i])
                    self.oldCars[i].update()
                    self.oldCars[i].setFuture(self.oldTracks[i].get_future_pos(60))

                    if self.oldCars[i].checkCollision(self.player):
                        score = self.player.score

                        print "You died, final score: {}".format(score)

                        if(score >= highScore.getLowest()):
                            name = raw_input("New high score, what's your name?")

                            highScore.addScore(name, score)

                        highScore.printScore()
                        highScore.save()

                        sys.exit(0)

                self.coin.update(self.player)

            elif self.state == STATE_COUNTDOWN:
                if(time.time() > self.startTime + 1): 
                    self.state = STATE_GAME

                for car in self.oldCars:
                    car.updateGraphics()

                self.player.updateGraphics()
                self.coin.updateGraphics()

        
            #self.screen.blit(self.roundaboutImage, screenshaker.offset.getTuple(), self.roundaboutRect)
            self.screen.blit(self.roundaboutImage, screenshaker.offset.getTuple(), self.roundaboutRect)
            self.player.draw(self.screen);

            for car in self.oldCars:
                car.draw(self.screen)

            self.coin.draw(self.screen)

            if self.state == STATE_COUNTDOWN:
                self.screen.blit(self.readyImg, self.readyBox)

            pygame.display.flip()

game = Game()
game.startGame()
game.main()
