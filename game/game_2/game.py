import pygame
pygame.init()

height = 500
width = 1000
screen = pygame.display.set_mode((width,height))

white = 255,255,255
red = 255,0,0
black = 0,0,0
blue = 0,0,255

def play():
    barHeight = 20
    barWidth = 160
    barx = width//2 - barWidth//2
    bary = height - barHeight - 10
    moveX = 0

    ballRadius = 8
    ballY = bary - 10

    brickWidth = 100
    brickHeight = 30

    brickList = []
    for i in range(4):
        for j in range(10):
            brick = pygame.Rect(j * (brickWidth + 5),i * (brickHeight + 5), brickWidth, brickHeight)
            brickList.append(brick)

    while True:
        ballX = barx + barWidth // 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moveX = 1
                elif event.key == pygame.K_LEFT:
                    moveX = -1
            elif event.type == pygame.KEYUP:
                moveX = 0

        screen.fill(white)

        pygame.draw.rect(screen,red,[barx,bary,barWidth,barHeight])
        pygame.draw.circle(screen,blue,(ballX,ballY),ballRadius)

        for i in range(len(brickList)):
            pygame.draw.rect(screen,black,brickList[i])

        barx += moveX

        if barx > width - 50:
            moveX = -1
        elif barx < 0:
            moveX = 1

        pygame.display.flip()
play()