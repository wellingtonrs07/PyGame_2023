# Imports e arquivos
from config import largura, altura, fps, QUIT, GAME,Azul, INIT,OVER, WIN
from math import*
import pygame
from assets import RUA,NEW_GAME,load_assets, JOGADOR,GAME_OVER,WIN
from classes import Button, Jogador

# Gera a tela
tela = pygame.display.set_mode((largura, altura))

def telaover(screen):
    assets, btns = load_assets()
    
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()[0]
    

    telajogo = assets[WIN]
    fundo_rect = telajogo.get_rect()

    # começa a rodar o loop
    running = True
    scroll = 0

    while running:
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(Azul)

        imagem_fundo_bg = telajogo.get_width()

        screen.blit(assets[WIN], (scroll, 0))

        # Ajusta a velocidade do jogo.
        clock.tick(fps)
    
    # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT # muda o state para quit
                running = False # para de rodar

    return state