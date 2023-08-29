
"""
CB: ASHKAN & SHERVIN
2023/8/29 12:10:24
"""

import pygame
from pygame.locals import *

# ابعاد پنجره
WIDTH = 800
HEIGHT = 400

# مقدار اولیه Pygame
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# حلقه اصلی بازی
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

#ّ پایان بازی
pygame.quit()