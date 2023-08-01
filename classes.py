# Classes

# Importar as bibliotecas e arquivos
import pygame
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


        if self.rect.collidepoint(pos) == False:
            self.image = imagem # Troca a imagem
            

        return apertou
