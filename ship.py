import pygame

class Ship: #a class to manage the ship
    def __init__(self,ai_game): #to initialize the ship and set its starting position. ai game will give ship access to all the resources of alien invasion
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp') #to load the ship
        self.rect = self.image.get_rect() #to get ship's rect

        self.rect.midbottom = self.screen_rect.midbottom #to start each new ship at the bottom center of the screen

        self.x = float(self.rect.x) # to store a decimal value for the ship's horizontal position
        
        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self): #to update the ship's position based on the movement flag
        if self.moving_right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left:
            self.rect.x -= self.settings.ship_speed

        self.rect.x = self.x #update rect object from self.x

    def blitme(self): #to draw the ship at its current location
        self.screen.blit(self.image, self.rect)

