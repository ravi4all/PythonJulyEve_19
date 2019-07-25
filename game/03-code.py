import pygame
pygame.init()

height = 500
width = 1000
screen = pygame.display.set_mode((width,height))

white = 255,255,255
red = 255,0,0

x = 0
y = 0
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(white)
    pygame.draw.rect(screen,red,[x,y,50,50])
    x = x + 1
    y += 1

    pygame.display.flip()