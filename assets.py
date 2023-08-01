import pygame
import os
from config import largura, altura, WIDTH_CARRO, HEIGHT_CARRO, WIDTH_NPC,HEIGHT_NPC, Imagens

PAISAGEM = 'paisagem'
CARRO_IMG = 'carro'
ASFALTO = 'asfalto'
TelaI = 'Tela Inicial'

def load_assets():
    assets = {}

    assets[TelaI] = pygame.image.load(os.path.join(Imagens, 'tela_inicial.png')).convert()
    assets[TelaI] = pygame.transform.scale(assets[TelaI],(largura, altura))
    assets[ASFALTO] = pygame.image.load(os.path.join(Imagens, 'asphalt-texture.png')).convert()

    return [assets]
