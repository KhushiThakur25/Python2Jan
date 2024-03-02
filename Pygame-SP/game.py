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





red = 255,0,0
white = 255,255,255
w,h = 50,50

def homeScreen():
    font = pygame.font.SysFont(None,100)
    text = font.render("Welcome to the jungle",True,white)

    font_2 = pygame.font.SysFont(None,70)
    text_2 = font_2.render("Press SPACE key to start Game..",True,white)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()
            screen.blit(bg,(0,0))
            screen.blit(text,(100,100))
            screen.blit(text_2,(50,300))
            pygame.display.update()

def gameOver():
    font = pygame.font.SysFont(None,200)
    text = font.render("Game Over..",True,white)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit
        screen.blit(text,(100,100))
        pygame.display.update()


def drawSnake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(screen,white,[snakeList[i][0],snakeList[i][1],w,h])

def score(counter):
    font = pygame.font.SysFont(None,30)
    text =  font.render("Score:{}".format(counter),True,white)
    screen.blit(text,(100,10))



def game():
    frogX = random.randint(1,screenWidth-frogWidth)
    frogY = random.randint(1,screenHeight-frogHeight)
    move_x = 0.3
    move_y = 0.3
    speed = 2
    counter = 0
    snakeList = []
    snakelength = 1
    x,y = 0,0
    FPS = 6000
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_x = speed
                    move_y = 0

                elif event.key == pygame.K_LEFT:
                    move_x = -speed
                    move_y = 0

                elif event.key == pygame.K_UP:
                    move_x = 0
                    move_y = -speed

                elif event.key == pygame.K_DOWN:
                    move_x = 0
                    move_y = speed

                else:
                    move_x = 0
                    move_y = 0

        screen.blit(bg,(0,0))
        screen.blit(frogImg,(frogX,frogY))
        score(counter)
            
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
            FPS += 3000
            counter += 1

        for each in snakeList[:-1]:
            if each == snakeList[-1]:
                gameOver()
                
        pygame.display.flip()
        clock.tick(FPS)
homeScreen()