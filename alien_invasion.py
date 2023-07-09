import sys, pygame
from ship import Ship
from settings import Settings
from bullet import Bullet

class AlienInvasion:
    """ clase general para gestionar los recursos y el comportamiento del juego """
    
    def __init__(self):
        """ Inicializa el juego y crea recursos"""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
    
    def _check_keydown_events(self, event):
        """ respuesta a pulsación del teclado """
        if event.key == pygame.K_RIGHT:
            #se mueve a la derecha
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            #se mueve a la izquierda
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            #se sale del programa
            sys.exit()
    
    def _fire_bullet(self):
        """ crea una bala nueva y la añade al grupo de balas """ 
        if len(self.bullets) < self.settings.bullet_allowed: 
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
          
    def _check_keyup_events(self, event):
        """ responde a liberación del teclado """
        if event.key == pygame.K_RIGHT:
            #deja de moverse a la derecha
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            #deja de moverse a la izquierda
            self.ship.moving_left = False
    
    def _check_events(self):
        #busca eventos del teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                    
    def _check_updagte_screen(self):
        #redibuja la pantalla en cada paso por el bucle
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        #hace visible la última pantalla dibujada
        pygame.display.flip()
    
    def _update_bullets(self):
        self.bullets.update()
        #se deshace de las balas que han desaparecido
        for bullet in self.bullets.copy():
            if(bullet.rect.bottom <=0):
                self.bullets.remove(bullet)
        
    
    def run_game(self):
        """ inicia el bucle principal para el juego """
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._check_updagte_screen()
            

            
if __name__ == '__main__':
    #hace una instancia del juego y lo ejecuta
    ai = AlienInvasion()
    ai.run_game()