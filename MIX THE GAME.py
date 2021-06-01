import pygame
import os
import time
import random
import sys
from pygame.locals import *

from pygame import event
pygame.font.init()

# Window size
window_x, window_y = 750, 550
WIN = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('Mix')

"assets:"
red = pygame.Color(255, 0, 0)
background = pygame.transform.scale (pygame.image.load(os.path.join('assets/Background/background-black.png')), (window_x, window_y))
cherry = "assets/cherry/cherry0.png"
pineapple = "assets/pineapple/pineapplesprite.png"
orange = "assets/orange/orangesprite.png"
fruitlist = [cherry, pineapple, orange]

def main():
    run = True
    FPS = 60
    level = 1
    score = 0
    main_font = pygame.font.SysFont("comicsans", 50)
    snake_speed = 8
    direction = 'RIGHT'
    change_to = direction

    # fruit position
    fruit_position = [random.randrange(1, (window_x // 20)) * 10,
                    random.randrange(1, (window_y // 20)) * 10]
    fruit_spawn = True

    clock = pygame.time.Clock().tick(60)

    def redraw_window():
        WIN.blit(background, (0, 0))
        # Draw text
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
        score_label = main_font.render(f"Score: {score}", 1, (255,255,255))

        WIN.blit(level_label, (window_x - level_label.get_width() - 10, 10))
        WIN.blit(score_label, (10, 10))

        pygame.display.update()
    

    fruit = random.choice(fruitlist)
    
        # defining snake default position
    snake_position = [100, 50]

    # defining first 4 blocks of snake body
    snake_body = [[100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
                ]
        # game over function
    def game_over():
        # creating font object my_font
        my_font = pygame.font.Font('assets/PressStart2P.ttf', 30)

        # creating a text surface on which text 
        # will be drawn
        game_over_surface = my_font.render(
            '''Score: ''' + str(score) + ' /Restart(space)', True, red)

        # create a rectangular object for the text 
        # surface object
        game_over_rect = game_over_surface.get_rect()

        # setting position of the text
        game_over_rect.midtop = (window_x / 2, window_y / 4)

        # blit wil draw the text on screen
        WIN.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        # after 2 seconds we will quit the program
        time.sleep(2)

        for event in pygame.event.get():
            if event.key == K_SPACE:
                main()
    WIN.blit(background, (0, 0))
    while run:
        redraw_window()

        # handling key events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # Condtions for pressing only one key at a time
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
        
        # Snake's movement
        if direction == 'UP':
            snake_position[1] -= 30
        if direction == 'DOWN':
            snake_position[1] += 30
        if direction == 'LEFT':
            snake_position[0] -= 30
        if direction == 'RIGHT':
            snake_position[0] += 30
        
        # Snake's growing mechanism when eating fruit
        # and score increment
        snake_body.insert(0, list(snake_position))
        if fruit_position[0] - 10 <= snake_position[0] <= fruit_position[0] + 10 \
                and fruit_position[1] - 10 <= snake_position[1] <= fruit_position[1] + 10:
            score += 10
            fruit_spawn = False
            fruit = random.choice(fruitlist)
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x // 20)) * 10,
                            random.randrange(1, (window_y // 20)) * 10]
        fruit_spawn = True

        # Game Over conditions
        if snake_position[0] < 0 or snake_position[0] > window_x - 10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > window_y - 10:
            game_over()

        # Touching the snake body
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()
        # Refresh game screen
        pygame.display.update()

        # Frame Per Second / Refresh Rate
        
        
main()