import pygame
import random

# create the screen
win = pygame.display.set_mode((550,550))
pygame.display.set_caption('tic-tac-toe')

first = pygame.draw.rect(win, (255, 255, 255), (25, 25, 150, 150)) ##color
first = pygame.draw.rect(win, (255, 255, 255), (200, 25, 150, 150)) #second
third = pygame.draw.rect(win, (255, 255, 255), (375, 25, 150, 150))#th
fourth = pygame.draw.rect(win, (255, 255, 255), (25, 200, 150, 150)) ##color
fifth = pygame.draw.rect(win, (255, 255, 255), (200, 200,  150, 150))#second
sixth = pygame.draw.rect(win, (255, 255, 255), (375, 200, 150, 150))

seventh = pygame.draw.rect(win, (255, 255, 255), (25, 375, 150, 150)) ##color
eighth = pygame.draw.rect(win, (255, 255, 255), (200, 375, 150, 150))#second
ninth = pygame.draw.rect(win, (255, 255, 255), (375, 375, 150, 150))



run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():  ##what player does
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()  ##new thing happens it comes to front
pygame.quit()
