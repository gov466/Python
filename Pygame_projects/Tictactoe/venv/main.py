import pygame
import random

# create the screen
win = pygame.display.set_mode((550,550))
pygame.display.set_caption('tic-tac-toe')

first = pygame.draw.rect(win, (255, 255, 255), (25, 25, 150, 150)) ##color
second = pygame.draw.rect(win, (255, 255, 255), (200, 25, 150, 150)) #second
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

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            ##print(pos)
            if first.collidepoint(pos):
                pygame.draw.rect(win, (255, 0, 0), (50, 50, 100, 100))

                pygame.draw.circle(win, (0, 255, 0), (100, 100), 50)
            if second.collidepoint(pos):
                pygame.draw.rect(win, (255, 0, 0), (225, 50, 100, 100))

                pygame.draw.circle(win, (0, 255, 0), (275, 100), 50)
            if third.collidepoint(pos):
                pygame.draw.rect(win, (255, 0, 0), (400, 50, 100, 100))

                pygame.draw.circle(win, (0, 255, 0), (450, 100), 50)

            if fourth.collidepoint(pos):
                pygame.draw.rect(win, (255, 0, 0), (50, 225, 100, 100))
                pygame.draw.circle(win, (0, 255, 0), (100, 275), 50)
            if fifth.collidepoint(pos):
                pygame.draw.rect(win, (255, 0, 0), (225, 225, 100, 100))
                pygame.draw.circle(win, (0, 255, 0), (275, 275), 50)
            if sixth.collidepoint(pos):
                pygame.draw.rect(win, (255, 0, 0), (400, 225, 100, 100))
                pygame.draw.circle(win, (0, 255, 0), (450, 275), 50)

            if seventh.collidepoint(pos):
                pygame.draw.rect(win, (255, 0, 0), (50, 400, 100, 100))
                pygame.draw.circle(win, (0, 255, 0), (100, 450), 50)
            if eighth.collidepoint(pos):
                pygame.draw.rect(win, (255, 0, 0), (225, 400, 100, 100))
                pygame.draw.circle(win, (0, 255, 0), (275, 450), 50)
            if ninth.collidepoint(pos):
                pygame.draw.rect(win, (255, 0, 0), (400, 400, 100, 100))
                pygame.draw.circle(win, (0, 255, 0), (450, 450), 50)
    pygame.display.update()  ##new thing happens it comes to front
pygame.quit()
