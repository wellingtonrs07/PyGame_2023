# Imports e arquivos
from config import largura, altura, fps, QUIT, GAME,Azul, INIT,Imagens,Fontes, WIN, OVER
from math import*
import random
import pygame
from assets import RUA,NEW_GAME,load_assets, JOGADOR, LISTA_IMAGEM,TELA_WIN
from classes import Button, Jogador,Obstaculo
from os import path
import time

# Nível
nivel = 0
# Gera a tela
tela = pygame.display.set_mode((largura, altura))
#Inicializa mixer
pygame.mixer.init()

# load e play do som de fundo

pygame.font.init()
font = pygame.font.Font((path.join(Fontes,'pixelart.ttf')),22)
font1 = pygame.font.Font((path.join(Fontes,'pixelart.ttf')),33)


def telajogo(screen):

    #Carregando o som de fundo
    pygame.mixer.music.load('sounds/trilha_sonora_jogando.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()

    assets, btns = load_assets()
    jogador = Jogador(assets)


    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Variável para acompanhar o tempo decorrido
    tempo_inicial = time.time()

    #Variável para contabilizar as vidas:
    vidas = 3

    coracao = pygame.image.load(path.join(Imagens, 'coracao.png')).convert_alpha()
    coracao = pygame.transform.scale(coracao, (70, 50))
    coracaoRect = coracao.get_rect()
    coracaoRect.center = (1200, 30)

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

    # Variável para acompanhar o tempo decorrido
    over = False
    ganhou = False
    assets = load_assets()[0]
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

        scroll -= 8
    
        #Resetando o scroll
        if abs(scroll) > imagem_fundo_bg:
            scroll = 0
        
        screen.blit(jogador.image, (jogador.rect.x, jogador.rect.y))
        screen.blit(coracao,coracaoRect)

  
        # Ajusta a velocidade do jogo.
        clock.tick(fps)
        nivel = 0
        # Calcular o tempo decorrido
        tempo_atual = time.time()
        segundos_decorridos = int(tempo_atual - tempo_inicial)
        if segundos_decorridos >= 30 and segundos_decorridos < 60:
            #Aumento do nível e velocidade do carro
            scroll -= 8
            nivel = 1
        if segundos_decorridos >= 60 and segundos_decorridos < 90:
            scroll -= 10
            nivel = 2
        if segundos_decorridos >= 90:
            ganhou = True
        # Renderizar o contador na tela
        # Renderizar o contador na tela e nivel
        texto_contador = font.render(f"{segundos_decorridos} seg", True, (255, 255, 255))
        screen.blit(texto_contador, (10, 10))
        nivel_tela = font.render(f'Nivel {nivel}',True,(255,255,255))
        screen.blit(nivel_tela,(10,30))


        # Renderizar o contador de vidas
        vidas_contador = font1.render(f'{vidas}',True, (255,255,255))
        screen.blit(vidas_contador, (1230, 15))
        # Verifica se houve colisão entre nave e meteoro
        hits = pygame.sprite.spritecollide(jogador,all_obs, True)


        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT # muda o state para quit
                running = False # para de rodar
            
            if ganhou == True:
                state = WIN
                running = False
            if over == True:
                state = OVER
                running = False
            
            
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

        for obstac in hits: # OBSTACULO  
            img = random.choice(assets[LISTA_IMAGEM])  
            obs = Obstaculo(img)
            all_obs.add(obs)

        
        if len(hits) > 0:
            if vidas != 0:
                vidas -=1
            if vidas > 0 and segundos_decorridos == 90:
                ganhou = True
            if vidas == 0:
                over = True


        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        pygame.display.update()
        
    return state