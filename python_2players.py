# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 14:58:55 2025

@author: Lesya
"""

import pygame
import sys
import random
import time

# Инициализация Pygame
pygame.init()

# Константы
CELL_SIZE = 15
GRID_SIZE = 100  # Размер сетки
SCREEN_SIZE = CELL_SIZE * GRID_SIZE
FPS = 10

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)

# Создание окна
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Змейка на двоих")

# Шрифт для вывода текста
font = pygame.font.SysFont("Arial", 20)

# Функция для отрисовки текста
def draw_text(text, position, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

# Функция для отрисовки кнопки
def draw_button(text, rect, color, text_color):
    pygame.draw.rect(screen, color, rect)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

# Основной класс игры
class SnakeGame:
    def __init__(self):
        self.snakes = {
            "player1": [(GRID_SIZE // 4, GRID_SIZE // 2)],  # Змейка игрока 1
            "player2": [(3 * GRID_SIZE // 4, GRID_SIZE // 2)],  # Змейка игрока 2
        }
        self.directions = {
            "player1": (0, -1),  # Начальное направление игрока 1 (вверх)
            "player2": (0, 1),   # Начальное направление игрока 2 (вниз)
        }
        self.food = []  # Список еды
        self.mongoose = []  # Список мангустов
        self.scores = {
            "player1": 0,
            "player2": 0,
        }
        self.last_food_time = time.time()
        self.last_mongoose_time = time.time()
        self.spawn_food()

    def spawn_food(self):
        while True:
            food_x = random.randint(0, GRID_SIZE - 1)
            food_y = random.randint(0, GRID_SIZE - 1)
            food_value = random.randint(1, 9)
            food = ((food_x, food_y), food_value)
            if food[0] not in self.snakes["player1"] and food[0] not in self.snakes["player2"] and food[0] not in [f[0] for f in self.food]:
                self.food.append(food)
                break

    def spawn_mongoose(self):
        while True:
            mongoose = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
            if mongoose not in self.snakes["player1"] and mongoose not in self.snakes["player2"] and mongoose not in [f[0] for f in self.food] and mongoose not in self.mongoose:
                self.mongoose.append(mongoose)
                break

    def update(self):
        for player, snake in self.snakes.items():
            # Перемещение змейки
            head_x, head_y = snake[0]
            dir_x, dir_y = self.directions[player]
            new_head = (head_x + dir_x, head_y + dir_y)

            # Проверка столкновения с границами или самим собой
            if (new_head[0] < 0 or new_head[1] < 0 or
                new_head[0] >= GRID_SIZE or new_head[1] >= GRID_SIZE or
                new_head in snake or
                new_head in self.snakes["player1"] + self.snakes["player2"]):
                return player

            # Добавляем новую голову
            snake.insert(0, new_head)

            # Проверка на поедание еды
            for food in self.food:
                if new_head == food[0]:
                    self.scores[player] += food[1]
                    self.food.remove(food)
                    for _ in range(food[1]):
                        snake.append(snake[-1])  # Увеличение длины змейки
                    break
            else:
                snake.pop()  # Убираем хвост, если еда не съедена

            # Проверка столкновения с мангустами
            if new_head in self.mongoose:
                return player

        # Добавление еды каждые 2 секунды
        if time.time() - self.last_food_time > 2:
            self.spawn_food()
            self.last_food_time = time.time()

        # Добавление мангуста каждые 5 секунд
        if time.time() - self.last_mongoose_time > 5:
            self.spawn_mongoose()
            self.last_mongoose_time = time.time()

        return None

    def draw(self):
        # Очистка экрана
        screen.fill(BLACK)

        # Отрисовка змей
        for x, y in self.snakes["player1"]:
            pygame.draw.rect(screen, GREEN, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        for x, y in self.snakes["player2"]:
            pygame.draw.rect(screen, BLUE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # Отрисовка еды
        for food in self.food:
            food_x, food_y = food[0]
            food_value = food[1]
            draw_text(str(food_value), (food_x * CELL_SIZE + CELL_SIZE // 4, food_y * CELL_SIZE + CELL_SIZE // 4), WHITE)

        # Отрисовка мангустов
        for mongoose in self.mongoose:
            mongoose_x, mongoose_y = mongoose
            draw_text("&", (mongoose_x * CELL_SIZE + CELL_SIZE // 4, mongoose_y * CELL_SIZE + CELL_SIZE // 4), YELLOW)

        # Отрисовка счета
        draw_text(f"Игрок 1: {self.scores['player1']}", (10, 10), WHITE)
        draw_text(f"Игрок 2: {self.scores['player2']}", (SCREEN_SIZE - 150, 10), WHITE)

    def change_direction(self, player, new_direction):
        # Проверяем, чтобы змейка не могла двигаться в противоположном направлении
        opposite_direction = (-self.directions[player][0], -self.directions[player][1])
        if new_direction != opposite_direction:
            self.directions[player] = new_direction

# Основной игровой цикл
def main():
    clock = pygame.time.Clock()

    while True:
        game = SnakeGame()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    # Управление игроком 1
                    if event.key == pygame.K_UP:
                        game.change_direction("player1", (0, -1))
                    elif event.key == pygame.K_DOWN:
                        game.change_direction("player1", (0, 1))
                    elif event.key == pygame.K_LEFT:
                        game.change_direction("player1", (-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        game.change_direction("player1", (1, 0))

                    # Управление игроком 2
                    elif event.key == pygame.K_w:
                        game.change_direction("player2", (0, -1))
                    elif event.key == pygame.K_s:
                        game.change_direction("player2", (0, 1))
                    elif event.key == pygame.K_a:
                        game.change_direction("player2", (-1, 0))
                    elif event.key == pygame.K_d:
                        game.change_direction("player2", (1, 0))

                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            loser = game.update()
            if loser:
                break  # Игра окончена

            game.draw()
            pygame.display.flip()
            clock.tick(FPS)
        
        winner = "player1" if loser == "player2" else "player2"    
        # Экран конца игры
        while True:
            screen.fill(BLACK)
            draw_text("Игра окончена", (SCREEN_SIZE // 2 - 70, SCREEN_SIZE // 2 - 60), WHITE)
            draw_text(f"Игрок 1: {game.scores['player1']}", (SCREEN_SIZE // 2 - 70, SCREEN_SIZE // 2 - 30), GREEN)
            draw_text(f"Игрок 2: {game.scores['player2']}", (SCREEN_SIZE // 2 - 70, SCREEN_SIZE // 2), BLUE)
            draw_text(f"Победил: {winner}", (SCREEN_SIZE // 2 - 70, SCREEN_SIZE // 2 + 30), RED)

            # Рисование кнопок
            new_game_button = pygame.Rect(SCREEN_SIZE // 2 - 70, SCREEN_SIZE // 2 + 70, 140, 40)
            exit_button = pygame.Rect(SCREEN_SIZE // 2 - 70, SCREEN_SIZE // 2 + 120, 140, 40)

            draw_button("Новая игра", new_game_button, GRAY, WHITE)
            draw_button("Выход", exit_button, GRAY, WHITE)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if new_game_button.collidepoint(event.pos):
                        main()  # Запускаем новую игру
                    elif exit_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

if __name__ == "__main__":
    main()
