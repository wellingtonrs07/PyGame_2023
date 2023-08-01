<<<<<<< HEAD
import pygame
import os
from config import WIDTH, HEIGHT, WIDTH_CARRO, HEIGHT_CARRO, WIDTH_NPC,HEIGHT_NPC

PAISAGEM = 'paisagem'
CARRO_IMG = 'carro'



def load_assets():
    assets = {}
=======
# Imagens, Sons, Fontes, Entre outros

import pygame
import os
from config import largura, altura, Imagens

# Cria as keys do dicionario

TelaI = 'Tela Inicial'

def assets():
    assets = {}

    assets[TelaI] = pygame.image.load(os.path.join(Imagens, 'fundo_teste.png')).convert()

    return [assets]
>>>>>>> 083961e458c2bc20c420ac05914cd67b4ec93f23
