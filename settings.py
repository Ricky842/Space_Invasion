class Settings():
    """A class to store all settings for the alien invasion game"""

    def __init__(self):
        """Initialize game settings"""
        #Screen settings
        self.screen_width = 850
        self.screen_height = 650
        self.bg_color = (33, 182, 168)

        #Ship Settings
        self.ship_speed = 1.5

        #Bullet Settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5
