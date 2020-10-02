import pygame
from pygame.draw import *
import numpy as np
import random

pygame.init()
FPS = 30
screen = pygame.display.set_mode((600, 800))

a=0
b=0
surf = pygame.Surface((600, 800), pygame.SRCALPHA)

rect(screen, (75, 75, 75), (0, 0, 600, 350)) #небо
circle(screen, (255, 255, 255), (500, 100), 70) #луна
ellipse(screen, (55, 55, 55), (200, 100, 300, 50)) # облака
ellipse(screen, (45, 45, 45), (350, 150, 250, 50)) # облака
ellipse(screen, (35, 35, 35), (50, 25, 500, 60)) # облака
ellipse(screen, (25, 25, 25), (15, 95, 430, 35)) # облака

def house(point,size):
    '''
    функция рисует дом
    навход: кортеж координат, размер дома
    на выход: рисует дом
    '''
    x, y, width, height = point[0], point[1], size, 5/3*size
    rect(screen, (45, 35, 19), (x, y, width, height))  # дом
    polygon(screen, (20, 20, 20),
            ([x + 15*size/300, y - 25*size/300], [x + width - 15*size/300, y - 25*size/300],
             [x + 15*size/300 + width, y], [x - 15*size/300, y]))  # крыша
    rect(screen, (45, 45, 45), (x + 30*size/300, y - 65*size/300, 15*size/300, 40*size/300))
    rect(screen, (45, 45, 45), (x + 60*size/300, y - 100*size/300, 30*size/300, 90*size/300))
    rect(screen, (35, 35, 35), (x + 250*size/300, y - 100*size/300, 15*size/300, 75*size/300))
    # закрываем трубу облаком
    ellipse(screen, (25, 25, 25), (x-35*size/300, y-105*size/300, 430*size/300, 35*size/300))
    rect(screen, (45, 45, 45), (x + 160*size/300, y - 100*size/300, 20*size/300, 90*size/300))
    # окна
    for i in range(4):
        rect(screen, (222 - 50, 184 - 50, 135 - 50), (x + 25*size/300 + 70*size/300 * i, y, 40*size/300, 230*size/300))
    # балкон
    rect(screen, (25, 25, 25), (x - 25*size/300, y + 230*size/300, width + 50*size/300, 50*size/300))
    rect(screen, (25, 25, 25), (x - 25*size/300, y + 160*size/300, width + 50*size/300, 20*size/300))
    for i in range(7):
        rect(screen, (25, 25, 25), (x + 25*size/300 + i*size/300 * 40, y + 180*size/300, 10*size/300, 50*size/300))
    # окна
    for i in range(3):
        j = random.randint(0,1)
        if j:
            rect(screen, (255, 255, 0), (x + 30*size/300 + i * 90*size/300, y + 300*size/300, 60*size/300, 100*size/300))
        else:
            rect(screen, (55 + 30, 35 + 30, 19 + 30), (x + 30*size/300 + i * 90*size/300, y + 300*size/300, 60*size/300, 100*size/300))


def ghost(point,size):
    '''
    функция рисует привидение
    на вход: кортеж координат, размер духа
    на выход: рисует привидение
    '''
    circle(surf, (200,200,200,127), point, int(size/4))
    # решаем СЛАУ чтобы найти полином описывающий точки приведения и сделать красивые плавные границы
    from_x_to_xy = lambda x, coef: sum([coef[i] * x ** i for i in range(len(coef))])
    # кладем все точки приведения
    points = []
    ghost_side_left = [[point[0]-50*size/200, point[1]], [point[0]-60*size/200, point[1]+60*size/200], [point[0]-70*size/200, point[1]+90*size/200], [point[0]-80*size/200, point[1]+130*size/200], [point[0]-90*size/200, point[1]+160*size/200], [point[0]-100*size/200, point[1]+170*size/200], [point[0]-110*size/200, point[1]+175*size/200], [point[0]-120*size/200, point[1]+210*size/200]]
    coef_matrix = np.array([[1, elem[0], elem[0] ** 2, elem[0] ** 3, elem[0] ** 4, elem[0] ** 5, elem[0] ** 6,
                             elem[0] ** 7] for elem in ghost_side_left])
    vector = np.array(list(map(lambda x: x[1], ghost_side_left)))
    coef_polynom = np.linalg.solve(coef_matrix, vector)

    x = list(range(point[0]-int(120*size/200), point[0]-int(49*size/200)))
    left_points = [[elem, int(from_x_to_xy(elem, coef_polynom))] for elem in x]
    left_points.reverse()
    points.extend(left_points)

    x = np.arange(point[0]-119*size/200, point[0]+101*size/200)
    y = list(15*np.cos(x/(size/200) / 15)*size/200 + point[1]+210*size/200 - 20*np.cos(380/15)*size/200)
    ghost_side_down = [[x[i], int(y[i])] for i in range(len(x))]
    points.extend(ghost_side_down)
    points.extend([[point[0]+50*size/200, point[1]], [point[0]-50*size/200, point[1]]])
    polygon(surf, (200,200,200,127), points)
    # рисуем глаза
    circle(surf, (100, 200, 250), (point[0] - int(20*size/200), point[1] - int(20*size/200)), int(size/20))
    circle(surf, (100, 200, 250), (point[0] + int(20*size/200), point[1] - int(20*size/200)), int(size/20))
    circle(surf, (0, 0, 0), (point[0] - int(18*size/200), point[1] - int(22*size/200)), int(size*0.03))
    circle(surf, (0, 0, 0), (point[0] + int(22*size/200), point[1] - int(22*size/200)), int(size*0.03))
    ellipse(surf, (255, 255, 255), [point[0] + 24*size/200, point[1] - 25*size/200, 3*size/200, 2*size/200])
    ellipse(surf, (255, 255, 255), [point[0] - 16*size/200, point[1] - 25*size/200, 3*size/200, 2*size/200])
    surf.set_alpha(10)
house((50,200),100)
house((250,200),100)
house((450,200),100)
screen0 = screen.copy()
p = (400, 200)
ghost(p, 100)




pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            # decrement in x co-ordinate
            a += 10
            screen.blit(screen0,(0,0))
            screen.blit(surf, (a, b))
            pygame.display.update()
        elif keys[pygame.K_LEFT]:
            # decrement in x co-ordinate
            a -= 10
            screen.blit(screen0,(0,0))
            screen.blit(surf, (a, b))
            pygame.display.update()
        elif keys[pygame.K_DOWN]:
            # decrement in x co-ordinate
            b += 10
            screen.blit(screen0,(0,0))
            screen.blit(surf, (a, b))
            pygame.display.update()
        elif keys[pygame.K_UP]:
            # decrement in x co-ordinate
            b -= 10
            screen.blit(screen0,(0,0))
            screen.blit(surf, (a, b))
            pygame.display.update()


pygame.quit()