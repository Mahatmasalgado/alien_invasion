import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ una clase para representar un solo alien de la flota """
    
    def __init__(self, ai_game):
        """ inicializa el alien y establece su posición inicial """
        super().__init__()
        self.screen = ai_game.screen
        
        #carga la imagen del alien y configura su atributo rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        #inicia un nuevo alien cerca de la parte superior izquierda de la pantalla
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #guarda la posición horizontal exacta del alien
        self.x = float(self.rect.x)
    