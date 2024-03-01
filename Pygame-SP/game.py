import pygame
import random
pygame.init()
screenWidth = 1000
screenHeight = 500
size = screenWidth,screenHeight
screen = pygame.display.set_mode(size)

bg = pygame.image.load('bgg.png')
frogImg = pygame.image.load('frog1.png')

frogWidth = frogImg.get_width()
frogHeight = frogImg.get_height()

frogX = random.randint(1,screenWidth-frogWidth)
frogY = random.randint(1,screenHeight-frogHeight)

red = 255,0,0
white = 255,255,255
x,y,w,h = 0,0,50,50

def drawSnake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(screen,white,[snakeList[i][0],snakeList[i][1],w,h])



move_x = 0
move_y = 0
snakeList = []
snakelength = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = 0.3
                move_y = 0

            elif event.key == pygame.K_LEFT:
                move_x = -0.3
                move_y = 0

            elif event.key == pygame.K_UP:
                move_x = 0
                move_y = -0.3

            elif event.key == pygame.K_DOWN:
                move_x = 0
                move_y = 0.3

            else:
                move_x = 0
                move_y = 0

    screen.blit(bg,(0,0))
    screen.blit(frogImg,(frogX,frogY))
        
    #screen.fill(red)
    frog = pygame.Rect(frogX,frogY,frogWidth,frogHeight)
    snake = pygame.draw.rect(screen,white,[x,y,w,h])
    x += move_x
    y += move_y

    snakeHead = []
    snakeHead.append(x)
    snakeHead.append(y)
    snakeList.append(snakeHead)
    drawSnake(snakeList)

    if len(snakeList) > snakelength:
        del snakeList[0]

    if x > screenWidth:
        x = -w
    elif x < -50:
        x = screenWidth
    if y > screenHeight:
        y = -h
    elif y < -50:
        y = screenHeight

    if frog.colliderect(snake):
        frogX = random.randint(1,screenWidth-frogWidth)
        frogY = random.randint(1,screenHeight-frogHeight)

        snakelength += 40
    pygame.display.flip()