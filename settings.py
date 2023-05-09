class Settings:
    """A class to store all settings for sideway shooter"""
    def __init__ (self):
        """Initialize the game settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (170, 171, 175)

        #Ship's settings.
        self.ship_speed = 1.5

        """Bullet settings"""
        self.bullet_speed = 6.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60,60,60) 
        self.bullets_allowed = 3

        #Alien settings.
        #alien_frequency controls how often a new alien appears
        #Higher values -> more frequent aliens. Max = 1.0.
        self.alien_frequency = 0.008
        self.alien_speed = 1.5

