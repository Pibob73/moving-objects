import math
from pygame import draw
import pygame

pygame.init()
sc = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
rad = 60
radX = 60
while True:
    X = 250 + 150 * math.cos(math.pi / 2 - rad)
    Y = 250 + 150 * math.sin(math.pi / 2 - rad)
    Xb = X + 50 * math.cos(radX)
    Yb = Y + 50 * math.sin(radX)
    rad += 0.01
    radX += 0.5
    sc.fill((0, 0, 0))
    draw.circle(sc, (255, 0, 255), (X, Y), 10)
    draw.circle(sc, (0, 0, 255), (Xb, Yb), 10)
    pygame.display.update()
    clock.tick(30)
