# Imports e arquivos
from config import largura, altura, fps, QUIT, GAME,Azul, INIT
from math import*
import pygame
from assets import RUA,NEW_GAME,load_assets, JOGADOR
from classes import Button, Jogador


# Gera a tela
tela = pygame.display.set_mode((largura, altura))

def telajogo(screen):
    assets, btns = load_assets()
    jogador = Jogador(assets)

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()[0]
    

    telajogo = assets[RUA]
    fundo_rect = telajogo.get_rect()

    # começa a rodar o loop
    running = True
    scroll = 0

    while running:
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(Azul)

        imagem_fundo_bg = telajogo.get_width()

        screen.blit(assets[RUA], (scroll, 0))
    
        #Colocando o scrool no fundo

        screen.blit(assets[RUA], (scroll + imagem_fundo_bg, 0))

        scroll -= 5
    
        #Resetando o scroll
        if abs(scroll) > imagem_fundo_bg:
            scroll = 0
        
        screen.blit(jogador.image, (0,350))

  
        # Ajusta a velocidade do jogo.
        clock.tick(fps)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT # muda o state para quit
                running = False # para de rodar
            
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_UP:#verifica a telca apertada 
                    jogador.vy_jogador -= 8#Faz o jogador se movimenta para a esquerda 
                if event.key == pygame.K_DOWN:#verifica a tecla apertada 
                    jogador.vy_jogador += 8#faz o jogador se movimentar para a direita 

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        pygame.display.update()
        
    return state