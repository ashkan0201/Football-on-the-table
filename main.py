
"""
CB: ASHKAN & SHERVIN
2023/8/29 12:10:24
"""

import pygame
from pygame.locals import *

# ابعاد پنجره
WIDTH = 800
HEIGHT = 400

# ابعاد بازیکنان
PLAYER_WIDTH = 10
PLAYER_HEIGHT = 60

# ابعاد توپ
BALL_RADIUS = 6

# تعداد گل هر بازیکن
player1_score = 0
player2_score = 0

# مکان بازیکنان
player1_pos = [10, HEIGHT // 2 - PLAYER_HEIGHT // 2]
player2_pos = [WIDTH - 10 - PLAYER_WIDTH, HEIGHT // 2 - PLAYER_HEIGHT // 2]

# مکان توپ
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_pos = [WIDTH // 2, HEIGHT // 2]

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