# Imports e arquivos
from config import largura, altura, fps, QUIT,Azul,GAME
from math import*
import pygame
from assets import load_assets,TELA_OVER,SIM,NAO
from classes import Button

# Gera a tela
tela = pygame.display.set_mode((largura, altura))

def telaover(screen):
    assets = load_assets()
    
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets,btns = load_assets()[0]
    

    # começa a rodar o loop
    running = True
    scroll = 0

    # coloca a posição dos botões
    botaosim = Button((((largura/2)-150)), (altura/4), btns[SIM])
    botaonao = Button(((largura/2)+150),(altura/4), btns[NAO])

    while running:
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(Azul)

        screen.blit(assets[TELA_OVER], (scroll, 0))

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
