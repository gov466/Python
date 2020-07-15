import pygame

# create the screen
screen = pygame.display.set_mode((800,600))

# title and icon
pygame.display.set_caption("space invader")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # RGB color
    screen.fill((0, 0, 0))
    pygame.display.update()