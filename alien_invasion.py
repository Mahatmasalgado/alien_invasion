import sys, pygame
from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """ clase general para gestionar los recursos y el comportamiento del juego """
    
    def __init__(self):
        """ Inicializa el juego y crea recursos"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
    
        self._create_fleet()
        
    def _check_fleet_edges(self):
        """ si algún alien llega al borde """
        for alien in self.aliens.sprites():
            if(alien.check_edges()):
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """ baja la flota y cambia dirección """
        for alien in self.aliens.sprites():
            alien.y += self.settings.fleet_drop_speed
            alien.rect.y = alien.y
            
        self.settings.fleet_direction *= -1
        
        
    def _create_alien(self, alien_number, row_number):
        #crea un alien y lo coloca en la fila
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            alien.x = alien_width + (2 * alien_width * alien_number)
            alien.rect.x = alien.x
            alien.y = alien_height + (2 * alien_height * row_number)
            alien.rect.y = alien.y
            self.aliens.add(alien)
        
    def _create_fleet(self):
        """ crea la flota de aliens """
        #hace un alien y halla el número de aliens en una fila , el espacio entre aliens es igual a la anchura de un alien 
        alien = Alien(self)
        
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        #determina el número de filas de aliens que caben en la pantalla
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        #creamos la flota completa
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
    
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
        self.aliens.draw(self.screen)
        #hace visible la última pantalla dibujada
        pygame.display.flip()
    
    def _update_bullets(self):
        self.bullets.update()
        #se deshace de las balas que han desaparecido
        for bullet in self.bullets.copy():
            if(bullet.rect.bottom <=0):
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """ responde a las colisiones bala-alien"""
        #busca balas que han colisionado
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
        if not self.aliens:
            #destruye las balas existentes y crea una flota nueva
            self.bullets.empty()
            self._create_fleet()
    
    def _update_aliens(self):
        """ actualiza la posición de todos los aliens de la flota """
        self._check_fleet_edges()
        self.aliens.update()
        
    
    def run_game(self):
        """ inicia el bucle principal para el juego """
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._check_updagte_screen()
            

            
if __name__ == '__main__':
    #hace una instancia del juego y lo ejecuta
    ai = AlienInvasion()
    ai.run_game()