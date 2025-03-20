import pygame
import math
import random
# Инициализация Pygame
pygame.init()

# Установка размеров окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Установка заголовка окна
pygame.display.set_caption("Горы в Pygame")

# Цвета

UP_sky= (254,213,162)
Up_sky2=(254,213,196)
Mountain1=(252,152,49)
SUN=(252,238,33)
land1=(254,213,148)
Mountain2=(172,67,52)
land2=(179,134,148)

def smooth_corner(start, end, center, steps):
    points = []
    for i in range(steps + 1):
        angle = math.pi / 2 * (i / steps)  # Угол от 0 до 90 градусов
        x = center[0] + math.cos(angle) * (start[0] - center[0]) + math.sin(angle) * (end[0] - center[0])
        y = center[1] + math.cos(angle) * (start[1] - center[1]) + math.sin(angle) * (end[1] - center[1])
        points.append((x, y))
    return points

# Основной цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Заливка экрана белым цветом
    screen.fill(UP_sky)
    pygame.draw.rect(screen, Up_sky2, (0, 145, width, (height // 2)-145))
    pygame.draw.circle(screen, SUN, (360, 145), 40)

    base_points = []
    for i in range(15):
        x = int((i / 14) * width)  # Равномерно распределяем по ширине экрана
        y = random.randint(300, 500)  # Случайная высота вершины
        base_points.append((x, y))

    # Добавляем плавные переходы между некоторыми вершинами
    all_points = []
    for i in range(len(base_points) - 1):
        all_points.append(base_points[i])  # Добавляем текущую вершину

        # Плавный переход между каждой 3-й вершиной
        if i % 3 == 0:
            smooth_points = smooth_corner(
                base_points[i], base_points[i + 1],
                ((base_points[i][0] + base_points[i + 1][0]) // 2,  # Центр для сглаживания
                 (base_points[i][1] + base_points[i + 1][1]) // 2),
                10  # Количество промежуточных точек
            )
            all_points.extend(smooth_points)

    # Добавляем последнюю вершину
    all_points.append(base_points[-1])

    # Рисуем гору
    pygame.draw.polygon(screen, Mountain1, all_points, 0)

    # Рисуем траву (основание горы)
    pygame.draw.polygon(screen, land1, [
        (0, height),
        (0, 500),
        *all_points,
        (width, 500),
        (width, height)
    ], 0)

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()