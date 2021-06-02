import pygame
import os
from pygame.locals import *
from sys import exit


menu_selecao = 1
WIDTH = 600
HEIGHT = 600
FPS = 30

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
screen_game = pygame.Surface((WIDTH, HEIGHT), 0, 32)
botao_enter = False
BG = pygame.transform.scale(pygame.image.load(os.path.join('assets/Background/background-black.png')), (WIDTH, HEIGHT))

def eventos():

    global menu_selecao, botao_enter
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                menu_selecao += 1
            if event.key == K_UP:
                menu_selecao -= 1
            if event.key == K_RETURN:
                menu_selecao += 10

def selecao():

    global menu_selecao, botao_enter

    if menu_selecao == 1:

        screen_game.fill((0, 0, 0))

        fonte = pygame.font.SysFont ("arial", 20, False, False)
        start_game = fonte.render(">> Start <<", True, (255, 255, 255))
        screen_game.blit(start_game, ((WIDTH/2)-60, (HEIGHT/2)))

        fonte = pygame.font.SysFont("arial", 20, False, False)
        credits_game = fonte.render("  Credits  ", True, (255, 255, 255))
        screen_game.blit(credits_game, ((WIDTH / 2) - 50, (HEIGHT / 2)+22))

        fonte = pygame.font.SysFont("arial", 20, False, False)
        exit_game = fonte.render("    Exit    ", True, (255, 255, 255))
        screen_game.blit(exit_game, ((WIDTH / 2) - 50, (HEIGHT / 2)+44))


    if menu_selecao == 2:

        screen_game.fill((0, 0, 0))

        fonte = pygame.font.SysFont("arial", 20, False, False)
        start_game = fonte.render("     Start     ", True, (255, 255, 255))
        screen_game.blit(start_game, ((WIDTH / 2) - 60, (HEIGHT / 2)))

        fonte = pygame.font.SysFont("arial", 20, False, False)
        credits_game = fonte.render(">>Credits<<", True, (255, 255, 255))
        screen_game.blit(credits_game, ((WIDTH / 2) - 60, (HEIGHT / 2) + 22))

        fonte = pygame.font.SysFont("arial", 20, False, False)
        exit_game = fonte.render("    Exit    ", True, (255, 255, 255))
        screen_game.blit(exit_game, ((WIDTH / 2) - 50, (HEIGHT / 2) + 44))

    if menu_selecao == 3:

        screen_game.fill([0, 0, 0])

        fonte = pygame.font.SysFont("arial", 20, False, False)
        start_game = fonte.render("     Start     ", True, (255, 255, 255))
        screen_game.blit(start_game, ((WIDTH/2)-60, (HEIGHT/2)))

        fonte = pygame.font.SysFont("arial", 20, False, False)
        credits_game = fonte.render("  Credits  ", True, (255, 255, 255))
        screen_game.blit(credits_game, ((WIDTH / 2) - 50, (HEIGHT / 2)+22))

        fonte = pygame.font.SysFont("arial", 20, False, False)
        exit_game = fonte.render(">>Exit<<", True, (255, 255, 255))
        screen_game.blit(exit_game, ((WIDTH / 2) - 50, (HEIGHT / 2)+44))

    if menu_selecao == 4:
        menu_selecao = 3

    if menu_selecao == 0:
        menu_selecao = 1

    if menu_selecao == 12:
        menu_selecao = 200

    if menu_selecao == 200:

        screen_game.fill([0, 0, 0])

        fonte = pygame.font.SysFont("arial", 20, False, False)
        fonte_render = fonte.render("----Luã Maury Maquiné da Silva----", True, (100, 245, 250))
        fonte_render2 = fonte.render("---https://github.com/luamaquine---", True, (247, 142, 67))
        voltar_render = fonte.render(">> Voltar <<", True, (255, 255, 255))
        screen_game.blit(fonte_render, ((WIDTH / 2) - 130, (HEIGHT / 2)))
        screen_game.blit(fonte_render2, ((WIDTH / 2) - 130, (HEIGHT / 2) + 20))
        screen_game.blit(voltar_render, ((WIDTH / 2) - 45, (HEIGHT / 2) + 300))

    if menu_selecao == 201:
        menu_selecao = 200
    if menu_selecao == 199:
        menu_selecao = 200

    if menu_selecao == 210:
        menu_selecao = 2

    if menu_selecao == 13:
        menu_selecao = 500

    if menu_selecao == 500:
        pygame.quit()
        exit()    

while True:
    selecao()
    print(botao_enter)
    print(menu_selecao)
    clock.tick(FPS)
    eventos()
    screen.blit(screen_game, (0, 0))

    pygame.display.update()
    pygame.display.flip()