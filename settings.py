class Settings:
    """ guarda todas las configuraciones del juego """
    
    def __init__(self):
        """ inicializa las configuraciones del juego """
        
        #de pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        
        #configuración de las balas
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5
        
        #configuración de los aliens
        self.alien_speed = 1.5
        self.fleet_drop_speed = 5
        #fleet_direction de 1 representa derecha; -1 representa izquierda
        self.fleet_direction = 1