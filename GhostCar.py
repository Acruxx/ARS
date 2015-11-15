from car import *

class GhostCar(Car):
    def __init__(self):
        Car.__init__(self, 0, 0)

        self.future = None
        self.oldVel = Vec2(0, 0)


    def updateGraphics(self):
        Car.updateGraphics(self)

        if self.velVector.getLen() < self.oldVel.getLen():
            self.breaking = True
        else:
            self.breaking = False

        if self.future != None:
            if self.future[1] > self.rad + 30:
                self.turning = 1
            elif self.future[1] < self.rad - 30:
                self.turning = -1
            else:
                self.turning = 0

    def setFuture(self, future):
        if future != None:
            self.future = future;

