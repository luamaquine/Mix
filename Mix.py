import pygame
import time
import random
import menu
from pygame.locals import *


def main():
    snake_speed = 8

    # Window size
    window_x = 720
    window_y = 480

    # defining colors
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(16, 56, 6)  # phtaloh green
    blue = pygame.Color(0, 0, 255)

    # Initializing pygame
    pygame.init()

    run_game = True

    # Main Function
    while menu.start_menu():
        menu.start_menu()

    # Initialize game window
    pygame.display.set_caption('Snake')
    game_window = pygame.display.set_mode((window_x, window_y))

    # FPS (frames per second) controller
    fps = pygame.time.Clock()

    # defining snake default position
    snake_position = [100, 50]

    # defining first 4 blocks of snake body
    snake_body = [[100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
                ]
    # fruit position
    fruit_position = [random.randrange(1, (window_x // 20)) * 10,
                    random.randrange(1, (window_y // 20)) * 10]

    fruit_spawn = True

    # setting default snake direction towards
    # right
    direction = 'RIGHT'
    change_to = direction

    # initial score
    score = 0

    background = pygame.image.load('assets/menu/snake.png')


    # displaying Score function
    def show_score(choice, color, font, size):
        # creating font object score_font
        score_font = pygame.font.Font('assets/PressStart2P.ttf', 20)

        # create the display surface object 
        # score_surface
        score_surface = score_font.render('Score : ' + str(score), True, white)

        # create a rectangular object for the text
        # surface object
        score_rect = score_surface.get_rect()

        # displaying text
        game_window.blit(score_surface, score_rect)


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
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()

        # after 2 seconds we will quit the program
        time.sleep(2)

        for event in pygame.event.get():
            if event.key == K_SPACE:
                main()


    cherry = "assets/cherry/cherry0.png"
    pineapple = "assets/pineapple/pineapplesprite.png"
    orange = "assets/orange/orangesprite.png"
    fruitlist = [cherry, pineapple, orange]

    fruit = random.choice(fruitlist)

    while run_game:

        game_window.blit(background, (0, 0))
        # handling key events
        for event in pygame.event.get():
            if event.type == QUIT:
                run_game = False
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

        i = 0

        for pos in snake_body:

            if i != 0:
                game_window.blit(pygame.image.load("assets/snake/snakebody.png"), [pos[0], pos[1]])
            else:
                if direction == 'UP':
                    game_window.blit(pygame.image.load("assets/snake/snakespriteup.png"), [pos[0], pos[1]])
                if direction == 'DOWN':
                    game_window.blit(pygame.image.load("assets/snake/snakespritedown.png"), [pos[0], pos[1]])
                if direction == 'LEFT':
                    game_window.blit(pygame.image.load("assets/snake/snakespriteleft.png"), [pos[0], pos[1]])
                if direction == 'RIGHT':
                    game_window.blit(pygame.image.load("assets/snake/snakespriteright.png"), [pos[0], pos[1]])

            i += 1

        game_window.blit(pygame.image.load(fruit), [fruit_position[0], fruit_position[1]])

        # Game Over conditions
        if snake_position[0] < 0 or snake_position[0] > window_x - 10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > window_y - 10:
            game_over()

        # Touching the snake body
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()

        # displaying score continuously
        show_score(1, white, 'times new roman', 20)

        # Refresh game screen
        pygame.display.update()

        # Frame Per Second / Refresh Rate
        fps.tick(snake_speed)
main()