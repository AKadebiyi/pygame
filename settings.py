class Settings: #class to store all settings for Alien Invasion
    def __init__(self): #to initaliza the game settings
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed = 1.5 #changing it from 1 pixel movement to 1.5 pixel

        #Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3 #limits the number of bullets to 3 at a time

        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 #fleet direction of 1 represents right; -1 represents left
