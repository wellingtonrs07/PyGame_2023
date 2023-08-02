# Classes

# Importar as bibliotecas e arquivos
import pygame
from config import largura, altura
from assets import JOGADOR
# Cria classe dos botoes
class Button():
    
    # Cria os botões
    def __init__(self, x, y, imagem):
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    
    # Cria função aparecer
    def aparecer(self, screen, imagem):

        apertou = False # Não apertou o botão

        pos = pygame.mouse.get_pos() # Pega posição do mouse


        if self.rect.collidepoint(pos):
            self.image = imagem # Troca imagem

            if pygame.mouse.get_pressed()[0] == True:
                apertou = True # Apertou o botão

        screen.blit(self.image, self.rect) #Coloca o botão na tela
            
        return apertou
    
#criando classe pro jogador
class Jogador(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self) 
        self.image = assets[JOGADOR]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = largura/2
        self.rect.bottom = altura - 10
        self.vy_jogador = 0
    
    def update(self):
        # Atualização da posição do barco
        self.rect.y+= self.vy_jogador

        # Mantem dentro da tela
        if self.rect.y > 350:
            self.rect.y = 350

        if self.rect.x > 700:
            self.rect.x = 700


