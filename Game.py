from sprites import *
from settings import *
from os import path
import pygame

#Game
class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Steve")
        self.load_data()
        pygame.key.set_repeat(500,100)
        self.clock = pygame.time.Clock()
    def load_data(self):
        game_folder = path.dirname(__file__)
        self.LevelOneMap = []
        with open (path.join(game_folder, 'level_one_map.txt'), 'rt') as f:
            for line in f:
                self.LevelOneMap.append(line)

    def new(self):
        #initialize all variables and do all the setup for the game
        self.all_sprites = pygame.sprite.Group()
        self.wall = pygame.sprite.Group()
        for row, tiles in enumerate(self.LevelOneMap):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(col,row,self)
                if tile == 'P':
                    self.Steve = Player(col, row, self)


    def run(self):
        #game loop
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(fps) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, width, tilesize):
            pygame.draw.line(self.screen, lightgrey, (x,0), (x,height), 1)
        for y in range(0, width, tilesize):
            pygame.draw.line(self.screen, lightgrey, (0,y), (width,y), 1)


    def draw(self):
        self.screen.fill(navyblue)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def events(self):
        # Events
        for event in pygame.event.get():
            # HOTKEYS
            key = pygame.key.get_pressed()
            if key[pygame.K_F11]:
                self.screen = pygame.display.set_mode((width, height))
            if key[pygame.K_q] and key[pygame.K_RSHIFT] or key[pygame.K_LSHIFT]:
                self.quit()
            if event.type == pygame.QUIT:
                self.quit()
            if key[pygame.K_w]:
                self.Steve.move(dy=-1)
            if key[pygame.K_s]:
                self.Steve.move(dy=+1)
            if key[pygame.K_a]:
                self.Steve.move(dx=-1)
            if key[pygame.K_d]:
                self.Steve.move(dx=+1)
    def make_game_work(self):
        self.load_data()
        self.new()
        self.run()
        self.quit()
        self.update()
        self.draw()
game = Game()
running = True
while running:
    running = game.events()
    game.make_game_work()
    clock.tick(fps)
