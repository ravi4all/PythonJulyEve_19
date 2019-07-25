# pip install pygame
import pygame
pygame.init()

height = 500
width = 1000
screen = pygame.display.set_mode((width,height))

white = 255,255,255
# rgb - red,gree,blue
screen.fill(white)

# update screen
pygame.display.flip()