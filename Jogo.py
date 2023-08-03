# O JOGO

# Importar bibliotecas e arquivos
import pygame
from config import largura,altura,fps,GAME,QUIT,INIT,INTR,RET
from tela_inicial import telainicial
from tela_jogo import telajogo
from tela_instrucoes import telainstrucoes
from assets import load_assets, tela_inicial_som, tela_jogo_som


# Inicializa o pygame e o mixer
pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Nitro Dash')

state = GAME

assets = load_assets()[0]

while state != QUIT:
    if state == GAME:
        state = telainicial(tela)
        # load e play do som de fundo
        tela_inicial_som.play()
    elif state == INIT:
        state = telajogo(tela)
        # load e play do som de fundo
        tela_inicial_som.stop()
        tela_jogo_som.play()
        pygame.mixer.music.play(-1)
    elif state == INTR:
        state = telainstrucoes(tela)
        tela_inicial_som.play()
    elif state == RET:
        state = telainicial(tela)
    else:
        state = QUIT

# Desliga o pygame
pygame.quit()
