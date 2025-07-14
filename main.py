from dino_runner.components.game import Game
import pygame
from pygame.locals import *
from sys import exit
import os
import random # Importado para a classe Nuvens

# == DIRETÓRIOS E IMAGENS ==
diretorio_principal = os.path.dirname(__file__)

# Caminho para a pasta de imagens do Dino (onde 'DinoRun' está)
diretorio_imagens_dino = os.path.join(diretorio_principal, 'dino_runner', 'assets', 'Dino') 

# Caminho para a pasta 'Other' (onde 'Cloud.png', 'Track.png' estão)
diretorio_outros_assets = os.path.join(diretorio_principal, 'dino_runner', 'assets', 'Other')

diretorio_sons = os.path.join(diretorio_principal, 'assets', 'sounds')

diretorio_imagens_cactus = os.path.join(diretorio_principal, 'dino_runner', 'assets', 'Cactus')


# == INICIALIZAÇÃO DO PYGAME E DA TELA ==

pygame.init()
pygame.mixer.init()  # add a musiquinha de fundo
# Caminho da música
caminho_musica = os.path.join(diretorio_principal, 'dino_runner', 'intermission_loop_b.mp3') 
diretorio_sons = os.path.join(diretorio_principal, 'dino_runner') # 'sons_score_sound.wav' está direto na pasta 'dino_runner'

som_pontuacao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'sons_score_sound.wav'))
som_pontuacao.set_volume(0.8)  # Ajusta o volume (opcional)

# Carrega e toca a música em loop
pygame.mixer.music.load(caminho_musica)
pygame.mixer.music.set_volume(0.5)  # Volume entre 0.0 e 1.0
pygame.mixer.music.play(-1)  # -1 = toca em loop infinito


largura = 1280  # Largura da tela
altura = 540  # Altura da tela

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Dinobero")

game_over_imagem = pygame.image.load(os.path.join(diretorio_outros_assets, 'GameOver.png')).convert_alpha()

reset_imagem = pygame.image.load(os.path.join(diretorio_outros_assets, 'Reset.png')).convert_alpha()

dino_menu_imagem = pygame.image.load(os.path.join(diretorio_outros_assets, 'Teste.png')).convert_alpha()
GAME_STATE = "MENU" # Definimos que o jogo começa no estado de MENU

SEQUENCIA_OBSTACULOS = [
    'cacto', 'passaro', 'cacto', 'cacto', 'passaro', 
    'cacto', 'passaro', 'cacto', 'cacto', 'passaro',
    'cacto', 'cacto', 'passaro', 'cacto', 'passaro',

]
indice_obstaculo_atual = 0 
SPAWN_OBSTACLE = pygame.USEREVENT + 1 
pygame.time.set_timer(SPAWN_OBSTACLE, 2000) 
velocidade_jogo = 5
ultimo_marco = 0  # Variável para controlar o último marco atingido
recorde = 0

def atualizar_spawn_obstaculos():
    intervalo = max(400, 2000 - (velocidade_jogo * 100))  # Diminui com a velocidade, mínimo 400ms
    pygame.time.set_timer(SPAWN_OBSTACLE, intervalo)



# == CLASSES DINOSSAURO ==


