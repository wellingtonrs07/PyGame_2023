# Imports e arquivos
from config import largura, altura, fps, QUIT, GAME,Azul, INIT,OVER, WIN
from math import*
import pygame
from assets import RUA,NEW_GAME,load_assets, JOGADOR,TELA_WIN,SIM,NAO
from classes import Button, Jogador

# Gera a tela
tela = pygame.display.set_mode((largura, altura))

def telawin(screen):
    assets = load_assets()[0]
    btns = load_assets()[1]
    
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    
    #fim
    telajogo = assets[TELA_WIN]
    fundo_rect = telajogo.get_rect()

    # começa a rodar o loop
    running = True
    scroll = 0

    # coloca a posição dos botões
    botaosim = Button((((largura/2)-250)), (altura/4)+440, btns[SIM])
    botaonao = Button(((largura/2)+20),(altura/4)+440, btns[NAO])

    while running:
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(Azul)

        screen.blit(assets[TELA_WIN], (scroll, 0))

        # Desenha os botões
        sim = botaosim.aparecer(screen, btns[SIM])
        nao = botaonao.aparecer(screen, btns[NAO])

        # Ajusta a velocidade do jogo.
        clock.tick(fps)
    
    # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT or nao:
                state = QUIT # muda o state para quit
                running = False # para de rodar

            if sim:
                state = GAME
                running = False

    # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        pygame.display.update()
    return state