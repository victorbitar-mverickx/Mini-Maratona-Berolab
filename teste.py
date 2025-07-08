from pygame.locals import *
import pygame
from sys import exit

pygame.init()  

largura = 640 
altura = 480

tela = pygame.display.set_mode((largura, altura)) #CRiAndo a tela
pygame.display.set_caption("Dinobero")  # Definindo o nome da janela

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


    pygame.draw.rect(tela, (255, 0, 0), (100, 100, 50, 50))  # Desenhando um retângulo vermelho
    pygame.display.update()  # Atualizando a tela  do joguinho
