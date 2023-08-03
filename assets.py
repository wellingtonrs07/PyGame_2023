import pygame
import os
from config import largura, altura, WIDTH_CARRO, HEIGHT_CARRO, WIDTH_NPC,HEIGHT_NPC, Imagens
pygame.mixer.init()
#Nomeando as keys do dicionário assets
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

LISTA_IMAGEM = 'lista imagem'
OBSTACULO1 = 'lixeira'
OBSTACULO2 = 'saco de lixo'
OBSTACULO3 = 'maciel'
OBSTACULO4 = 'mendigo'
VIDA = 'VIDA'

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
    assets[TELA_OVER] = pygame.transform.scale(assets[TELA_OVER],(largura, altura))

    assets[LISTA_IMAGEM] =  [
        pygame.image.load(os.path.join(Imagens, 'lixo.png')).convert_alpha(), 
        pygame.image.load(os.path.join(Imagens, 'maciel.png')).convert_alpha(),
        pygame.image.load(os.path.join(Imagens, 'mendigao.png')).convert_alpha(),
        pygame.image.load(os.path.join(Imagens, 'saco_lixo.png')).convert_alpha()]

    assets[LISTA_IMAGEM] =  [pygame.transform.scale(assets[LISTA_IMAGEM][0], (100,100)), pygame.transform.scale(assets[LISTA_IMAGEM][1], (100,100)), pygame.transform.scale(assets[LISTA_IMAGEM][2], (100,100)), pygame.transform.scale(assets[LISTA_IMAGEM][3], (100,100))]

    assets[VIDA] = pygame.image.load(os.path.join(Imagens,'coracao.png')).convert_alpha()
    assets[VIDA] = pygame.transform.scale(assets[VIDA],(75, 75))



    btns = {}

    btns[NEW_GAME] = pygame.image.load(os.path.join(Imagens, 'btn_inicio.png')).convert_alpha()
    btns[NEW_GAME] = pygame.transform.scale(btns[NEW_GAME],(300,150))

    btns[RETURN] = pygame.image.load(os.path.join(Imagens, 'btn_return.png')).convert_alpha()
    btns[RETURN] = pygame.transform.scale(btns[RETURN], (75, 75))

    btns[INSTRUCOES] = pygame.image.load(os.path.join(Imagens, 'btn_inte.png')).convert_alpha()
    btns[INSTRUCOES] = pygame.transform.scale(btns[INSTRUCOES], (75, 75))

    return [assets,btns]
