import sys
import pygame

from ship import Ship
from random import random

from settings import Settings
from bullet import Bullet
from alien_ship import Alien_ship

class Sideway_shooter:
    """Overall class to manage the games assets and behaviour."""
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Sideway_Shooter')
        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

    
    def run_game(self):
        """Strat the main loop for the game."""
        while True:
            self._check_event()

            #Consider creating a new alien.
            self._create_alien()

            self.ship.update()
            self._update_bullets()
            self.aliens.update()
            self._screen_update()    
            self.clock.tick(60)

    def _check_event(self):
        """Check for keyboard press"""
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 sys.exit()
             elif event.type == pygame.KEYDOWN:
                 self._check_keydown(event)

             elif event.type == pygame.KEYUP:
                 self._check_keyup(event)

                 
    def _check_keydown(self,event):
        if event.key == pygame.K_UP:
            #Move the ship UP.
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            #Move the ship down.
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys = exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup(self,event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets groups"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        #Update bullets position.
        self.bullets.update()

        #Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Check whether any bullets have hit an alien."""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

    def _create_alien(self):
        """Create an alien, if conditions are right."""
        if random() < self.settings.alien_frequency:
            alien = Alien_ship(self)
            self.aliens.add(alien)

    def _screen_update(self):
        #Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        """Draw the ship to the screen"""
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.aliens.draw(self.screen)

        #Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == "__main__":
    sws = Sideway_shooter()
    sws.run_game()
        



        