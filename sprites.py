import os
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(senseiFolder, "sensei.png")).convert()
        self.image.colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = (width/2,height/2)
