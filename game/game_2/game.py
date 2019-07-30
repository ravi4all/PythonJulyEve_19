import pygame
pygame.init()

height = 500
width = 1000
screen = pygame.display.set_mode((width,height))

white = 255,255,255
red = 255,0,0
black = 0,0,0
blue = 0,0,255

bg_music = pygame.mixer.Sound("music_1.wav")
bg_music.play(-1)

bg_img = pygame.image.load("img_1.jpg")

def homeScreen():
    font = pygame.font.Font('font_1.ttf', 100)
    text = font.render("Break the Walls", True, red)
    font_2 = pygame.font.Font('font_1.ttf', 70)
    text_2 = font_2.render("Press SPACE to Start Game", True, red)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play()

        screen.blit(bg_img,(0,0))
        screen.blit(text, (200, 100))
        screen.blit(text_2, (100, 250))
        pygame.display.flip()

def score(c):
    font = pygame.font.SysFont(None,30)
    text = font.render("Score : {}".format(c), True, red)
    screen.blit(text, (5,5))

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
    moveBall = False
    ballOnBar = True
    ballMoveX = 0
    ballMoveY = 0
    for i in range(1,5):
        for j in range(10):
            brick = pygame.Rect(j * (brickWidth + 5),i * (brickHeight + 5), brickWidth, brickHeight)
            brickList.append(brick)

    count = 0
    FPS = 300
    clock = pygame.time.Clock()
    while True:
        if ballOnBar:
            ballX = barx + barWidth // 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moveX = 3
                elif event.key == pygame.K_LEFT:
                    moveX = -3
                elif event.key == pygame.K_SPACE:
                    if ballOnBar:
                        moveBall = True
                        ballOnBar = False
            elif event.type == pygame.KEYUP:
                moveX = 0

        # screen.fill(white)
        screen.blit(bg_img, (0, 0))

        barRect = pygame.draw.rect(screen,red,[barx,bary,barWidth,barHeight])
        pygame.draw.circle(screen,blue,(ballX,ballY),ballRadius)
        ballRect = pygame.Rect(ballX,ballY,ballRadius,ballRadius)

        for i in range(len(brickList)):
            pygame.draw.rect(screen,black,brickList[i])

        barx += moveX
        ballX += ballMoveX
        ballY += ballMoveY

        for i in range(len(brickList)):
            if brickList[i].colliderect(ballRect):
                del brickList[i]
                ballMoveY = 3
                count += 1
                FPS += 20
                break

        score(count)

        if moveBall:
            ballMoveX = -3
            ballMoveY = -3
            moveBall = False

        if barx > width - 50:
            moveX = -3
        elif barx < 0:
            moveX = 3

        if ballX > width - ballRadius:
            ballMoveX = -3
        elif ballX < ballRadius:
            ballMoveX = 3
        elif ballY < ballRadius:
            ballMoveY = 3
        elif barRect.colliderect(ballRect):
            ballMoveY = -3
        elif ballY > height*2:
            # print("Game Over")
            # play()
            ballOnBar = True
            ballMoveY = 0
            ballMoveX = 0
            ballY = bary - 10

        pygame.display.flip()
        clock.tick(FPS)
# play()
homeScreen()