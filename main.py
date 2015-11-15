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

pygame.mixer.init()

STATE_MENU = 0
STATE_GAME = 1
STATE_COUNTDOWN = 2

class HighScoreDisplay:
    def __init__(self):
        self.BOARD_SIZE = 720
        
        self.size = width, height = self.BOARD_SIZE, self.BOARD_SIZE

        self.black = 0, 0, 0
        
        self.screen = pygame.display.set_mode(self.size)
        self.roundaboutImage = pygame.image.load("media/roundaboutNew.png")
        self.roundaboutImage = pygame.transform.scale(self.roundaboutImage, self.size);
        self.roundaboutRect = self.roundaboutImage.get_rect()

        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 60)

    def run(self):
        while 1:
            self.screen.fill(self.black)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return
                    if event.key == pygame.K_q:
                        sys.exit()
                

            #self.screen.blit(self.roundaboutImage, screenshaker.offset.getTuple(), self.roundaboutRect)
            self.screen.blit(self.roundaboutImage, screenshaker.offset.getTuple(), self.roundaboutRect)

            yPos = 0
            for line in highScore.getString().split("\n"):
                textSurface = self.font.render(line, True, (255,255,255))
                self.screen.blit(textSurface, (0,yPos), textSurface.get_rect())
                yPos += textSurface.get_height()





            pygame.display.flip()

class Game:
    def __init__(self):
        self.BOARD_SIZE = 720
        
        self.size = width, height = self.BOARD_SIZE, self.BOARD_SIZE
        self.speed = [0.2, 0.2]
        self.black = 0, 0, 0
        
        self.screen = pygame.display.set_mode(self.size)
        self.roundaboutImage = pygame.image.load("media/roundaboutNew.png")
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

        self.explosionSound = pygame.mixer.Sound("media/Explosion.wav")

    
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

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                
                self.inputManager.onEvent(event);
        
            if self.state == STATE_GAME:
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
                        self.player.shakeSound.stop()

                        score = self.player.score
                        
                        self.explosionSound.play()

                        print "You died, final score: {}".format(score)

                        pygame.display.quit()

                        if(score >= highScore.getLowest()):
                            name = raw_input("New high score, what's your name?\n")

                            highScore.addScore(name, score)

                        highScore.save()
                        return


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

pygame.mixer.music.load("media/AmericanRoundabout.ogg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

while True:
    game = Game()
    game.startGame()
    game.main()
    
    scoreDisplay = HighScoreDisplay()
    scoreDisplay.run()
