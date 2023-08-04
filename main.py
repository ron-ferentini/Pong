# pong16
# Ron Ferentini

import pygame
from pygame.locals import *
import time, random

pygame.init()

# Variables
ScreenWidth = 800
ScreenHeight = 600

BallX = random.randint(300,500)
BallY = random.randint(100,500)
BallSize = 10
BallHalf = BallSize / 2
BallLocation = (BallX, BallY)
dx = random.choice([-3,3])    # change in x value
dy = random.choice([-3,3])    # change in y value

RPaddleW = 20
RPaddleH = 80
RPaddleX = ScreenWidth - 30
RPaddleY = (ScreenHeight / 2) - (RPaddleH / 2)
RPaddle = (RPaddleX, RPaddleY, RPaddleW, RPaddleH)
RPaddleUpOrDown = 0

LPaddleW = 20
LPaddleH = 80
LPaddleX = 10
LPaddleY = (ScreenHeight / 2) - (LPaddleH / 2)
LPaddle = (LPaddleX, LPaddleY, LPaddleW, LPaddleH)

RScore = 0
LScore = 0

# Constant
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
GRAY = (128,128,128)


# create a Pygame window
pygame.display.set_caption("Pong")
screen = pygame.display.set_mode((ScreenWidth,ScreenHeight))
MyFont = pygame.font.SysFont(None, 100)
MySmallFont = pygame.font.SysFont(None, 30)
Message = ''

WidthOfNet = 10
CenterOfScreen = ScreenWidth / 2
LeftSideOfNet = CenterOfScreen - (WidthOfNet / 2)

PointScored = False
NewGame = False

# standard pygame game loop
GameRunning = True
while GameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRunning = False
        #keyboard events
        if event.type == pygame.KEYDOWN and event.key == K_DOWN:
            RPaddleUpOrDown = 3
        if event.type == pygame.KEYDOWN and event.key == K_UP:
            RPaddleUpOrDown = -3
        if event.type == KEYUP and (event.key == K_DOWN or event.key == K_UP):
            RPaddleUpOrDown = 0
        if event.type == pygame.KEYDOWN and event.key == K_n:
            if NewGame == True:
                Message = ''
                dx = random.choice([-3,3])
                dy = random.choice([-3,3])
                LScore = 0
                RScore = 0
                NewGame = False

    BallX += dx
    BallY += dy
    BallLocation = (BallX, BallY)

    # check if the Right Paddle goes off the top of the screen
    if RPaddleY < 0:
        RPaddleY = 0

    # check if the Right Paddle goes off the bottom of the screen
    if RPaddleY + RPaddleH > ScreenHeight:
        RPaddleY = ScreenHeight - RPaddleH
        
    # ball goes off the right side
    if BallX > ScreenWidth - BallHalf:
        LScore += 1
        PointScored = True
    # ball goes off the left side
    if BallX < BallHalf:
        RScore += 1
        PointScored = True

    if LScore == 10 or RScore == 10:
        Message = 'GAME OVER! Press N for New Game'
        NewGame = True

    if NewGame == True:
        TextImg = MySmallFont.render(Message, True, GRAY, BLACK)
        screen.blit(TextImg, (240,75))
        dx = 0
        dy = 0
        BallX = 400
        BallY = 300
        #GameRunning = False

    #if PointScored == True:
        #Message = 'Press SPACE to continue'
        #dx = 0
        #dy = 0
        #BallX = 400
        #BallY = 300
        #PointScored = False
        
    # bounce code
    if (BallX > ScreenWidth - BallHalf or BallX < BallHalf) or PointScored == True:
        dx *= -1

    if (BallY > ScreenHeight - BallHalf or BallY < BallHalf) or PointScored == True:
        dy *= -1
        
    if PointScored == True:
        PointScored = False
        
    # Collision detection w/ RPaddle
    if BallX + BallHalf > RPaddleX and \
       BallX - BallHalf < RPaddleX + RPaddleW and \
       BallY > RPaddleY and \
       BallY < RPaddleY + RPaddleH:
        dx *= -1

    # Collision detection w/LPaddle
    if BallX - BallHalf < LPaddleX  + LPaddleW  and \
       BallY > LPaddleY and \
       BallY < LPaddleY + LPaddleH:
        dx *= -1
      
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (LeftSideOfNet,0,WidthOfNet,ScreenHeight))    
    pygame.draw.circle(screen, RED, BallLocation, BallSize, BallSize)

    RPaddleY += RPaddleUpOrDown
    RPaddle = (RPaddleX, RPaddleY, RPaddleW, RPaddleH)
    pygame.draw.rect(screen, BLUE, RPaddle)

    if NewGame == False:
        if BallY > LPaddleY + (LPaddleH / 2):       # below bottom half of the paddle
            LPaddleY += random.randint(-1,5)
        else:   # above
            LPaddleY -= random.randint(-1,5)

    LPaddle = (LPaddleX, LPaddleY, LPaddleW, LPaddleH)
    pygame.draw.rect(screen, GREEN, LPaddle)

    TextImg = MyFont.render(str(RScore), True, BLUE, WHITE)
    TextRect = TextImg.get_rect()
    TextRect.midtop = (450,10)
    screen.blit(TextImg, TextRect)

    TextImg = MyFont.render(str(LScore), True, GREEN, WHITE)
    TextRect = TextImg.get_rect()
    TextRect.midtop = (350,10)    
    screen.blit(TextImg, TextRect)

    TextImg = MySmallFont.render(Message, True, GRAY, BLACK)
    TextRect = TextImg.get_rect()
    TextRect.midtop = (400,100)    
    screen.blit(TextImg, TextRect)
    
    pygame.display.update()
    time.sleep(0.005)
# end of the while loop
print("Game Over")
pygame.quit()
