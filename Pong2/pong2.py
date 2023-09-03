import pygame
from sys import exit
from time import sleep

pygame.init()

X, Y, = 1000, 700
screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Kazim - Pong')

clock = pygame.time.Clock()

player_a_surf = pygame.image.load('paddle.png').convert()
player_a_rect = player_a_surf.get_rect(center = (52, Y/2))

player_b_surf = pygame.image.load('paddle.png').convert()
player_b_rect = player_b_surf.get_rect(center = (948, Y/2))

ball_surf = pygame.image.load('ball.png').convert()
ball_rect = ball_surf.get_rect(center = (X/2, Y/2))

text = pygame.font.SysFont(None, 80)
a = b = 0

def refresh_a():
    score_a_surf = text.render(f'{a:02}', True, 'white')
    score_a_rect = score_a_surf.get_rect(midright = (475, 50))
    screen.blit(score_a_surf, score_a_rect)

def refresh_b():
    score_b_surf = text.render(f'{b:02}', True, 'white')
    score_b_rect = score_b_surf.get_rect(midleft = (525, 50))
    screen.blit(score_b_surf, score_b_rect)

x = y = 5
paddle_speed = 7

def one_player(condition):
    global x, y, a, b

    if condition:
        # automate player b
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player_a_rect.top >= 0: player_a_rect.y -= paddle_speed
        elif keys[pygame.K_s] and player_a_rect.bottom <= Y: player_a_rect.y += paddle_speed
        if ball_rect.y < player_b_rect.top and player_b_rect.top >= 0: player_b_rect.y -= 4
        if ball_rect.bottom > player_b_rect.bottom and player_b_rect.bottom <= Y: player_b_rect.y += 4
    
    else:
        # no automation
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player_a_rect.top >= 0: player_a_rect.y -= paddle_speed
        elif keys[pygame.K_s] and player_a_rect.bottom <= Y: player_a_rect.y += paddle_speed
        if keys[pygame.K_UP] and player_b_rect.top >= 0: player_b_rect.y -= paddle_speed
        elif keys[pygame.K_DOWN] and player_b_rect.bottom <= Y: player_b_rect.y += paddle_speed

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit('Thanks for playing')


    pygame.draw.rect(screen, 'black', pygame.Rect(0, 0, X, Y), 350)
    pygame.draw.rect(screen, 'white', pygame.Rect(0, 0, X, Y), 2)
    pygame.draw.rect(screen, 'white', pygame.Rect(X/2, 0, 5, Y))

    if a == b or a > b or b > a:
        refresh_a()
        refresh_b()
    
    ball_rect.x += x
    ball_rect.y += y
    if ball_rect.y <= 0 or ball_rect.midbottom[1] >= Y: y *= -1
    if ball_rect.right >= X:
        ball_rect.center = (X/2, Y/2)
        x *= -1
        a += 1
    elif ball_rect.left <= 0:
        ball_rect.center = (X/2, Y/2)
        x *= -1
        b += 1
    screen.blit(ball_surf, ball_rect)


    one_player(True) # Change to False for 2 player


    if ball_rect.left == player_a_rect.right and ball_rect.top <= player_a_rect.bottom and ball_rect.bottom >= player_a_rect.top: x *= -1
    elif player_a_rect.colliderect(ball_rect) and ball_rect.left < player_a_rect.right: y *= -1
    if ball_rect.right == player_b_rect.left and ball_rect.top <= player_b_rect.bottom and ball_rect.bottom >= player_b_rect.top: x *= -1
    elif player_b_rect.colliderect(ball_rect) and ball_rect.right > player_b_rect.left: y *= -1

    screen.blit(player_a_surf, player_a_rect)
    screen.blit(player_b_surf, player_b_rect)

    if a == 10:
        sleep(1)
        exit('player A wins')
    elif b == 10:
        sleep(1)
        exit('player B wins')
    
    pygame.display.update()
    clock.tick(120) # 144 or 120 are optimal speeds

    # Finished
