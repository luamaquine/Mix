import pygame
import random
from pygame.locals import *
from pygame.time import delay
import Mix

# Helper functions
def on_grid_random():
    x = random.randint(0,59)
    y = random.randint(0,59)
    return (x * 10, y * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

# Macro definition for snake movement.
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()

while Mix.start_menu:
    Mix.start_menu()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('MIX')

# Ball

ball = [(400, 500)]
ballpos = pygame.Surface((10, 10))
ballpos.fill((255, 255, 255))

ball2 = [(250, 100)]
ballpos2 = pygame.Surface((10, 10))
ballpos2.fill((255, 255, 255))

ball3 = [(300, 100)]
ballpos3 = pygame.Surface((10, 10))
ballpos3.fill((255, 255, 255))

ball4 = [(100, 200)]
ballpos4 = pygame.Surface((10, 10))
ballpos4.fill((255, 255, 255))

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((34, 139, 34)) #White

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255, 0, 0))

grape_pos = on_grid_random()
grape = pygame.Surface((10,10))
grape.fill((128, 0, 128))

banana_pos = on_grid_random()
banana = pygame.Surface((10,10))
banana.fill((255, 255, 0))

cherry_pos = on_grid_random()
cherry = pygame.Surface((10,10))
cherry.fill((139, 0, 0))

orange_pos = on_grid_random()
orange = pygame.Surface((10,10))
orange.fill((255, 215, 0))

mine_pos = on_grid_random()
mine = pygame.Surface((10,10))
mine.fill((192, 192, 192))

mine1_pos = on_grid_random()
mine1 = pygame.Surface((10,10))
mine1.fill((192, 192, 192))

mine2_pos = on_grid_random()
mine2 = pygame.Surface((10,10))
mine2.fill((192, 192, 192))

mine3_pos = on_grid_random()
mine3 = pygame.Surface((10,10))
mine3.fill((192, 192, 192))

my_direction = LEFT

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0
font = pygame.font.Font('freesansbold.ttf', 18)
level = 1

game_over = False
while not game_over:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        score = score + 1

    if collision(snake[0], grape_pos):
        grape_pos = on_grid_random()
        snake.append((0,0))
        score = score + 1 

    if collision(snake[0], banana_pos):
        banana_pos = on_grid_random()
        snake.append((0,0))
        score = score + 1

    if collision(snake[0], cherry_pos):
        cherry_pos = on_grid_random()
        snake.append((0,0))
        score = score + 1

    if collision(snake[0], orange_pos):
        orange_pos = on_grid_random()
        snake.append((0,0))
        score = score + 1

    if collision(snake[0], mine_pos):
        mine_pos = on_grid_random()
        game_over = True
        break

    if collision(snake[0], mine1_pos):
        mine1_pos = on_grid_random()
        game_over = True
        break

    if collision(snake[0], mine2_pos):
        min2_pos = on_grid_random()
        game_over = True
        break

    if collision(snake[0], mine3_pos):
        min3_pos = on_grid_random()
        game_over = True
        break
    

        
    # Check if snake collided with boundaries
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break
    
    # Check if the snake has hit itself
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    if game_over:
        break
    
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
        
    # Actually make the snake move.
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    

    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    screen.blit(grape, grape_pos)
    screen.blit(banana, banana_pos)
    screen.blit(cherry, cherry_pos)
    screen.blit(orange, orange_pos)
    screen.blit(mine, mine_pos)
    screen.blit(mine1, mine1_pos)
    screen.blit(mine2, mine2_pos)
    screen.blit(mine3, mine3_pos)

    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)

    level_font = font.render('Level: %s' % (level), True, (255, 255, 255))
    level_rect = level_font.get_rect()
    level_rect.topright = (120, 10)
    screen.blit(level_font, level_rect)
    
    for pos in snake:
        screen.blit(snake_skin, pos)
    for pos in ball:
        screen.blit(ballpos, pos)    
    if score > 4:
        level = 2
        for pos in ball2:
            screen.blit(ballpos2, pos)
    if score > 9:
        level = 3
        for pos in ball3:
            screen.blit(ballpos3, pos)
    if score >19:
        level = 4
        for pos in ball4:
            screen.blit(ballpos4, pos)

    # ball movement
    ball[0] = (ball[0][0] + 10, ball[0][1] - 10)

    # Ball collision with walls
    if ball[0][0] == 590:
        ball[0] = (ball[0][1] - 10, ball[0][0] - 10)  

    # Ball 2
    ball2[0] = (ball2[0][0] + 10, ball2[0][1] - 10)

    # Ball 2 collision with walls
    if ball2[0][0] == 590:
        ball2[0] = (ball2[0][1] - 10, ball2[0][0] - 10) 

    # Ball 3
    ball3[0] = (ball3[0][1] + 10, ball3[0][0] - 10)

    # Ball 3 collision with walls
    if ball3[0][0] == 590:
        ball3[0] = (ball3[0][1] - 10, ball3[0][0] + 10)

    # ball 4 movement
    ball4[0] = (ball4[0][0] + 10, ball4[0][1] - 10)

    # Ball 4 collision with walls
    if ball4[0][0] == 590:
        ball4[0] = (ball4[0][1] - 10, ball4[0][0] + 10)  

    # Ball collision with snake
    for i in range(len(snake)):
        if ball[0][0] == snake[i][0] and ball[0][1] == snake[i][1]:
            game_over = True
            break
    
    for i in range(len(snake)):
        if ball2[0][0] == snake[i][0] and ball2[0][1] == snake[i][1]:
            game_over = True
            break

    for i in range(len(snake)):
        if ball3[0][0] == snake[i][0] and ball3[0][1] == snake[i][1]:
            game_over = True
            break

    for i in range(len(snake)):
        if ball4[0][0] == snake[i][0] and ball4[0][1] == snake[i][1]:
            game_over = True
            break


    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 200)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()