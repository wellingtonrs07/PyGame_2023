# Configurações do jogo
from os import path
import pygame
from math import*


# Infos Básicas
largura = 1300
altura = 700
fps = 60
WIDTH_CARRO = 150
HEIGHT_CARRO = 80
WIDTH_NPC = 100
HEIGHT_NPC = 50

# States
QUIT = 0
GAME = 1
INIT = 2
END = 3
INTR = 4
RET = 5
WIN = 6
OVER = 7

# Paths para arquivos/pastas
Imagens = path.join(path.dirname(__file__), 'images')
Click = path.join(path.dirname(__file__), 'sounds', 'mixkit-fast-double-click-on-mouse-275.wav')

Azul = (0,0,255)