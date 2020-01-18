"""
Space Invader
Created by: Fahim kamal
Date: 17.01.2020
"""
import random

import pygame

# Initialize the pygame
pygame.init()

# Initialize the screen size
screen = pygame.display.set_mode((800, 600))
# Initialize the title of screen
pygame.display.set_caption('Space Invader by Fahim')
# Initialize the icon
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
# Set screen color RGB - Red, Green, Blue
screen.fill((0, 0, 0))

# Set the player
player_img = pygame.image.load('spaceship.png')
player_x = 350
player_y = 500
player_x_change = 0


# Set the Enemy
enemy_img = pygame.image.load('enemy.png')
enemy_x = random.randint(0, 736)
enemy_y = random.randint(50, 150)
enemy_x_change = 0.3

def player():
    """place the player at a specific location"""
    screen.blit(player_img, (player_x, player_y))

def enemy():
    """place the player at a specific location"""
    screen.blit(enemy_img, (enemy_x, enemy_y))


game_running = True

# Main game loop
while game_running:
    # Set screen color RGB - Red, Green, Blue
    screen.fill((0, 0, 0))
    # Iterate through all events in pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If I press cross button on window the game closes
            game_running = False

        # Player movement
        # Check if any key is pressed or not
        if event.type == pygame.KEYDOWN:
            print('a key is pressed')

            # if left arrow is pressed
            if event.key == pygame.K_LEFT:
                print('Left key is pressed')
                player_x_change = -0.5

            # if right arrow is pressed
            if event.key == pygame.K_RIGHT:
                print('Right key is pressed')
                player_x_change = 0.5

        # Check if any key is released after pressing
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print('keystroke is released')
                player_x_change = 0

    # Change the player location
    player_x += player_x_change

    # border check for player
    if player_x <= 0:
        # Left border
        player_x = 0
    elif player_x >= 736:
        # Right border
        player_x = 736

    # Border check for enemy
    if enemy_x <= 0:
        enemy_x_change *= -1
        enemy_y += 36
    elif enemy_x > 736:
        enemy_x_change *= -1
        enemy_y += 36

    enemy_x += enemy_x_change

    player()
    enemy()
    pygame.display.update()