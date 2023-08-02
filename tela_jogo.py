# Imports e arquivos
from config import largura, altura, fps, QUIT, GAME,Azul, INIT
from math import*
import pygame
from assets import RUA,NEW_GAME,load_assets, JOGADOR , SOM_JOGANDO, SOM_TELA_INICIAL
from classes import Button, Jogador
# Gera a tela
tela = pygame.display.set_mode((largura, altura))
pygame.mixer.init()

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
        #Toca a música
        pygame.mixer.music.set_volume(0.4)
        
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(Azul)

        imagem_fundo_bg = telajogo.get_width()

        screen.blit(assets[RUA], (scroll, 0))

        # Desenha os botões
    
        #Colocando o scrool no fundo

        screen.blit(assets[RUA], (scroll + imagem_fundo_bg, 0))

        scroll -= 5
    
        #Resetando o scroll
        if abs(scroll) > imagem_fundo_bg:
            scroll = 0
        
        screen.blit(jogador.image, (jogador.rect.x, jogador.rect.y))

  
        # Ajusta a velocidade do jogo.
        clock.tick(fps)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT # muda o state para quit
                pygame.mixer.stop()
                running = False # para de rodar
            
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_UP:#verifica a telca apertada 
                    jogador.vy_jogador += 8 #Faz o jogador parar
                    
                if event.key == pygame.K_DOWN:#verifica a tecla apertada 
                    jogador.vy_jogador -= 8 #faz o jogador parar
            
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_UP:#verifica a telca apertada 
                    jogador.vy_jogador -= 8 #Faz o jogador se movimenta para cima
                
                if event.key == pygame.K_DOWN:#verifica a tecla apertada 
                    jogador.vy_jogador += 8 #faz o jogador se movimentar para baixo
                    


        jogador.update()

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        pygame.display.update()
        
    return state