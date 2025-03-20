import pygame

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Цвета
GRAY = (128, 128, 128)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(GRAY)

    # его лицо нарисовываем
    pygame.draw.circle(screen, YELLOW, (300, 200), 100)

    # юудет улыбкой
    pygame.draw.rect(screen, BLACK, (250, 250, 100, 10))

    # левый шлах
    pygame.draw.circle(screen, RED, (260, 165), 20)
    # паравый глаз
    pygame.draw.circle(screen, RED, (340, 165), 15)

    # левая бровь
    pygame.draw.line(screen, BLACK, (210, 120), (285, 155), 10)
    pygame.draw.line(screen, BLACK, (390, 130), (315, 155), 10)

    # левый шлах
    pygame.draw.circle(screen, BLACK, (260, 165), 10)
    # паравый глаз
    pygame.draw.circle(screen, BLACK, (340, 165), 6)

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
