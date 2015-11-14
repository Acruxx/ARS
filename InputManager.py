import pygame

class InputManager:
    def __init__(self):
        self.moveLeft = False
        self.moveRight = False

        self.accelerate = False
        self.decelerate = False

    def onEvent(self, event):
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.moveRight = True

            if event.key == pygame.K_a:
                self.moveLeft = True

            if event.key == pygame.K_s:
                self.decelerate = True

            if event.key == pygame.K_w:
                self.accelerate = True

         if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.moveRight = False

            if event.key == pygame.K_a:
                self.moveLeft = False

            if event.key == pygame.K_s:
                self.decelerate = False

            if event.key == pygame.K_w:
                self.accelerate = False

        
       
