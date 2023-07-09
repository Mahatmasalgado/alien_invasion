class Settings:
    """ guarda todas las configuraciones del juego """
    
    def __init__(self):
        """ inicializa las configuraciones del juego """
        
        #de pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5