class Settings: #class to store all settings for Alien Invasion
    def __init__(self): #to initaliza the game's static settings
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #Bullet settings
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3 #limits the number of bullets to 3 at a time

        #alien settings
        self.fleet_drop_speed = 10
        
        #ship settings
        self.ship_limit = 3


        self.speedup_scale = 1.1 #how quickly the game speeds up

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self): #to initialize settings that change throughout the game
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.fleet_direction = 1 #fleet direction of 1 reps right; -1 reps left

        self.alien_points = 50 #scoring

    def increase_speed(self): #increased speed settings
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale