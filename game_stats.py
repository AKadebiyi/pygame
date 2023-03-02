class GameStats: #to track statistics for Alien Invasion
    def __init__(self, ai_game): #to initialize statistics
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False #to start Alien Invasion in an inactive state

    def reset_stats(self): #to initialize stats that can change during the game
        self.ships_left = self.settings.ship_limit