import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))

# небо
rect(screen, (75, 75, 75), (0, 0, 600, 350))
# луна
circle(screen, (255, 255, 255), (500, 100), 70)
# облака (белогривые лошадки :)
ellipse(screen, (55, 55, 55), (200, 100, 300, 50))
ellipse(screen, (45, 45, 45), (350, 150, 250, 50))
ellipse(screen, (35, 35, 35), (50, 25, 500, 60))
ellipse(screen, (25, 25, 25), (15, 95, 430, 35))

#дом
rect(screen, (75, 60, 19), (50, 200, 300, 500))
# крыша
polygon(screen, (20, 20, 20), ([65, 175], [335, 175], [365, 200], [35, 200]))
rect(screen())



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()