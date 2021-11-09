"""
Name: Zi Yi Xiao
bumper.py

Problem: This program creates two circles of different colors and chooses initial
random directions for them to move.

Certification of Authenticity:
I certify that this assignment is my own work, but I got help from the internet (stackoverflow.com)
to complete this program.
"""

import pygame

pygame.init()

window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

x1, y1, r1, mx1, my1 = 200, 200, 14, 2, 0.5
x2, y2, r2, mx2, my2 = 300, 200, 14, -1, -1.5


def move(c, v, r, m):
    c += v
    if c < r: c, v = r, -v
    if c > m - r: c, v = m - r, -v
    return c, v


running = True
while running:
    clock.tick(60)
    x1, mx1 = move(x1, mx1, r1, 400)
    y1, my1 = move(y1, my1, r1, 400)
    x2, mx2 = move(x2, mx2, r2, 400)
    y2, my2 = move(y2, my2, r2, 400)

    v1 = pygame.math.Vector2(x1, y1)
    v2 = pygame.math.Vector2(x2, y2)

    nv = v2 - v1
    m1 = pygame.math.Vector2(mx1, my1)
    m2 = pygame.math.Vector2(mx2, my2)
    mx1, my1 = m1.x, m1.y
    mx2, my2 = m2.x, m2.y

    window.fill((255, 255, 255))
    pygame.draw.circle(window, (255, 0, 0), (round(x1), round(y1)), r1)
    pygame.draw.circle(window, (0, 0, 255), (round(x2), round(y2)), r2)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
