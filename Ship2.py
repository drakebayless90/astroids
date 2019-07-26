class Ship2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movey = 100
        self.movex =100
        pos = (400,400)
        self.image = pygame.image.load('ship.png')
        self.image = pygame.transform.smoothscale(self.image,(100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(0, 0)
        self.health = 10

    def update(self,enemyGroup):
        self.rect.move_ip(self.speed)
        hitlist = pygame.sprite.spritecollide(self,enemyGroup, False)
        for enemy in hitlist:
            self.health -= 1
            print(self.health)