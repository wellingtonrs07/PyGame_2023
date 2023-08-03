# O JOGO

# Importar bibliotecas e arquivos
import pygame
from config import largura,altura,fps,GAME,QUIT,INIT,INTR,RET,WIN, OVER
from tela_inicial import telainicial
from tela_jogo import telajogo
from tela_instrucoes import telainstrucoes
from assets import load_assets
from tela_win import telawin
from tela_over import telaover


# Inicializa o pygame e o mixer a
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
    elif state == INIT:
        state = telajogo(tela)
    elif state == INTR:
        state = telainstrucoes(tela)
    elif state == OVER:
        state = telaover(tela)
    elif state == WIN:
        state = telawin(tela)
    else:
        state = QUIT

# Desliga o pygame
pygame.quit()
