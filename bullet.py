import pygame

from pygame.sprite import Sprite

class Bullet(Sprite): # a class to manage bullets fired from the ship; the class inherits from Sprite from the pygame.sprite module
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Create a bullet rect at (0,0) and the set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y) #Store the bullet's position as a decimal

    def update(self): #to move the bullet up the screen
        self.y -= self.settings.bullet_speed #update the decimal position of the bullet
        self.rect.y = self.y #update the rect position

    def draw_bullet(self): #to draw the bullet to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)