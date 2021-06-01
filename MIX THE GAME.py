import pygame
import os
import time
import random
pygame.font.init()

# Window size
window_x, window_y = 750, 550
WIN = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('Mix')

"assets:"
background = pygame.transform.scale (pygame.image.load(os.path.join('assets/Background/background-black.png')), (window_x, window_y))

def main():
    run = True
    FPS = 60
    level = 1
    main_font = pygame.font.SysFont("comicsans", 50)

    # fruit position
    fruit_position = [random.randrange(1, (window_x // 20)) * 10,
                    random.randrange(1, (window_y // 20)) * 10]

    clock = pygame.time.Clock().tick(60)

    def redraw_window():
        WIN.blit(background, (0, 0))
        # Draw text
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

        WIN.blit(level_label, (window_x - level_label.get_width() - 10, 10))

        fruit_position.display(WIN)
        
        pygame.display.update()


    while run:
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
main()