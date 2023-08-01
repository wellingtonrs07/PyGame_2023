import pygame
import os
from config import largura, altura, WIDTH_CARRO, HEIGHT_CARRO, WIDTH_NPC,HEIGHT_NPC, Imagens

PAISAGEM = 'paisagem'
CARRO_IMG = 'carro'
RUA = 'asfalto'
TelaI = 'Tela Inicial'
NEW_GAME = 'new_game'


def load_assets():
    assets = {}

    assets[TelaI] = pygame.image.load(os.path.join(Imagens, 'menu.png')).convert()
    assets[TelaI] = pygame.transform.scale(assets[TelaI],(largura, altura))
    
    assets[RUA] = pygame.image.load(os.path.join(Imagens, 'rua.png')).convert()

    btns = {}

    btns[NEW_GAME] = pygame.image.load(os.path.join(Imagens, 'botao_jogar.png')).convert()
    return [assets,btns]
