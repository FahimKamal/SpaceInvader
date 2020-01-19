"""
Space Invader
Created by: Fahim kamal
Date: 17.01.2020
"""
import random
import pygame
from math import sqrt
from pygame import mixer

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
# Background image
background = pygame.image.load('gamebg.gif')

# Background sound
mixer.music.load('background.wav')
mixer.music.play(-1)  # Because of -1 the sound will play in loop

# Set the player
player_img = pygame.image.load('spaceship.png')
player_x = 350
player_y = 500
player_x_change = 0

# Set the Enemies
enemy_number = 6
enemy_img = [pygame.image.load('enemy.png') for _ in range(enemy_number)]
enemy_x = [random.randint(0, 736) for _ in range(enemy_number)]
enemy_y = [random.randint(50, 150) for _ in range(enemy_number)]
enemy_x_change = [0.3 for _ in range(enemy_number)]

# Set the bullet
bullet_img = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 500
bullet_y_change = 0.7
bullet_state = 'ready'

# score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
font_x = 10
font_y = 10

def show_score():
    text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(text, (font_x, font_y))

def player():
    """place the player at a specific location"""
    screen.blit(player_img, (player_x, player_y))


def enemy(i):
    """place the enemy at a specific location"""
    screen.blit(enemy_img[i], (enemy_x[i], enemy_y[i]))


def fire():
    global bullet_state
    screen.blit(bullet_img, (bullet_x + 16, bullet_y + 10))


def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = sqrt(((enemy_x - bullet_x) ** 2) + ((enemy_y - bullet_y) ** 2))
    if distance < 27:
        return True
    return False


game_running = True

# Main game loop
while game_running:
    # Set screen color RGB - Red, Green, Blue
    screen.fill((0, 0, 0))
    # set background
    screen.blit(background, (0, 0))
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

            # press space to fire bullet
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bullet_y = player_y
                    bullet_x = player_x
                    bullet_state = 'fire'

                    # play sound
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()

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

    player()

    # Border check for enemy
    for i in range(enemy_number):
        if enemy_x[i] <= 0:
            enemy_x_change[i] *= -1
            enemy_y[i] += 36
        elif enemy_x[i] > 736:
            enemy_x_change[i] *= -1
            enemy_y[i] += 36

        enemy_x[i] += enemy_x_change[i]
        enemy(i)

        # Enemy and bullet collision check
        if is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y):
            # Bullet will be ready to fire again
            bullet_state = 'ready'
            # Enemy will goto a random location
            enemy_x[i] = random.randint(0, 736)
            enemy_y[i] = random.randint(50, 150)
            score += 1

            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            print(score)

    if bullet_state == 'fire':
        bullet_y -= bullet_y_change
        fire()

    # border check for bullet
    if bullet_y < 0:
        bullet_state = 'ready'
    show_score()
    pygame.display.update()
