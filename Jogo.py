# O JOGO

# Importar bibliotecas e arquivos
import pygame
from config import largura,altura,fps,GAME,QUIT,INIT,INTR,RET
from tela_inicial import telainicial
from tela_jogo import telajogo
from tela_instrucoes import telainstrucoes


# Inicializa o pygame e o mixer
pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Nitro Dash')

state = GAME

while state != QUIT:
    if state == GAME:
        state = telainicial(tela)
    elif state == INIT:
        state = telajogo(tela)
    elif state == INTR:
        state = telainstrucoes(tela)
    elif state == RET:
        state = telainicial(tela)
    else:
        state = QUIT

# Desliga o pygame
pygame.quit()
