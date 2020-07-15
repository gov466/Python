import pygame

# create the screen
screen = pygame.display.set_mode((800,600))

# title and icon
pygame.display.set_caption("space invader")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX, playerY))
#game loop
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # RGB color

    player()
    pygame.display.update()