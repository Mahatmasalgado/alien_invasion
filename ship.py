import pygame
class Ship:
    """ clase para gestionar la nave """
    
    def __init__(self, ai_game):
        """ Inicializa la nave y la posición inicial """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        #carga la imagen de la nave y obtiene su rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        #coloca inicialmente cada nave en el centro de la parte inferior de la pantalla
        self.rect.midbottom = self.screen_rect.midbottom
        
        #guarda un valir decimal para la posición horizontal de la nave
        self.x = float(self.rect.x)
        
        #bandera de movimiento
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """ actualiza la posicion de la nave en función del movimiento y de los bordes """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        self.rect.x = self.x 
        
    
    
    def blitme(self):
        """ dibuja la nave en su ubicación actual """
        self.screen.blit(self.image, self.rect)
        