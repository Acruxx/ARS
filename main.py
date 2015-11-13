import sys, pygame

pygame.init()

size = width, height = 1280, 720
speed = [0.2, 0.2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

roundaboutImage = pygame.image.load("media/roundabout.png")
#roundabout = pygame.image.load("ball.gif")
roundaboutRect = roundaboutImage.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    screen.blit(roundaboutImage, roundaboutRect)
    pygame.display.flip()
