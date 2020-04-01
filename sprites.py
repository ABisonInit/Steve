class loadingScreen(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(senseiFolder, "sensei.png")).convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = (width/2,height/2)
        self.y_speed = y_steve
        self.x_speed = x_steve
    def update(self):
        self.rect.x += self.x_speed
        if self.rect.y != 0:
            if self.rect.x >= width:
                self.x_speed = 0
                self.rect.x = 512
                self.rect.y = 0
        if self.x_speed == 0:
            self.rect.y += self.y_speed
            if self.rect.y >= height:
                self.rect.y = 388
                self.rect.x = 0
                self.y_speed = y_steve
                self.x_speed = x_steve
                self.rect.x += self.x_speed

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,game):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        #self.image = pygame.image.load(os.path.join(senseiFolder, "sensei.png")).convert()
        #self.image.set_colorkey(black)
        self.image = pygame.Surface((tilesize, tilesize))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = steveSpeed
        self.game = game

    def collide_wall(self, dx = 0, dy = 0):
        for wall in self.game.wall:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False
    def move(self, dx = 0, dy = 0):
        if not self.collide_wall(dx,dy):
            self.x += dx
            self.y += dy
    def update(self):
        self.rect.x = self.x * tilesize
        self.rect.y = self.y * tilesize

class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,game):
        self.groups = game.all_sprites, game.wall
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = pygame.Surface((tilesize,tilesize))
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.load_data()
        self.x = x
        self.y = y
    def update(self):
        self.rect.x = self.x * tilesize
        self.rect.y = self.y * tilesize
    def load_data(self):
        pass



