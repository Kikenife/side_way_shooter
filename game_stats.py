class GameStats:
    """Tract statistics for sideway shooter."""

    def __init__(self,sw_game):
        """Initialize statistics."""
        self.settings = sw_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can chsnge during the game"""
        self.ships_left = self.settings.ship_limit
