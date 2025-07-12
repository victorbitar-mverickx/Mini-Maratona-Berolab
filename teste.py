from pygame.locals import *
import pygame
from sys import exit
from random import randint

pygame.init()  

largura = 640 
altura = 480
x = largura // 2 - 50  # Centralizando o retângulo na tela
y = altura  // 2 - 50  # Centralizando o retângulo na tela

tela = pygame.display.set_mode((largura, altura)) #CRiAndo a tela
pygame.display.set_caption("Dinobero")  # Definindo o nome da janela

relogio = pygame.time.Clock()  # Criando um relógio para controlar a taxa de quadros no caso pra fazer a animação 

while True:
    relogio.tick(30)  # Limitando a 30 quadros por segundo
    tela.fill((255, 255, 255))  # Preenchendo a tela com a cor branca
     
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:  # Verificando se uma tecla foi pressionada
            if event.key == K_a:  # Se a tecla 'a' for pressionada
                 x = x - 20  # Move o retângulo para a esquerda
            if event.key == K_d:
                x = x + 20  # Move o retângulo para a direita
            if event.key == K_w:   
                y = y - 20  # Move o retângulo para cima
            if event.key == K_s:
                y = y + 20  # Move o retângulo para baixo       
        
   # if pygame.key.get_pressed()[K_a]:  # Verificando se a tecla 'seta esquerda' está pressionada    

    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 100, 100))  # Desenhando um retângulo vermelho (rect) significa retângulo

    y += 1  # Incrementando a coordenada y para mover o retângulo para baixo
    if y > altura:  # Se o retângulo sair da tela, reinicia a posição y
        y = 0
    

    circle_azul = pygame.draw.circle(tela, (0, 255, 0), (100, 100), 50)  # Desenhando um círculo verde (circle) significa círculo

    if ret_vermelho.colliderect(circle_azul): #colisão entre o retângulo vermelho e o círculo azul
     ret_vermelho.x = 0  # Reinicia a posição do retângulo
     print('Colidiu')







   # pygame.draw.line(tela, (0, 0, 255), (10, 10), (10, 10), 5)  # Desenhando uma linha azul (line) significa linha

    #pygame.draw.polygon(tela, (255, 255, 0), [(50  , 50), (10, 10), (550, 400)])  # Desenhando um polígono amarelo (polygon) significa polígono








     pygame.display.update()  # Atualizando a tela  do joguinho
