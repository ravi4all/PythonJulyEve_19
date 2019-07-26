import pygame
import random
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))

red = 255,0,0
white = 255,255,255
black = 0,0,0

mouse = pygame.image.load("mouse_1.png")
mouseWidth = mouse.get_width()
mouseHeight = mouse.get_height()
mouseX = random.randint(0,width - mouseWidth)
mouseY = random.randint(0,height - mouseHeight)

snakeW, snakeH = 80,80
img = pygame.Surface((snakeW, snakeH))
img.fill(red)
rect = img.get_rect()
rect.center = width/2, height/2
moveX = 0
moveY = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = 1
                moveY = 0
            elif event.key == pygame.K_LEFT:
                moveX = -1
                moveY = 0
            elif event.key == pygame.K_DOWN:
                moveY = 1
                moveX = 0
            elif event.key == pygame.K_UP:
                moveY = -1
                moveX = 0

    screen.fill(white)

    # screen.blit(img,(rect.x, rect.y))
    pygame.draw.rect(screen,red,rect)
    screen.blit(mouse, (mouseX, mouseY))
    mouseRect = pygame.Rect(mouseX, mouseY, mouseWidth, mouseHeight)
    rect.x += moveX
    rect.y += moveY

    if mouseRect.colliderect(rect):
        rect.width += 10
        mouseX = random.randint(0, width - mouseWidth)
        mouseY = random.randint(0, height - mouseHeight)

    if rect.left > width:
        rect.x = -50
    elif rect.right < 0:
        rect.x = width
    elif rect.top > height:
        rect.y = -50
    elif rect.bottom < 0:
        rect.y = height

    pygame.display.update()