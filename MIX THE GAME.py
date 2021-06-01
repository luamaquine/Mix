import pygame
import os
import time
import random

# Window size
window_x, window_y = 720, 480
WIN = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('Mix')

"assets:"
background = pygame.image.load('assets/Backgroud/background-black.png')

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock
    def redraw_window():
        WIN.blit(background, (0, 0))

        pygame.display.update()


    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
