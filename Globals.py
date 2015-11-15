import random

from Screenshaker import *
from HighScore import *

CAR_SCALE = 0.3;

BOARD_SIZE = 720

MIN_RAD = 200
MAX_RAD = 130

MAX_SHAKE_RAD = 120
MIN_SHAKE_RAD = 202

screenshaker = Screenshaker()

def getRandomRadius():
    return MIN_RAD + MAX_RAD * random.random()

highScore = HighScore()
