import pygame
from settings import Settings
from ship import Ship
from ufo import Ufo
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #Initialize the game and create the screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Space Force")

    #Make a Ufo
    ufo = Ufo(ai_settings, screen)

    #Make a ship
    ship = Ship(screen, ai_settings)

    #Make a group to store bullets in
    bullets = Group()

    #Start the main loop of the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, ufo, bullets)

        #Make the most recently drawn screen visible
        pygame.display.flip()

run_game()
