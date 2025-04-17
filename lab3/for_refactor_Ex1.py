import pygame
from pygame.draw import *

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
PINK = (255, 200, 200)
BLACK = (0, 0, 0)


#тушка
def body(x,y,color): #100 80 GRAY
    rect(screen, color, (width // 2 - x, height // 2 - y, 2*x, 3*y))
#голова
def head(x,y,color): #75 100/90 GRAY
    rect(screen, color, (width // 2 - x, height // 2 - 2*y, 2*x, y+10))
#уши
def ears(x,y,color): # 30 280 GRAY
    rect(screen, color, (width // 2 - 100 + x, height // 2 - y, 40, 130))
    rect(screen, color, (width // 2 + x, height // 2 - y, 40, 130))
#уши внутри#
def in_ears(x,y,color): # 20 270 PINK
    rect(screen, color, (width // 2 - 3*x, height // 2 - y, 20, 100))
    rect(screen, color, (width // 2 + 2*x, height // 2 - y, 20, 100))
#глаза
def eye(x,y,color): # 30 140 BLACK
    rect(screen, color, (width // 2 - x, height // 2 - y, 12, 12))
    rect(screen, color, (width // 2 + x, height // 2 - y, 12, 12))
#нос
def nose(y,color): # 110 PINK
    rect(screen, color, (width // 2, height // 2 - y, 8, 8))
#лапки
def paws(x,y,color): # 40 140GRAY
    rect(screen, color, (width // 2 - 3*x, height // 2 - 30, 240, 40))
    rect(screen, color, (width // 2 - 2*x, height // 2 + y, 40, 80))
    rect(screen, color, (width // 2 + x, height // 2 + y, 40, 80))

def base_draw():
    body(100, 80, GRAY)
    head(75, 90, GRAY) # 75 100/90 GRAY
    ears(30, 280, GRAY)
    in_ears(20, 270, PINK)
    eye(30, 140, BLACK)
    nose(110, PINK)
    paws(40, 140, GRAY)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    base_draw()
    pygame.display.flip()

pygame.quit()