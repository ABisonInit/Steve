import os
from sprites import *
from settings import *
import pygame

#Initializing and screen
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption(title)
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
Steve = Player()
all_sprites.add(Steve)



#Running the Game
running = True
while running:
    clock.tick(fps)
    #Events
    for event in pygame.event.get():
        #HOTKEYS
        key = pygame.key.get_pressed()
        if key[pygame.K_F11]:
            screen = pygame.display.set_mode((width,height))
        if key[pygame.K_q] and key[pygame.K_RSHIFT] or key[pygame.K_LSHIFT]:
            running = False

        #QUIT
        if event.type == pygame.QUIT:
            running = False

        #Update
        all_sprites.update()


        #Draw/Render
    screen.fill(white)
    all_sprites.draw(screen)
    pygame.display.flip()
