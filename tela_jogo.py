# Imports e arquivos
from config import largura, altura, fps, QUIT, GAME,Azul, INIT
from math import*
import pygame
from assets import RUA,NEW_GAME,load_assets, JOGADOR, LISTA_IMAGEM
from classes import Button, Jogador, Obstaculo


# Gera a tela
tela = pygame.display.set_mode((largura, altura))

def telajogo(screen):
    assets, btns = load_assets()
    jogador = Jogador(assets)


    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()[0]
    

    telajogo = assets[RUA]

    # começa a rodar o loop
    running = True
    scroll = 0
    all_obs = pygame.sprite.Group()

    groups = {}
    groups['all_obs'] = all_obs
    for obs in assets[LISTA_IMAGEM]:
        obs = Obstaculo(obs)
        all_obs.add(obs)

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
        
        screen.blit(jogador.image, (jogador.rect.x, jogador.rect.y))



        # Ajusta a velocidade do jogo.
        clock.tick(fps)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT # muda o state para quit
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
                    

        all_obs.update()
        jogador.update()

        all_obs.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        pygame.display.update()
        
    return state