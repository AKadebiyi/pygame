import sys #contains tools to exit the game when the player quits

from time import sleep

import pygame #contains the functionality we need to make the game

from settings import Settings #importing Settings

from game_stats import GameStats

from scoreboard import Scoreboard

from button import Button

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

        #to create an instance to store game stats; and create a scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self) #creates an instance of Ship

        self.bullets = pygame.sprite.Group() #creates an instance of Bullet

        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.play_button = Button(self, "Play") #to make the play button

    def run_game(self): #Start the main loop for the game
        while True: #manages screen updates, runs continually
            self._check_events()

            if self.stats.game_active: #to identify the parts that should run only when the game is active
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self): #responds to keypresses and mouse events
        for event in pygame.event.get(): #accessor method that pygame uses to access events it detects
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                
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

        self._check_bullet_alien_collissions()

    def _check_bullet_alien_collissions(self): #to respond to bullet/alien collisions
        collissions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True) #to remove any bullets and aliens that have collided

        if collissions:
            for aliens in collissions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()

        if not self.aliens: #destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
                    
    def _create_fleet(self): #to create a fleet
        alien = Alien(self) #to make an alien
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width) #spacing between each alien is one alien width
        number_aliens_x = available_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height #to determine the number of rows of aliens that fit on the screen
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows): #to create the full fleet of aliens
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _check_fleet_edges(self): #to respond appropriately if any aliens have reached an edge
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self): #to drop the entire fleet and change the fleet's direction
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_alien(self, alien_number, row_number):
            alien = Alien(self) #to create an alien and place it in the row
            alien_width, alien_height = alien.rect.size
            alien.x = alien_width + (2 * alien_width * alien_number)
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_number)
            self.aliens.add(alien)

    def _update_aliens(self): #to update the positions of all aliens in the fleet
        self._check_fleet_edges() #to check if the fleet is at an edge, then updating the positions of all aliens in the fleet
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom() #to look for aliens hitting the bottom of the screen

    def _ship_hit(self): #respond to the ship being hit by an alien
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1 #decrements ships_left
            
            self.aliens.empty() #to get rid of any remaining aliens and bullets
            self.bullets.empty()

            self._create_fleet() #to create a new fleet and center the ship
            self.ship.center_ship()

            sleep(0.5) #to pause
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True) #to make the cursor visible once game becomes inactive like when ship is hit

    def _check_aliens_bottom(self): #to check if any aliens have reached the bottom of the screen
        screen_rect = self.screen.get_rect()
        
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom: #to treat this the same as if the ship got hit
                self._ship_hit
                break

    def _check_play_button(self, mouse_pos): #to start a new game when the player clicks the Play button
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings() #to reset the game settings

            self.stats.reset_stats() #to reset the game statistics
            self.stats.game_active = True 
            self.sb.prep_score() #to prep the score when starting a new game

            #to get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet() #to create a new fleet
            self.ship.center_ship() #to center the ship

            pygame.mouse.set_visible(False) #to hide the cursor when game is active

    def _update_screen(self): #to update images on the screen, and flip to the new screen
            self.screen.fill(self.settings.bg_color) #to fill the background and redraw the screen during each pass thru the loop

            self.ship.blitme()

            for bullet in self.bullets.sprites():
                bullet.draw_bullet()

            self.aliens.draw(self.screen)

            self.sb.show_score() #to draw the score info

            if not self.stats.game_active: #to draw the play button if the game is inactive
                self.play_button.draw_button()
    
            pygame.display.flip() # Make the most recently drawn screen visible
if __name__ == '__main__':
    ai = AlienInvasion() # Makes a game instance, 
    ai.run_game() #and runs the game