import sys, pygame
from ship import Ship
from settings import Settings

class AlienInvasion:
    """ clase general para gestionar los recursos y el comportamiento del juego """
    
    def __init__(self):
        """ Inicializa el juego y crea recursos"""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
    
    def _check_events(self):
        #busca eventos del teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        #se mueve a la derecha
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        #se mueve a la izquierda
                        self.ship.moving_left = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        #deja de moverse a la derecha
                        self.ship.moving_right = False
                    if event.key == pygame.K_LEFT:
                        #deja de moverse a la izquierda
                        self.ship.moving_left = False
                        

    def _check_updagte_screen(self):
        #redibuja la pantalla en cada paso por el bucle
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        #hace visible la última pantalla dibujada
        pygame.display.flip()
    
    def run_game(self):
        """ inicia el bucle principal para el juego """
        while True:
            self._check_events()
            self.ship.update()
            self._check_updagte_screen()
            

            
if __name__ == '__main__':
    #hace una instancia del juego y lo ejecuta
    ai = AlienInvasion()
    ai.run_game()