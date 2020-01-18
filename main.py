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
            # If I press cross button on window the game closes
            game_running = False

        # Player movement
        # Check if any key is pressed or not
        if event.type == pygame.KEYDOWN:
            print('a key is pressed')

            # if left arrow is pressed
            if event.key == pygame.K_LEFT:
                print('Left key is pressed')

            # if right arrow is pressed
            if event.key == pygame.K_RIGHT:
                print('Right key is pressed')

        # Check if any key is released after pressing
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print('keystroke is released')

    player_x += 0.1
    player()
    pygame.display.update()