class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.imagens_dinossauro = []
        # CORREÇÃO: Usando a variável correta "diretorio_imagens_dino"
        self.imagens_dinossauro.append(pygame.image.load(os.path.join(diretorio_imagens_dino, 'DinoRun1.png')).convert_alpha())
        self.imagens_dinossauro.append(pygame.image.load(os.path.join(diretorio_imagens_dino, 'DinoRun2.png')).convert_alpha())

        
        self.index_lista = 0
        self.image = self.imagens_dinossauro[int(self.index_lista)]
        self.rect = self.image.get_rect()
    
        self.rect.center = (100, altura - 50) # Posição inicial
        self.rect.inflate_ip(-30, -10)  # Ajusta o tamanho do retângulo para o Dino
        self.pulo = False
        self.velocidade_pulo = 5.25# Velocidade atual do pulo
        self.forca_pulo = 15# Força inicial do pulo, ajuste esse valor!
        self.posicao_chao_y = altura - 50 # Y onde o Dino 'aterra' (o mesmo valor de rect.center[1] inicial)

    

    def update(self):
        if self.index_lista >= len(self.imagens_dinossauro):
            self.index_lista = 0

        self.image = self.imagens_dinossauro[int(self.index_lista)]
        self.index_lista += 0.25
        
        if self.pulo:
            # Se o Dino está pulando, atualiza a posição Y
            self.rect.y -= self.velocidade_pulo
            
            # Atualiza a velocidade do pulo (simulando gravidade)
            self.velocidade_pulo -= 0.5 # A velocidade diminui a cada frame
            
            if self.rect.center[1] >= self.posicao_chao_y: # Verifica se o centro Y passou do chão
                self.rect.center = (100, self.posicao_chao_y) # Retorna o Dino para o chão
                self.pulo = False # Não está mais pulando
                self.velocidade_pulo = 0
        
    def pular(self):
        if not self.pulo:  # Só pula se não estiver pulando
            self.pulo = True
            self.velocidade_pulo = self.forca_pulo  # Reseta a velocidade do pulo para a força inicial

    def transformar_em_fossil(self, nova_imagem):
        self.image = nova_imagem
        self.rect = self.image.get_rect(center=self.rect.center)

    def resetar_imagens(self):
        self.imagens_dinossauro = []
        self.imagens_dinossauro.append(pygame.image.load(os.path.join(diretorio_imagens_dino, 'DinoRun1.png')).convert_alpha())
        self.imagens_dinossauro.append(pygame.image.load(os.path.join(diretorio_imagens_dino, 'DinoRun2.png')).convert_alpha())
        self.index_lista = 0
        self.image = self.imagens_dinossauro[0]
        self.rect = self.image.get_rect(center=self.rect.center)

      

