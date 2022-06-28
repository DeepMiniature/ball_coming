import pygame
import random
import math
#from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((690,690))
pygame.display.set_caption('Ball Coming')
#mixer.music.load('Charas Ganja Mereko Pyara.mp3')
#mixer.music.play(-1)

# variables used in program
ball_show = 'no'
ball_x = 322
ball_y = 600
ball_up, ball_down, ball_right, ball_left = 'no', 'no', 'no', 'no'
background_show = 'no'
bkrd_y1 = 0
bkrd_y2 = -690
bkrd_change_up, bkrd_change_down = 'no', 'no'
font1 = pygame.font.Font('LHANDW_0.TTF', 20)
start = False
font2 = pygame.font.Font('LHANDW_0.TTF',50)
game_over = font2.render('GAME OVER', True, (255, 215, 0))
game_over_print = False
score = 0
fun = True

# images
ball = pygame.image.load('ball.png')
background1 = pygame.image.load('bkrnd.png')
background2 = pygame.image.load('bkrnd.png')

# enemy balls
ball_enemy = []
for i in range(5):
    ball_enemy.append(pygame.image.load('ball1.png'))
ball_enemy_x = [322, 422, 222, 322, 222]
ball_enemy_y = [0, -230, -460, -690, -910]
ball_enemy_x_change = [2.5, 2.5, 2.5, 2.5, 2.5]
speed = 0

running = True

# functions
def show(x1, y1):
    global ball, ball_show
    msg1 = font1.render("Press F1 to START", True, (0, 35, 102))
    screen.blit(msg1, (10,90))
    screen.blit(ball, (x1, y1))

def show_enemy(x1, y1):
    global ball, ball_enemy
    screen.blit(ball_enemy, (340, 200))

def ball_enemy_mov(i):
    global ball1, ball_enemy_x, ball_enemy_y, ball_enemy, ball_enemy_x_change, ball_enemy_y_change, score

    ball_enemy_y[i] += 3

    if ball_enemy_y[i] >= 690:
        ball_enemy_y[i] = -460
        lane = random.randint(1,3)
        score = score + 5

        if lane == 1:
            ball_enemy_x[i] = 222

        elif lane == 2:
            ball_enemy_x[i] = 322

        elif lane == 3:
            ball_enemy_x[i] = 422

    if ball_enemy_x[i] <= 200:
        ball_enemy_x_change[i] = 2.5

    elif ball_enemy_x[i] >= 430:
        ball_enemy_x_change[i] = -2.5

    ball_enemy_x[i] += ball_enemy_x_change[i]

    screen.blit(ball_enemy[i], (ball_enemy_x[i], ball_enemy_y[i]))

def collision(i):
    global ball_enemy_x, ball_enemy_y, ball_x, ball_y
    distance = math.sqrt((ball_x - ball_enemy_x[i])**2 + (ball_y - ball_enemy_y[i])**2)
    if distance < 50:
        return True
    else:
        return False

def show_score():
    global score, font1
    print_score = font1.render('SCORE:'+str(score), True, (0, 34, 100))
    screen.blit(print_score, (530, 90))

def deep():
    global font2
    deep = font2.render('Welcome to DEEP Games', True, (0, 52, 250))
    screen.blit(deep, (10, 340))

while running:
#    screen.fill((200, 160, 234))
    screen.blit(background1, (0, bkrd_y1))
    screen.blit(background2, (0, bkrd_y2))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_F1:
                start = True
                game_over_print = False
                score = 0

            elif event.key == pygame.K_KP_ENTER:
                ball_show = 'yes'
                fun = False

            if event.key == pygame.K_UP:
                ball_up = 'no'
                bkrd_change_up = 'yes'

            if event.key == pygame.K_DOWN:
                ball_down = 'no'
                bkrd_change_down = 'yes'

            if event.key == pygame.K_LEFT:
                ball_left = 'yes'

            if event.key == pygame.K_RIGHT:
                ball_right = 'yes'

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_F1:
                pass

            elif event.key == pygame.K_KP_ENTER:
                pass

            if event.key == pygame.K_UP:
                ball_up = 'no'
                bkrd_change_up = 'no'

            if event.key == pygame.K_DOWN:
                ball_down = 'no'
                bkrd_change_down = 'no'

            if event.key == pygame.K_LEFT:
                ball_left = 'no'

            if event.key == pygame.K_RIGHT:
                ball_right = 'no'

    if ball_up == 'yes':
        if ball_y >= 10:
            ball_y -= 2

    if ball_down == 'yes':
        if ball_y <= 620:
            ball_y += 2

    if ball_left == 'yes':
        if ball_x >= 200:
            ball_x -= 7

    if ball_right == 'yes':
        if ball_x <= 430:
            ball_x += 7

    if bkrd_change_up == 'yes':
        bkrd_y1 += 3
        bkrd_y2 += 3

        if bkrd_y1 >= 690:
            bkrd_y1 = -690

        if bkrd_y2 >= 690:
            bkrd_y2 = -690

    if bkrd_change_down == 'yes':
        bkrd_y1 -= 3
        bkrd_y2 -= 3

        if bkrd_y1 <= -690:
            bkrd_y1 = 690

        if bkrd_y2 <= -690:
            bkrd_y2 = 690

    if fun:
        deep()

    if start == True:

        for j in range(5):
            ball_enemy_mov(j)

            if collision(j):
                start = False
                take = [0, -230, -460, -690, -910]

                for i in range(5):
                    ball_enemy_y[i] = take[i]

                game_over_print = True

    if game_over_print:
        screen.blit(game_over, (170, 340))

    if ball_show == 'yes':
        show(ball_x, ball_y)

    show_score()
#    show_enemy(0, 0)

    pygame.display.update()
