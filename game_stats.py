

class GameStats():
    """ sigue las estadisticas del juego """
    
    def __init__(self, ai_game):
        """ inicializa las estadísticas """
        self.settings = ai_game.settings
        self.reset_stats()
        
    def reset_stats(self):
        """ Inicializa las estadísticas que pueden cambiar durante el juego """
        self.ship_left = self.settings.ship_limit
