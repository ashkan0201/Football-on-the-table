
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

# سرعت بازیکنان
PLAYER_SPEED = 5

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
    
    # شرایط و محدودیت های حرکتی بازیکن سمت چپ
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_speed = -PLAYER_SPEED
    elif keys[pygame.K_s]:
        player1_speed = PLAYER_SPEED
    else:
        player1_speed = 0

    # شرایط و محدودیت های حرکتی بازیکن سمت راست
    if keys[pygame.K_UP]:
        player2_speed = -PLAYER_SPEED
    elif keys[pygame.K_DOWN]:
        player2_speed = PLAYER_SPEED
    else:
        player2_speed = 0

    player1_pos[1] += player1_speed
    player2_pos[1] += player2_speed

    # محدود کردن بازیکن سمت چپ در نیمه خود
    if player1_pos[1] < 0:
        player1_pos[1] = 0
    elif player1_pos[1] > HEIGHT - PLAYER_HEIGHT:
        player1_pos[1] = HEIGHT - PLAYER_HEIGHT

    # محدود کردن بازیکن سمت راست در نیمه خود
    if player2_pos[1] < 0:
        player2_pos[1] = 0
    elif player2_pos[1] > HEIGHT - PLAYER_HEIGHT:
        player2_pos[1] = HEIGHT - PLAYER_HEIGHT

    # پس زمینه
    window.fill((48, 52, 69))

    # ترسیم المان ها
    pygame.draw.rect(window, (2, 170, 255), (player1_pos[0], player1_pos[1], PLAYER_WIDTH, PLAYER_HEIGHT))
    pygame.draw.rect(window, (255, 0, 81), (player2_pos[0], player2_pos[1], PLAYER_WIDTH, PLAYER_HEIGHT))

    pygame.draw.circle(window, (221, 144, 254), (ball_pos[0], ball_pos[1]), BALL_RADIUS)
    
    pygame.draw.aaline(window, (2, 202, 151), (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # نمایش امتیازها
    font = pygame.font.Font(None, 36)
    player1_score_text = font.render(str(player1_score), True, (2, 170, 255))
    player2_score_text = font.render(str(player2_score), True, (255, 0, 81))
    window.blit(player1_score_text, (WIDTH // 2 - 50, 10))
    window.blit(player2_score_text, (WIDTH // 2 + 40, 10))
    
    # بروزرسانی پنجره
    pygame.display.flip()
    clock.tick(60)

#ّ پایان بازی
pygame.quit()