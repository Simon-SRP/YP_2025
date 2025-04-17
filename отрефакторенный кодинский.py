import pygame
from pygame.draw import *

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
COLORS = {
    'WHITE': (255, 255, 255),
    'GRAY': (150, 150, 150),
    'LIGHT_GRAY': (200, 200, 200),
    'PINK': (255, 200, 200),
    'DARK_PINK': (255, 150, 150),
    'BLACK': (0, 0, 0),
    'EYE_PINK': (255, 220, 220)
}


class Bunny:
    def __init__(self, screen, center_x, center_y):
        self.screen = screen
        self.center_x = center_x
        self.center_y = center_y
        self.scale = 1.0

    def draw(self):
        self._draw_body()
        self._draw_head()
        self._draw_ears()
        self._draw_face()
        self._draw_paws()

    def _draw_body(self):
        """Рисуем тело кролика"""
        width, height = 200 * self.scale, 240 * self.scale
        rect(self.screen, COLORS['GRAY'],
             (self.center_x - width // 2, self.center_y - height // 2, width, height))

        # Розовое брюшко
        belly_width, belly_height = 160 * self.scale, 180 * self.scale
        rect(self.screen, COLORS['PINK'],
             (self.center_x - belly_width // 2, self.center_y - belly_height // 2 + 20 * self.scale,
              belly_width, belly_height))

    def _draw_head(self):
        """Рисуем голову кролика"""
        width, height = 150 * self.scale, 120 * self.scale
        rect(self.screen, COLORS['GRAY'],
             (self.center_x - width // 2, self.center_y - height - 40 * self.scale, width, height))

    def _draw_ears(self):
        """Рисуем уши кролика с внутренней розовой частью"""
        # Внешние уши
        ear_width, ear_height = 40 * self.scale, 130 * self.scale
        left_ear_x = self.center_x - 70 * self.scale
        right_ear_x = self.center_x + 30 * self.scale
        ear_y = self.center_y - 200 * self.scale

        rect(self.screen, COLORS['GRAY'], (left_ear_x, ear_y, ear_width, ear_height))
        rect(self.screen, COLORS['GRAY'], (right_ear_x, ear_y, ear_width, ear_height))

        # Внутренние уши
        inner_width, inner_height = 20 * self.scale, 100 * self.scale
        rect(self.screen, COLORS['DARK_PINK'],
             (left_ear_x + 10 * self.scale, ear_y + 15 * self.scale, inner_width, inner_height))
        rect(self.screen, COLORS['DARK_PINK'],
             (right_ear_x + 10 * self.scale, ear_y + 15 * self.scale, inner_width, inner_height))

    def _draw_face(self):
        """Рисуем мордочку: глаза, нос, усы"""
        # Глаза
        eye_size = 12 * self.scale
        eye_y = self.center_y - 140 * self.scale
        circle(self.screen, COLORS['WHITE'], (self.center_x - 30 * self.scale, eye_y), eye_size)
        circle(self.screen, COLORS['WHITE'], (self.center_x + 30 * self.scale, eye_y), eye_size)

        # Зрачки
        circle(self.screen, COLORS['BLACK'], (self.center_x - 30 * self.scale, eye_y), eye_size // 2)
        circle(self.screen, COLORS['BLACK'], (self.center_x + 30 * self.scale, eye_y), eye_size // 2)

        # Ресницы
        self._draw_eyelashes(self.center_x - 30 * self.scale, eye_y, eye_size, -1)
        self._draw_eyelashes(self.center_x + 30 * self.scale, eye_y, eye_size, 1)

        # Нос
        nose_size = 8 * self.scale
        rect(self.screen, COLORS['PINK'],
             (self.center_x - nose_size // 2, self.center_y - 110 * self.scale, nose_size, nose_size))

        # Усы
        self._draw_whiskers()

    def _draw_eyelashes(self, x, y, size, direction):
        """Рисуем ресницы для глаз"""
        for angle in range(30, 151, 30):
            end_x = x + direction * size * 1.5 * pygame.math.Vector2(1, 0).rotate(-angle * direction).x
            end_y = y + size * 1.5 * pygame.math.Vector2(1, 0).rotate(-angle * direction).y
            line(self.screen, COLORS['BLACK'], (x, y), (end_x, end_y), 1)

    def _draw_whiskers(self):
        """Рисуем усы кролика"""
        base_x = self.center_x
        base_y = self.center_y - 100 * self.scale
        length = 60 * self.scale

        for angle in [-30, 0, 30]:
            for direction in [-1, 1]:
                end_x = base_x + direction * length * pygame.math.Vector2(1, 0).rotate(angle).x
                end_y = base_y + length * pygame.math.Vector2(1, 0).rotate(angle).y
                line(self.screen, COLORS['BLACK'], (base_x, base_y), (end_x, end_y), 1)

    def _draw_paws(self):
        """Рисуем лапки кролика"""
        # Передние лапки
        paw_width, paw_height = 40 * self.scale, 80 * self.scale
        rect(self.screen, COLORS['GRAY'],
             (self.center_x - 120 * self.scale, self.center_y + 140 * self.scale, paw_width, paw_height))
        rect(self.screen, COLORS['GRAY'],
             (self.center_x + 80 * self.scale, self.center_y + 140 * self.scale, paw_width, paw_height))

        # Задние лапки (большие)
        back_paw_width, back_paw_height = 240 * self.scale, 40 * self.scale
        rect(self.screen, COLORS['GRAY'],
             (self.center_x - 120 * self.scale, self.center_y + 100 * self.scale, back_paw_width, back_paw_height))


# Основная программа
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Cute Bunny")
    clock = pygame.time.Clock()

    bunny = Bunny(screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(COLORS['WHITE'])
        bunny.draw()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()