# Configurações do jogo
from os import path
import pygame


# Infos Básicas
largura = 1200
altura = 800
fps = 60
WIDTH_CARRO = 100
HEIGHT_CARRO = 50
WIDTH_NPC = 100
HEIGHT_NPC = 50

# States
QUIT = 0
GAME = 1
INIT = 2
END = 3

# Paths para arquivos/pastas
Imagens = path.join(path.dirname(__file__), 'images')

Azul = (0,0,255)