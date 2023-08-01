import pygame
import os
from config import WIDTH, HEIGHT, WIDTH_CARRO, HEIGHT_CARRO, WIDTH_NPC,HEIGHT_NPC, Imagens

PAISAGEM = 'paisagem'
CARRO_IMG = 'carro'
TelaI = 'Tela Inicial'

def load_assets():
    assets = {}

    assets[TelaI] = pygame.image.load(os.path.join(Imagens, 'fundo_teste.png')).convert()
    return [assets]
