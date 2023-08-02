import pygame
import os
from config import largura, altura, WIDTH_CARRO, HEIGHT_CARRO, WIDTH_NPC,HEIGHT_NPC, Imagens

PAISAGEM = 'paisagem'
CARRO_IMG = 'carro'
RUA = 'rua'
TelaI = 'Tela Inicial'
TelaInstrucao = 'tela instrucao'
NEW_GAME = 'new_game'
INSTRUCOES = 'instrucoes'
RETURN = 'return'
JOGADOR = 'jogador'

def load_assets():
    assets = {}

    assets[TelaI] = pygame.image.load(os.path.join(Imagens, 'menu.png')).convert()
    assets[TelaI] = pygame.transform.scale(assets[TelaI],(largura, altura))

    assets[TelaInstrucao] = pygame.image.load(os.path.join(Imagens, 'tela_instrucoes.png')).convert()
    assets[TelaInstrucao] = pygame.transform.scale(assets[TelaInstrucao],(largura, altura))
    
    assets[RUA] = pygame.image.load(os.path.join(Imagens, 'rua.png')).convert()
    assets[JOGADOR] = pygame.image.load(os.path.join(Imagens, 'carro_imagem.png')).convert()

    assets


    btns = {}

    btns[NEW_GAME] = pygame.image.load(os.path.join(Imagens, 'btn_inicio.png')).convert()
    btns[NEW_GAME] = pygame.transform.scale(btns[NEW_GAME],(200,100))

    btns[RETURN] = pygame.image.load(os.path.join(Imagens, 'btn_return.png')).convert()
    btns[RETURN] = pygame.transform.scale(btns[RETURN], (75, 75))

    btns[INSTRUCOES] = pygame.image.load(os.path.join(Imagens, 'btn_inte.png')).convert()
    btns[INSTRUCOES] = pygame.transform.scale(btns[INSTRUCOES], (75, 75))

    return [assets,btns]
