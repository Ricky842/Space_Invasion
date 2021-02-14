import sys
import pygame
from bullets import Bullet

#Implement changes on Key down events  
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        #Move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        #Move ship to the left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullets(ai_settings, screen, ship, bullets):
    #Create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        #Add new_bullet to the bullets Group
        bullets.add(new_bullet)

#Implement changes on Key Up events   
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        #Move the ship to the right
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        #Move ship to the left
        ship.moving_left = False

#Implement changes on events    
def check_events(ai_settings, screen, ship, bullets):
    #Respond to keypress and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_bullets(bullets):
    """Update the position of bullets and get rid of old bullets"""
    #Get Rid of old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

#Update screen with the changes
def update_screen(ai_settings, screen, ship, ufo, bullets):
    """Updates images on the screen and flips to new screen"""
    """Redraws the screen during each pass of the loop"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    ufo.blitme()
