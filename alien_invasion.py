import sys #contains tools to exit the game when the player quits

import pygame #contains the functionality we need to make the game

from settings import Settings #importing Settings

class AlienInvasion: #Overall class to manage game assets and behavior
    def __init__(self): #Initialize the game, and create game resources
        pygame.init() #initializes the background settings
        self.settings = Settings() #creates an instance of Settings
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height)) #to create a display window for all the game's graphical elements, called a surface, available in all methods in the class
        pygame.display.set_caption("Alien Invasion")

        #self.bg_color = (230,230,230) #to set background color

    def run_game(self): #Start the main loop for the game
        while True: #manages screen updates, runs continually
            for event in pygame.event.get(): #accessor method that pygame uses to access events it detects
                if event.type == pygame.QUIT: 
                    sys.exit()

                self.screen.fill(self.settings.bg_color) #to fill the background and redraw the screen during each pass thru the loop
    
                pygame.display.flip() # Make the most recently drawn screen visible
if __name__ == '__main__':
    ai = AlienInvasion() # Makes a game instance, 
    ai.run_game() #and runs the game