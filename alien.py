import pygame

from pygame.sprite import Sprite

class Alien(Sprite): # a class to represent a single alien in the fleet
    def __init__(self, ai_game): #to initialize the alien and set its starting position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/alien.bmp') #to load the alien image
        self.rect = self.image.get_rect() #to set its rect attribute

        #to start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x) #to store the alien's exact horizontal position

    def update(self): #to move the alien to the right
        self.x += self.settings.alien_speed
        self.rect.x = self.x
