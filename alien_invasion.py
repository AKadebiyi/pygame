import sys #contains tools to exit the game when the player quits

import pygame #contains the functionality we need to make the game

from settings import Settings #importing Settings

from ship import Ship

from bullet import Bullet

from alien import Alien

class AlienInvasion: #Overall class to manage game assets and behavior
    def __init__(self): #Initialize the game, and create game resources
        pygame.init() #initializes the background settings
        self.settings = Settings() #creates an instance of Settings
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #to create a display window for all the game's graphical elements, called a surface, available in all methods in the class
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self) #creates an instance of Ship

        self.bullets = pygame.sprite.Group() #creates an instance of Bullet

        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #self.bg_color = (230,230,230) #to set background color

    def run_game(self): #Start the main loop for the game
        while True: #manages screen updates, runs continually
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self): #responds to keypresses and mouse events
        for event in pygame.event.get(): #accessor method that pygame uses to access events it detects
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update() #to update bullet positions

        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
                    
    def _create_fleet(self): #to create a fleet
        alien = Alien(self) #to make an alien
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width) #spacing between each alien is one alien width
        number_aliens_x = available_space_x // (2 * alien_width)

        for alien_number in range(number_aliens_x): #to create the first row of aliens
            alien = Alien(self) #to create an alien and place it in the row
            alien.x = alien_width + (2 * alien_width * alien_number)
            alien.rect.x = alien.x

            self.aliens.add(alien)


    def _update_screen(self): #to update images on the screen, and flip to the new screen
            self.screen.fill(self.settings.bg_color) #to fill the background and redraw the screen during each pass thru the loop

            self.ship.blitme()

            for bullet in self.bullets.sprites():
                bullet.draw_bullet()

            self.aliens.draw(self.screen)
    
            pygame.display.flip() # Make the most recently drawn screen visible
if __name__ == '__main__':
    ai = AlienInvasion() # Makes a game instance, 
    ai.run_game() #and runs the game