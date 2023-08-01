# Imports e arquivos
from config import largura, altura, fps, QUIT, GAME,Azul
import pygame
from assets import RUA,NEW_GAME,load_assets
from classes import Button

# Gera a tela
tela = pygame.display.set_mode((largura, altura))

def telajogo(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()[0]

    telajogo = assets[RUA]
    fundo_rect = telajogo.get_rect()

    # começa a rodar o loop
    running = True

    while running:

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(Azul)
        screen.blit(telajogo, fundo_rect)
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