import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500, 500))


class Player:
    def __init__(self, x, y, xsize, ysize):
        self.x = x
        self.y = y
        self.xsize = xsize
        self.ysize = ysize

    def disp(self):
        pygame.draw.rect(screen, (255, 255, 255), [self.x, self.y, self.xsize, self.ysize])

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.x += 1
        if key[pygame.K_a]:
            self.x -= 1
        if key[pygame.K_w]:
            self.y -= 1
        if key[pygame.K_s]:
            self.y += 1


Steve = Player(40, 40, 100, 100)

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


