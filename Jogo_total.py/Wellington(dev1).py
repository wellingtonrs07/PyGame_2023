#Importação das bibliotecas

import pygame 
import random 
import math

#---Gera tela principal 
pygame.mixer.init()
largura = 1500 # Largura da tela 
comprimento = 500 #Comprimento da tela 

window = pygame.display.set_mode((largura, comprimento))



window.fill((0, 0, 0))  # Preenche com a cor branca
pygame.display.update()