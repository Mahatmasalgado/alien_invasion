import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ una clase para representar un solo alien de la flota """
    
    def __init__(self, ai_game):
        """ inicializa el alien y establece su posición inicial """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        #carga la imagen del alien y configura su atributo rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        #inicia un nuevo alien cerca de la parte superior izquierda de la pantalla
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #guarda la posición horizontal exacta del alien
        self.x = float(self.rect.x)
        
    def check_edges(self):
        """ devuelve true si el alien está en el borde de la pantalla """
        screen_rect = self.screen.get_rect()
        if ( self.rect.right >= screen_rect.right or self.rect.left <= 0 ):
            return True    
        
    def update(self):
        """ mueve la nave hacia la derecha o izquierda """        
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
    