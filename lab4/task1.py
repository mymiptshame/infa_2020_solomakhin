import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))


circle(screen, (255, 255, 0), (200, 175), 100)
circle(screen, (255, 0, 0), (150, 150), 30)
circle(screen, (255, 0, 0), (250, 150), 25)
circle(screen, (0, 0, 0), (150, 150), 15)
circle(screen, (0, 0, 0), (250, 150), 10)
rect(screen, (0, 0, 0), (125, 220, 125, 20))
line(screen, (0, 0, 0), [100, 95], [190, 125], 15)
line(screen, (0, 0, 0), [300, 95], [210, 125], 15)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()