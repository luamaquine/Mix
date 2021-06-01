import pygame
import time

pygame.init()


def start_menu():
    menu = True
    menu_x = 600
    menu_y = 600
    window = pygame.display.set_mode((menu_x, menu_y))
    menubg = pygame.image.load('assets/menu/luis.coimbra_menu.png')
    clock = pygame.time.Clock()
    font = pygame.font.Font('assets/PressStart2P.ttf', 10)


    def credits():
        creditswindow = pygame.display.set_mode((720, 480))
        background = pygame.image.load('assets/menu/credits.png')
        creditswindow.blit(background, (0, 0))
        pygame.display.update()
        time.sleep(10)
        start_menu()
        

    while menu:

        window.blit(menubg, (0, 0))
        pygame.display.set_caption('Snake')
        pygame.display.update()
        clock.tick(60)

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                quit()

            # Start button
            if 290 + 130 >= mouse[0] >= 290 and 180 + 50 >= mouse[1] >= 180:
                menubg = pygame.image.load('assets/menu/luis.coimbra_menustart.png')
                window.blit(menubg, (0, 0))
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    run_game = True
                    menu = False
                    return menu

            # Options button
            if 290 + 130 >= mouse[0] >= 290 and 255 + 50 >= mouse[1] >= 255:
                menubg = pygame.image.load('assets/menu/luis.coimbra_menuoptions.png')
                window.blit(menubg, (0, 0))
                pygame.display.update()

            # Credits button
            if 290 + 130 >= mouse[0] >= 290 and 325 + 50 >= mouse[1] >= 325:
                menubg = pygame.image.load('assets/menu/luis.coimbra_menucredits.png')
                window.blit(menubg, (0, 0))
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    credits()
                
            # Quit button
            if 290 + 130 >= mouse[0] >= 290 and 395 + 50 >= mouse[1] >= 395:
                menubg = pygame.image.load('assets/menu/luis.coimbra_menuquit.png')
                window.blit(menubg, (0, 0))
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    quit()

start_menu()    