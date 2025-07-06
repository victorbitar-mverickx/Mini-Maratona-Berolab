import pygame   

class Game: 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Dino Runner")
        self.clock = pygame.time.Clock()
        self.running = True