# == Classes bibibibobobo ==
def exibir_mensagem(msg, cor, tamanho):
    fonte = pygame.font.SysFont('Arial', tamanho,True, False)
    mensagem = f'{msg}'
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado
class Nuvens(pygame.sprite.Sprite):
    def __init__(self, largura_tela, altura_tela):
        super().__init__()
        
        # Carrega a imagem da nuvem da pasta 'Other'
        self.image = pygame.image.load(os.path.join(diretorio_outros_assets, 'Cloud.png')).convert_alpha()
        self.rect = self.image.get_rect()
        
        # CORREÇÃO: Posição inicial da nuvem para começar VISÍVEL na tela
        # Ela vai começar em algum lugar na metade direita da tela
        self.rect.x = random.randint(0, largura_tela + 300) 
        self.rect.y = random.randint(50, altura_tela // 3)

    def update(self):
        # Move a nuvem para a esquerda
        self.rect.x -= 2 
        
        # Se a nuvem saiu da tela pela esquerda, reposicione-a na direita
        if self.rect.right < 0:
            self.rect.x = largura + random.randint(50, 300) # Volta para fora da tela
            self.rect.y = random.randint(50, altura // 3)

class Track(pygame.sprite.Sprite):
    def __init__(self, largura_tela, altura_tela, Track_x):
        super().__init__() #Carrega o chão
        self.image_original = pygame.image.load(os.path.join(diretorio_outros_assets, 'Track.png')).convert_alpha()
        self.image = self.image_original
        self.rect = self.image.get_rect()

        self.rect.x = Track_x  # Começa na posição Track_x
        self.rect.y = altura_tela - self.rect.height // 2 - 20 # Posição Y ajustada para o Dino

    def update(self):
        global velocidade_jogo
        self.rect.x -= velocidade_jogo # Use a mesma velocidade das nuvens para manter a consistência
        if self.rect.right < 0:
            self.rect.x += self.image.get_width() * 2 

    def set_image(self, nova_imagem):
        self.image = nova_imagem

    def reset_image(self):
        self.image = self.image_original


class Cactus(pygame.sprite.Sprite):
    def __init__(self, largura_tela, altura_tela):
        super().__init__()
        self.images = []
        self.images.append(pygame.image.load(os.path.join(diretorio_imagens_cactus, 'SmallCactus1.png')).convert_alpha())
        self.images.append(pygame.image.load(os.path.join(diretorio_imagens_cactus, 'SmallCactus2.png')).convert_alpha())
        self.images.append(pygame.image.load(os.path.join(diretorio_imagens_cactus, 'SmallCactus3.png')).convert_alpha())

        # Carregar todas as imagens de cacto grande
        self.images.append(pygame.image.load(os.path.join(diretorio_imagens_cactus, 'LargeCactus1.png')).convert_alpha())
        self.images.append(pygame.image.load(os.path.join(diretorio_imagens_cactus, 'LargeCactus2.png')).convert_alpha())
        self.images.append(pygame.image.load(os.path.join(diretorio_imagens_cactus, 'LargeCactus3.png')).convert_alpha())

        # Escolhe uma imagem de cacto aleatoriamente
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()

        self.rect.x = largura_tela + random.randint(50, 200)  
        self.rect.bottom = altura_tela - 17 
    def update(self):
        global velocidade_jogo
        self.rect.x -= velocidade_jogo # Move o cacto para a esquerda
        
        # Se o cacto sair completamente da tela, remove-o
        if self.rect.right < 0:
         self.kill() # Remove o sprite de todos os grupos


class Bird(pygame.sprite.Sprite):
    def __init__(self, largura_tela, altura_tela):
        super().__init__()
        self.images = []
        self.images.append(pygame.image.load(os.path.join(diretorio_principal, 'dino_runner', 'assets', 'Bird', 'Bird1.png')).convert_alpha()) # Correção do caminho
        self.images.append(pygame.image.load(os.path.join(diretorio_principal, 'dino_runner', 'assets', 'Bird', 'Bird2.png')).convert_alpha()) # Correção do caminho   
        
        self.index_lista = 0
        self.image = self.images[int(self.index_lista)] 
        self.rect = self.image.get_rect()   
        self.rect.x = largura_tela + random.randint(20, 500)
        self.rect.y = random.randint(50, altura_tela // 2)  # Posição Y aleatória para a ave    

    def update(self):
        global velocidade_jogo
        if self.index_lista >= len(self.images):
           self.index_lista = 0

        self.image = self.images[int(self.index_lista)]
        self.index_lista += 0.1
            
        
        self.rect.x -= velocidade_jogo
            
            # Se a ave sair completamente da tela, reposicione-a
        if self.rect.right < 0:
            self.kill()  # Remove a ave de todos os grupos

# == INICIALIZAÇÃO DO JOGO == 

todas_as_sprites = pygame.sprite.Group()
dino = Dino()
todas_as_sprites.add(dino)

obstacles = pygame.sprite.Group()

largura_da_pista = pygame.image.load(os.path.join(diretorio_outros_assets, 'Track.png')).get_width()

for _ in range(12):  # Adiciona 12 nuvens
 nuvem1 = Nuvens(largura, altura)
 todas_as_sprites.add(nuvem1)


pista1 = Track(largura, altura, 0)
pista2 = Track(largura, altura, largura_da_pista)

todas_as_sprites.add(pista1)
todas_as_sprites.add(pista2)

velocidade_jogo = 5  # Começa com velocidade padrão

#outro cenario
fundo_cenario_alternativo = pygame.image.load(os.path.join(diretorio_outros_assets, 'country-platform.png')).convert_alpha()
fundo_x1= 0
fundo_x2 = largura

# Escalar o fundo para o tamanho da tela
fundo_cenario_alternativo = pygame.transform.scale(fundo_cenario_alternativo, (largura, altura))

# Carregar a imagem da pista original 
pista_original_imagem = pygame.image.load(os.path.join(diretorio_outros_assets, 'Track.png')).convert_alpha()

# Carregar a imagem do fossil
novo_dino_imagem = pygame.image.load(os.path.join(diretorio_imagens_dino, 'fossils3.png')).convert_alpha()




velocidade_jogo = 5  # Começa com velocidade padrão




relogio = pygame.time.Clock()
pontos = 0
contador_pontos = 0

# ==APORRA DO WHILE==
# == LOOP PRINCIPAL DO JOGO ==
while True:
    relogio.tick(60) # Mantém a taxa de quadros (FPS) 
    global fundo_x1, fundo_x2

    # == TRATAMENTO DE EVENTOS ==
    for event in pygame.event.get():
        if event.type == QUIT: # Se o usuário clicar para fechar a janela
            pygame.quit()
            exit()
        
        # --- Lógica de Eventos baseada no Estado do Jogo ---
        if GAME_STATE == "MENU":
            if event.type == KEYDOWN: # Se qualquer tecla for pressionada no MENU
                GAME_STATE = "PLAYING" # Muda para o estado de JOGANDO
                should_start_game = True # Variável para reiniciar o jogo
                
                dino.rect.center = (100, altura - 50)
                dino.pulo = False
                dino.velocidade_pulo = 0 # Garante que a velocidade do pulo é zero ao reiniciar
                
                
                obstacles.empty() # Limpa os obstáculos do jogo
                
                indice_obstaculo_atual = 0 # Reseta o índice de obstáculos  
                
                # Reposicionar a pista para que comece do zero
                pista1.rect.x = 0
                pista2.rect.x = largura_da_pista
                atualizar_spawn_obstaculos()

        elif GAME_STATE == "PLAYING": # Se o jogo está no estado de JOGANDO
           if event.type == SPAWN_OBSTACLE: # Evento para spawnar obstáculos
                if indice_obstaculo_atual >= len(SEQUENCIA_OBSTACULOS):
                    indice_obstaculo_atual = 0

                proximo_tipo_obstaculo = SEQUENCIA_OBSTACULOS[indice_obstaculo_atual]

                if proximo_tipo_obstaculo == 'cacto':
                    novo_obstaculo = Cactus(largura, altura)
                elif proximo_tipo_obstaculo == 'passaro':
                    novo_obstaculo = Bird(largura, altura)
                    
                todas_as_sprites.add(novo_obstaculo)
                obstacles.add(novo_obstaculo)
                indice_obstaculo_atual += 1 # Incrementa o índice para o próximo

                contador_pontos += 1
                if contador_pontos >= 10:  # A cada 10 frames
                    pontos += 1
                    contador_pontos = 0

                    texto_pontos = exibir_mensagem(f"Pontos: {pontos}", (0, 0, 0), 30)
                    tela.blit(texto_pontos, (largura - 200, 30))
            # Aumenta a velocidade a cada 100 pontos
                if pontos >= ultimo_marco + 100:
                    velocidade_jogo += 1
                    ultimo_marco = pontos
                    atualizar_spawn_obstaculos()  # Atualiza o intervalo dos oBstaculos
                    som_pontuacao.play()
                    print(f"Velocidade aumentada para: {velocidade_jogo}")
                    

                
                
                if pygame.sprite.spritecollideany(dino, obstacles):
                   GAME_STATE = "GAME_OVER"
                   print("Game Over!")
        
        if event.type == KEYDOWN:
            if GAME_STATE == "PLAYING":  # Se o jogo está em andamento
                if event.key == K_SPACE: # Pressionou ESPAÇO para pular
                   dino.pular()
        
            elif GAME_STATE == "GAME_OVER":
                GAME_STATE = "PLAYING"
                should_start_game = True

                dino.rect.center = (100, altura - 50)
                dino.pulo = False
                dino.velocidade_pulo = 0
                

                pontos = 0
                contador_pontos = 0
                indice_obstaculo_atual = 0
                velocidade_jogo = 5
                ultimo_marco = 0

                obstacles.empty()
                todas_as_sprites.empty()

        
                todas_as_sprites.add(dino)

                for _ in range(12):
                    nuvem = Nuvens(largura, altura)
                    todas_as_sprites.add(nuvem)

                pista1.rect.x = 0
                pista2.rect.x = largura_da_pista
                todas_as_sprites.add(pista1)
                todas_as_sprites.add(pista2)

                pygame.time.set_timer(SPAWN_OBSTACLE, 2000)

           
    # == LÓGICA DE ATUALIZAÇÃO E DESENHO BASEADA NO ESTADO DO JOGO ==
    tela.fill((255, 255, 255)) # Preenche a tela com branco (fundo)

    if GAME_STATE == "MENU":
        
       

        dino_menu_rect = dino_menu_imagem.get_rect(center=(largura // 2, altura // 2 - 50)) # Ajuste Y para mover para cima/baixo
        tela.blit(dino_menu_imagem, dino_menu_rect)

        # Desenha o texto "Pressione Qualquer Tecla para Começar"
        fonte_menu = pygame.font.Font(None, 40) # Fonte padrão, tamanho 40
        texto_menu = fonte_menu.render("Pressione Qualquer Tecla para Começar", True, (0, 0, 0)) # Texto em português, cor preta
        
        texto_rect_menu = texto_menu.get_rect(center=(largura // 2, altura // 2 + 50)) # Posição abaixo da imagem
        tela.blit(texto_menu, texto_rect_menu)

    elif GAME_STATE == "PLAYING":
        contador_pontos += 1
        if contador_pontos >= 10:  # Ajuste aqui para mais lento/rápido
            pontos += 1
            contador_pontos = 0
        for obstaculo in obstacles:
            if isinstance(obstaculo, Cactus) and not hasattr(obstaculo, "pontuado"):
                if obstaculo.rect.right < dino.rect.left:  # Passou do Dino
                    if dino.pulo:  # Dino estava pulando
                        pontos += 50
                        obstaculo.pontuado = True

        
        texto_pontos = exibir_mensagem(f"Pontos: {pontos}", (0, 0, 0), 30)
        tela.blit(texto_pontos, (largura - 200, 30))
        texto_recorde = exibir_mensagem(f"Recorde: {recorde}", (100, 100, 100), 24)
        tela.blit(texto_recorde, (largura - 200, 60))

        if 10 <= pontos < 1300:
            global fundo_x1, fundo_x2
            velocidade_fundo = velocidade_jogo
            fundo_x1 -= velocidade_jogo
            fundo_x2 -= velocidade_jogo
            if fundo_x1 + largura < 0:
                fundo_x1 = fundo_x2 + largura
            if fundo_x2 + largura < 0:
                fundo_x2 = fundo_x1 + largura
            tela.blit(fundo_cenario_alternativo, (fundo_x1, posicao_y_fundo_rolante))
            tela.blit(fundo_cenario_alternativo, (fundo_x2, posicao_y_fundo_rolante))
            
     
        else:
            pista1.set_image(pygame.Surface((1,1),pygame.SRCALPHA))
            pista2.set_image(pygame.Surface((1,1),pygame.SRCALPHA))
            fundo_x1 = 0
            fundo_x2 = largura
            dino.resetar_imagens()  # Reseta o Dino para a imagem original
            pista1.set_image(pista_original_imagem)
            pista2.set_image(pista_original_imagem)

        todas_as_sprites.draw(tela) # Desenha todas as sprites (Dino, Nuvens, Pista, Cactos)
        todas_as_sprites.update() # Atualiza a lógica de movimento e animação de todas as sprites

       
        if pygame.sprite.spritecollideany(dino, obstacles):
            GAME_STATE = "GAME_OVER"
            if pontos > recorde:
                recorde = pontos
                print(f"Novo recorde: {recorde} pontos!")
            print("Game Over!")
        

    elif GAME_STATE == "GAME_OVER":
        game_over_rect = game_over_imagem.get_rect(center=(largura // 2, altura // 2 - 50))
        tela.blit(game_over_imagem, game_over_rect)
        reset_rect = reset_imagem.get_rect(center=(largura // 2, altura // 2 + 50))
        tela.blit(reset_imagem, reset_rect)
    else:
        pontos +=1
        todas_as_sprites.update() # Atualiza a lógica de movimento e animação de todas as sprites
        texto_pontos =exibir_mensagem (pontos,40,(0, 0, 0), tela) # Exibe a pontuação na tela

    pygame.display.flip()
