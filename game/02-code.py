import pygame
pygame.init()

height = 500
width = 1000
screen = pygame.display.set_mode((width,height))

white = 255,255,255
red = 255,0,0
screen.fill(white)

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.draw.rect(screen,red,[0,0,50,50])

    pygame.display.flip()