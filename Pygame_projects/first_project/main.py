import pygame
import random

# create the screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("space invader")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyImg = pygame.image.load('skull.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 1
enemyY_change = 40

# bullet
# read state you cant see bullet on screen
# fire bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = random.randint(0, 800)
bulletY = random.randint(50, 150)
bulletX_change = 4
bulletY_change = 10
bullet_state="ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))


# game loop
running = True
while running:
    screen.fill((0, 0, 0))
    # playerX += 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # if keystroke is pressed check whether its right or left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -5
        if event.key == pygame.K_RIGHT:
            playerX_change = 5
        if event.key == pygame.K_SPACE:
            fire_bullet(playerX, bulletY)
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    # RGB color
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    # checking for boundaries of enemy
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 1
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -1
        enemyY += enemyY_change
    #bullet movement
    if bullet_state is "fire":
        fire_bullet(playerX, bulletY)
        bulletY -=bulletY_change


    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
