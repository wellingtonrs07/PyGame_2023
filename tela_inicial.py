# Imports e arquivos
from config import largura, altura, fps, quit, iniciando
import pygame
from assets import TelaI,assets

# Gera a tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Velozes e Furiosos')
assets = assets()[0]

def telainicial(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    running = True
    
    fundo = assets[TelaI]
    fundo_rect = fundo.get_rect()
    while running:
        screen.fill(0,0,0)
        screen.blit(fundo, fundo_rect)

        # Ajusta a velocidade do jogo.
        clock.tick(fps)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = quit # muda o state para quit
                running = False # para de rodar

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        pygame.display.update()
        
    return state