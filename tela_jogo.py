# Imports e arquivos
from config import largura, altura, fps, QUIT, GAME,Azul
import pygame
from assets import ASFALTO,NEW_GAME,load_assets
from classes import Button

# Gera a tela
tela = pygame.display.set_mode((largura, altura))

def telajogo(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()[0]
    btns = load_assets()[1]

    telajogo = assets[as]
    fundo_rect = telajogo.get_rect()

    # começa a rodar o loop
    running = True