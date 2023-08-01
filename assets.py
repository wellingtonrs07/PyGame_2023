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