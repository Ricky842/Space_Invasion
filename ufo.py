import pygame
from pygame.sprite import Sprite

class Ufo(Sprite):
    """A class to represent a single ufo in the fleet"""
    def __init__(self, ai_settings, screen):
        """Initialize the ufo ship and set its starting position"""
        super(Ufo, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        #Start each new alien at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)