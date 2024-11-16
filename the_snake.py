from random import choice, randint
from typing import Optional, Self

import pygame

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 20

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


# Тут опишите все классы игры.
class GameObject:
    """
    Базовый класс игрового объекта, в котором задаются общие для всех объектов
    атрибуты позиции и цвета и методы инициализации и отрисовки.
    """

    def __init__(
        self: Self,
        position: Optional[tuple[int, int]] = None,
        body_color: Optional[tuple[int, int, int]] = None
    ) -> Self:
        """
        Базовый конструктор игрового объекта; инициализация позиции и цвета
        игрового объекта.
        """
        if position:
            self.position = position
        else:
            self.position = (
                GRID_WIDTH // 2 * GRID_SIZE,
                GRID_HEIGHT // 2 * GRID_SIZE
            )

        self.body_color = body_color if body_color else BOARD_BACKGROUND_COLOR

    def draw(self: Self) -> None:
        """
        Абстрактный метод, предназначенный для переопределения в дочерних
        классах. Метод должен определять, как отрисовывается игровой объект.
        """
        pass


class Apple(GameObject):
    """Игровой объект "Яблоко"."""

    def __init__(self: Self) -> Self:
        """
        Инициализирует объект "Яблоко". Устанавливает цвет яблока и
        случайную свободную позицию на игровом поле.
        """
        super().__init__(self.randomize_position(), APPLE_COLOR)

    def randomize_position(self: Self) -> tuple[int, int]:
        """
        Возращает случайную позицию в пикселях, которая является
        свободной для установки в нее яблока.
        """
        pass

    def draw(self: Self) -> None:
        """Отрисовывает яблоко в позиции self.position."""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """
    Игровой объект "Змейка". Представляет из себя список координат,
    соответствующих положению сегментов тела. Атрибуты и методы класса
    обеспечивают логику движения, отрисовку, обработку событий и другие
    аспекты поведения змейки в игре.
    """

    def __init__(self: Self) -> Self:
        """Инициализирует начальное состояние змейки."""
        self.reset()

    def reset(self: Self) -> None:
        """Сбрасывает состояние змейки в начальное в случае проигрыша"""
        self.length = 1
        self.positions = [(
            GRID_WIDTH // 2 * GRID_SIZE,
            GRID_HEIGHT // 2 * GRID_SIZE
        )]
        self.direction = RIGHT
        self.next_direction = None
        self.body_color = SNAKE_COLOR

    def update_direction(self: Self) -> None:
        """Обновляет направление движения змейки"""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self: Self) -> None:
        """
        Обновляет позицию змейки, добавляя новую голову в начало списка
        сегментов и, если яблоко не было съедено, удаляя последний элемент.
        """
        pass

    def draw(self: Self) -> None:
        """Отрисовывает все сегменты змейки"""
        for position in self.positions[:-1]:
            rect = (pygame.Rect(position, (GRID_SIZE, GRID_SIZE)))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        # Отрисовка головы змейки
        head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

        # Затирание последнего сегмента
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def get_head_position(self: Self) -> tuple[int, int]:
        """Возвращает текущие координаты головы змейки"""
        return self.positions[0]


def handle_keys(game_object):
    """Обрабатывает дейтсвия пользователя"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    """Начало программы"""
    # Инициализация PyGame:
    pygame.init()
    # Тут нужно создать экземпляры классов.
    ...

    # while True:
    #     clock.tick(SPEED)

        # Тут опишите основную логику игры.
        # ...


if __name__ == '__main__':
    main()
