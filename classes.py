# Classes

# Importar as bibliotecas e arquivos
import pygame
from config import largura, altura
from assets import JOGADOR, LISTA_IMAGEM
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
        self.rect.centerx = 130
        self.rect.bottom = altura/2
        self.vy_jogador = 0
    
    def update(self):
        # Atualização da posição do barco
        self.rect.y += self.vy_jogador
        
        if self.rect.y > 520:
            self.rect.y = 520

        
        if self.rect.y < 54:
            self.rect.y = 54

#criando classe pros obstaculos
import random
class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = random.randint(54, 520)
        self.speedx = -5
        self.speddy = 0

    def update(self):
        self.rect.x += self.speedx

        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.right < 0:
            self.rect.x = random.randint(1000, 1300)
            self.rect.y = random.randint(54, 520)
            self.speedx = -5
            self.speddy = 0



