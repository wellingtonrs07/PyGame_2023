# Imports e arquivos
from config import largura, altura, fps, QUIT, GAME,Azul
import pygame
from assets import TelaInstrucao, RETURN, load_assets
from classes import Button

# Gera a tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Nitro Dash')

def telainstrucoes(screen):
    
    #Carregando o som de fundo
    pygame.mixer.music.load('sounds/musica_tela_inicial_e_instrucoes.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets, btns = load_assets()

    tela_instrucoes = assets[TelaInstrucao]
    instrucoes_rect = tela_instrucoes.get_rect()

    # começa a rodar o loop
    running = True

    # coloca a posição dos botões
    botaoreturn = Button(1225, 0, btns[RETURN])
    
    while running:

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(Azul)
        screen.blit(tela_instrucoes, instrucoes_rect)

        # Desenha os botões
        ret = botaoreturn.aparecer(screen, btns[RETURN])

        # Ajusta a velocidade do jogo.
        clock.tick(fps)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT # muda o state para quit
                running = False # para de rodar

            if ret:
                state = GAME # muda para a intro do jogo (telaintro)
                running = False # para de rodar

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        pygame.display.update()
        
    return state

    

    