from Vec2 import *
import random

MAX_OFFSET = 10

class Screenshaker:
    def __init__(self):
        self.offset = Vec2(0,0)

    def shake(self):
        self.offset = Vec2(MAX_OFFSET * random.random() - MAX_OFFSET / 2, MAX_OFFSET * random.random() - MAX_OFFSET / 2)

