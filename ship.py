
import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, sw_game):
        """Initialize the ship and set the settings"""
        self.screen = sw_game.screen
        self.settings = sw_game.settings
        self.screen_rect = sw_game.screen.get_rect()

        """load the ship image and get the its rect"""
        self.image = pygame.image.load("images/rocket_small.png")

        self.rect = self.image.get_rect()

        #Start each new ship at the side center of the screen.
        self.rect.midleft = self.screen_rect.midleft

        #Store a float for the ship's exact vertical position.
        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

    def update(self):
        """Update the ship's y value, not the rect."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        self.rect.y = self.y
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)