import pygame
import random

#defining variables with Bison Dos
white = (255,255,255)
black = (0,0,0)
#Initializing and screen
pygame.init()

screen = pygame.display.set_mode((0,0),(pygame.FULLSCREEN))

def Display(classes, var, colour, x, y, xsize, ysize):
    var = classes(x, y, xsize, ysize, colour)
    var.disp()
    var.update()

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
            if key[pygame.K_w] and key[pygame.K_LSHIFT]:
                self.y -= 4
            else:
                self.y -= 2
        if key[pygame.K_a]:
            if key[pygame.K_a] and key[pygame.K_LSHIFT]:
                self.x -= 4
            else:
                self.x -= 2
        if key[pygame.K_s]:
            if key[pygame.K_s] and key[pygame.K_LSHIFT]:
                self.y += 4
            else:
                self.y += 2
        if key[pygame.K_d]:
            if key[pygame.K_d] and key[pygame.K_LSHIFT]:
                self.x += 4
            else:
                self.x += 2

#Defining OOP
Steve = Player(40,40,50,50,white)


#Running the Game
running = True
while running:
    for event in pygame.event.get():
        key = pygame.key.get_pressed()
        #User keys pressed
        pressed = pygame.display.get_window_size
        if pressed == fullscreen:
            if key[pygame.K_F11]:
                screen = pygame.display.set_mode((1400,900))

        if key[pygame.K_0] or key[pygame.K_RSHIFT] and key[pygame.K_LSHIFT]:
            running = False

        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(60)

    screen.fill((0, 0, 0))

    Steve.disp()
    Steve.update()

    pygame.display.flip()
