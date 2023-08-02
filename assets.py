import pygame
import os
from config import largura, altura, WIDTH_CARRO, HEIGHT_CARRO, WIDTH_NPC,HEIGHT_NPC, Imagens, Sons

PAISAGEM = 'paisagem'
CARRO_IMG = 'carro'
RUA = 'rua'
TelaI = 'Tela Inicial'
TelaInstrucao = 'tela instrucao'
NEW_GAME = 'new_game'
INSTRUCOES = 'instrucoes'
RETURN = 'return'
JOGADOR = 'jogador'
TELA_WIN = 'tela win'
TELA_OVER = 'tela over'
OBSTACULO1 = 'lixeira'
OBSTACULO2 = 'saco de lixo'
OBSTACULO3 = 'maciel'
OBSTACULO4 = 'mendigo'


def load_assets():
    assets = {}

    assets[TelaI] = pygame.image.load(os.path.join(Imagens, 'menu.png')).convert()
    assets[TelaI] = pygame.transform.scale(assets[TelaI],(largura, altura))

    assets[TelaInstrucao] = pygame.image.load(os.path.join(Imagens, 'tela_instrucoes.png')).convert()
    assets[TelaInstrucao] = pygame.transform.scale(assets[TelaInstrucao],(largura, altura))
    
    assets[RUA] = pygame.image.load(os.path.join(Imagens, 'rua.png')).convert()

    assets[JOGADOR] = pygame.image.load(os.path.join(Imagens, 'carro_imagem.png')).convert_alpha()
    assets[JOGADOR] = pygame.transform.scale(assets[JOGADOR], (250,120))

    assets[TELA_WIN] =  pygame.image.load(os.path.join(Imagens, 'tela_win.png')).convert_alpha()
    assets[TELA_WIN] = pygame.transform.scale(assets[TELA_WIN],(largura, altura))

    assets[TELA_OVER] =  pygame.image.load(os.path.join(Imagens, 'tela_game_over.png')).convert_alpha()
    assets[TELA_OVER] = pygame.transform.scale(assets[TELA_WIN],(largura, altura))

    assets[OBSTACULO1] = pygame.image.load(os.path.join(Imagens,'lixo.png')).convert_alpha()
    assets[OBSTACULO1] = pygame.transform.scale(assets[OBSTACULO1],(WIDTH_NPC, HEIGHT_NPC))

    assets[OBSTACULO2] = pygame.image.load(os.path.join(Imagens,'saco_lixo.png')).convert_alpha()
    assets[OBSTACULO2] = pygame.transform.scale(assets[OBSTACULO2],(WIDTH_NPC, HEIGHT_NPC))

    assets[OBSTACULO3] = pygame.image.load(os.path.join(Imagens,'maciel.png')).convert_alpha()
    assets[OBSTACULO3] = pygame.transform.scale(assets[OBSTACULO3],(WIDTH_NPC, HEIGHT_NPC))

    assets[OBSTACULO4] = pygame.image.load(os.path.join(Imagens,'mendigao.png')).convert_alpha()
    assets[OBSTACULO4] = pygame.transform.scale(assets[OBSTACULO4],(WIDTH_NPC, HEIGHT_NPC))

    btns = {}

    btns[NEW_GAME] = pygame.image.load(os.path.join(Imagens, 'btn_inicio.png')).convert_alpha()
    btns[NEW_GAME] = pygame.transform.scale(btns[NEW_GAME],(300,150))

    btns[RETURN] = pygame.image.load(os.path.join(Imagens, 'btn_return.png')).convert_alpha()
    btns[RETURN] = pygame.transform.scale(btns[RETURN], (75, 75))

    btns[INSTRUCOES] = pygame.image.load(os.path.join(Imagens, 'btn_inte.png')).convert_alpha()
    btns[INSTRUCOES] = pygame.transform.scale(btns[INSTRUCOES], (75, 75))

    #Load dos sons do jogo
    pygame.mixer.music.load(os.path.join(Sons, 'musica_tela_inicial_e_instrucoes.mp3'))
    pygame.mixer.music.load(os.path.join(Sons, 'trilha_sonora_jogando.mp3'))
    pygame.mixer.music.set_volume(0.4)


    return [assets,btns]
