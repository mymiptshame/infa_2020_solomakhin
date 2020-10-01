import pygame
from pygame.draw import *
import numpy as np

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

# дом
x, y, width, height = 50, 200, 300, 500
rect(screen, (45, 35, 19), (x, y, width, height))
# крыша
polygon(screen, (20, 20, 20), ([x + 15, y - 25], [x + width - 15, y - 25], [x + 15 + width, y], [x - 15, y]))
rect(screen, (45, 45, 45), (x + 30, y - 65, 15, 40))
rect(screen, (45, 45, 45), (x + 60, y - 100, 30, 90))
rect(screen, (35, 35, 35), (x + 250, y - 100, 15, 75))
# закрываем трубу облаком
ellipse(screen, (25, 25, 25), (15, 95, 430, 35))
rect(screen, (45, 45, 45), (x + 160, y - 100, 20, 90))
# окна
for i in range(4):
    rect(screen, (222 - 50, 184 - 50, 135 - 50), (x + 25 + 70 * i, y, 40, 230))
# балкон
rect(screen, (25, 25, 25), (x - 25, y + 230, width + 50, 50))
rect(screen, (25, 25, 25), (x - 25, y + 160, width + 50, 20))
for i in range(7):
    rect(screen, (25, 25, 25), (x + 25 + i * 40, y + 180, 10, 50))
# окна
for i in range(3):
    if i == 2:
        rect(screen, (255, 255, 0), (x + 30 + i * 90, y + 300, 60, 100))
        break
    rect(screen, (55 + 30, 35 + 30, 19 + 30), (x + 30 + i * 90, y + 300, 60, 100))


# привидение
def ghost(point=(500, 500)):
    circle(screen, (200, 200, 200), point, 50)
    # polygon(screen, (255, 255, 255), (
    # [point[0] - 50, point[1]], [point[0] - 100, point[1] + 200], [point[0] + 100, point[1] + 170],
    # [point[0] + 50, point[1]]))
    # решаем СЛАУ чтобы найти полином описывающий точки приведения и сделать красивые плавные границы
    from_x_to_xy = lambda x, coef: sum([coef[i] * x ** i for i in range(len(coef))])
    # кладем все точки приведения
    points = []

    ghost_side_left = [[450, 500], [440, 560], [430, 590], [420, 630], [410, 660], [400, 670], [390, 675], [380, 710]]
    coef_matrix = np.array([[1, elem[0], elem[0] ** 2, elem[0] ** 3, elem[0] ** 4, elem[0] ** 5, elem[0] ** 6,
                             elem[0] ** 7] for elem in ghost_side_left])
    vector = np.array(list(map(lambda x: x[1], ghost_side_left)))
    coef_polynom = np.linalg.solve(coef_matrix, vector)

    x = list(range(380, 451))
    left_points = [[elem, int(from_x_to_xy(elem, coef_polynom))] for elem in x]
    left_points.reverse()
    points.extend(left_points)

    x = np.arange(381, 601)
    y = list(15*np.cos(x / 15) + 710 - 20*np.cos(380/15))
    ghost_side_down = [[x[i], int(y[i])] for i in range(len(x))]
    points.extend(ghost_side_down)

    points.extend([[550, 500], [450, 500]])
    polygon(screen, (200, 200, 200), points)
    # рисуем глаза
    circle(screen, (100, 200, 250), (point[0] - 20, point[1] - 20), 10)
    circle(screen, (100, 200, 250), (point[0] + 20, point[1] - 20), 10)
    circle(screen, (0, 0, 0), (point[0] - 18, point[1] - 22), 6)
    circle(screen, (0, 0, 0), (point[0] + 22, point[1] - 22), 6)
    ellipse(screen, (255, 255, 255), [point[0] + 24, point[1] - 25, 3, 2])
    ellipse(screen, (255, 255, 255), [point[0] - 16, point[1] - 25, 3, 2])






ghost()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
