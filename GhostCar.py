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

    def setFuture(self, future):
        if future != None:
            self.future = future;updateGraphics
