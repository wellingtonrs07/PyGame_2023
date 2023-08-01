# Imports e arquivos
from config import largura, altura, fps, QUIT, GAME,Azul
import pygame
from assets import TelaI,NEW_GAME,load_assets
from classes import Button

# Gera a tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Velozes e Furiosos')

def telainicial(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()[0]
    btns = load_assets()[1]

    fundo = assets[TelaI]
    fundo_rect = fundo.get_rect()

    # começa a rodar o loop
    running = True


    # coloca a posição dos botões
    botaonew = Button(((largura/2)-225), 470, btns[NEW_GAME])
    
    while running:

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(Azul)
        screen.blit(fundo, fundo_rect)

        # Desenha os botões
        new = botaonew.aparecer(screen, btns[NEW_GAME])

        # Ajusta a velocidade do jogo.
        clock.tick(fps)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT # muda o state para quit
                running = False # para de rodar

            if new:
                state = intro # muda para a intro do jogo (telaintro)
                running = False # para de rodar

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        pygame.display.update()
        
    return state