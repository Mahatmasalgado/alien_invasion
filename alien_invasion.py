import sys, pygame
from settings import Settings
class AlienInvasion:
    """ clase general para gestionar los recursos y el comportamiento del juego """
    
    def __init__(self):
        """ Inicializa el juego y crea recursos"""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """ inicia el bucle principal para el juego """
        while True:
            #busca eventos del teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #redibuja la pantalla en cada paso por el bucle
            self.screen.fill(self.settings.bg_color)
            
            #hace visible la última pantalla dibujada
            pygame.display.flip()
            
if __name__ == '__main__':
    #hace una instancia del juego y lo ejecuta
    ai = AlienInvasion()
    ai.run_game()