import pygame
import os
from config import largura, altura, WIDTH_CARRO, HEIGHT_CARRO, WIDTH_NPC,HEIGHT_NPC, Imagens

PAISAGEM = 'paisagem'
CARRO_IMG = 'carro'

TelaI = 'Tela Inicial'
NEW_GAME = 'new_game'

def load_assets():
    assets = {}

    assets[TelaI] = pygame.image.load(os.path.join(Imagens, 'fundo_teste.png')).convert()
    assets[TelaI] = pygame.transform.scale(assets[TelaI], (largura, altura))

    btns = {}

    btns[NEW_GAME] = pygame.image.load(os.path.join(Imagens, 'botao_jogar')).convert()
    return [assets,btns]
