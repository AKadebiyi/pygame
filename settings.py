class Settings: #class to store all settings for Alien Invasion
    def __init__(self): #to initaliza the game settings
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed = 1.5 #changing it from 1 pixel movement to 1.5 pixel

        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
