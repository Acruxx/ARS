import pygame

class InputManager:
    def __init__(self):
        self.moveLeft = False
        self.moveRight = False

    def onEvent(self, event):
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                self.moveRight = True

         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                self.moveLeft = True

         if event.type == pygame.KEYUP:
            if event.key == pygame.K_l:
                self.moveRight = False

         if event.type == pygame.KEYUP:
            if event.key == pygame.K_h:
                self.moveLeft = False
       
