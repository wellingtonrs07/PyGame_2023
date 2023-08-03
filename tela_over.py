# Imports e arquivos
from config import largura, altura, fps, QUIT,Azul
from math import*
import pygame
from assets import load_assets,TELA_OVER

# Gera a tela
tela = pygame.display.set_mode((largura, altura))

def telaover(screen):
    assets = load_assets()
    
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()[0]
    

    # começa a rodar o loop
    running = True
    scroll = 0

    while running:
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(Azul)

        screen.blit(assets[TELA_OVER], (scroll, 0))

        # Ajusta a velocidade do jogo.
        clock.tick(fps)
    
    # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT # muda o state para quit
                running = False # para de rodar
        
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        pygame.display.update()
        
    return state
