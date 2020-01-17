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

def player():
    """place the player at a specific location"""
    screen.blit(player_img, (player_x, player_y))


game_running = True

# Main game loop
while game_running:
    # Set screen color RGB - Red, Green, Blue
    screen.fill((0, 0, 0))
    # Iterate through all events in pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If I press crose button on window the game closes
            game_running = False
    # Player movement
    player_x += 0.1
    player()
    pygame.display.update()