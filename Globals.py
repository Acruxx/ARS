import random

CAR_SCALE = 0.3;

BOARD_SIZE = 720

MIN_RAD = 200
MAX_RAD = 130

def getRandomRadius():
    return MIN_RAD + MAX_RAD * random.random()
