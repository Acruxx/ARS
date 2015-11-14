from car import *

class Player(Car):
    def update(self, inputManager):
        if(inputManager.moveLeft):
            self.rad += MOVE_SPEED
        if(inputManager.moveRight):
            self.rad -= MOVE_SPEED

        self.ang += 0.02
        Car.update(self);

