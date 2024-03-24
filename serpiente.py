import pygame
import time
import random

pygame.init()

# Dimensiones de la pantalla
width = 800
height = 600

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Tamaño de los bloques de la serpiente
block_size = 10

# Velocidad de la serpiente
speed = 10

# Fuente para el texto
font = pygame.font.SysFont(None, 25)

# Inicializar la pantalla
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# Función para dibujar la serpiente
def snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(game_display, green, [block[0], block[1], block_size, block_size])

# Función principal del juego
def game_loop():
    game_exit = False
    game_over = False

    # Posición inicial de la serpiente
    lead_x = width / 2
    lead_y = height / 2

    lead_x_change = 0
    lead_y_change = 0

    snake_list = []
    snake_length = 1

    # Posición inicial de la comida
    rand_food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
    rand_food_y = round(random.randrange(0, height - block_size) / block_size) * block_size

    while not game_exit:
        while game_over == True:
            game_display.fill(white)
            message('Game Over! Press C to play again or Q to quit', red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= width or lead_x < 0 or lead_y >= height or lead_y < 0:
            game_over = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        game_display.fill(black)

        pygame.draw.rect(game_display, red, [rand_food_x, rand_food_y, block_size, block_size])

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for each_segment in snake_list[:-1]:
            if each_segment == snake_head:
                game_over = True

        snake(block_size, snake_list)

        pygame.display.update()

        if lead_x == rand_food_x and lead_y == rand_food_y:
            rand_food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
            rand_food_y = round(random.randrange(0, height - block_size) / block_size) * block_size
            snake_length += 1

        clock.tick(speed)

    pygame.quit()
    quit()

# Función para mostrar mensajes en la pantalla
def message(msg, color):
    screen_text = font.render(msg, True, color)
    game_display.blit(screen_text, [width / 6, height / 3])

game_loop()
