import pygame
import random

#defining variables with Bison Dos
white = (255,255,255)
black = (0,0,0)
navy

pygame.init()

screen = pygame.display.set_mode((500, 500))


class Player:
    def __init__(self, x, y, xsize, ysize, colour):
        self.x = x
        self.y = y
        self.xsize = xsize
        self.ysize = ysize
        self.colour = colour

    def disp(self):
        pygame.draw.rect(screen, self.colour, [self.x, self.y, self.xsize, self.ysize])

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.y -= 1
        if key[pygame.K_a]:
            self.x -= 1
        if key[pygame.K_s]:
            self.y += 1
        if key[pygame.K_d]:
            self.x += 1 
        if key[pygame.K_SHIFT] and [pygame.K_w]:
            self.y -= 2
        if key[pygame.K_SHIFT] and [pygame.K_a]:
            self.x -= 2
        if key[pygame.K_SHIFT] and [pygame.K_s]:
            self.y += 2
        if key[pygame.K_SHIFT] and [pygame.K_d]:
            self.x += 2
        if key[pygame.K_CTRL] and [pygame.K_w]:
            self.y -= 

Steve = Player(40, 40, 50, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(60)

    screen.fill((0, 0, 0))

    Steve.disp()
    Steve.update()

    pygame.display.flip()


