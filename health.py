import pygame

class Health(pygame.sprite.Sprite):
    def __init__(self, filename, x,y):
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.smoothscale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = 500, 50
        self.rect.x = x
        self.rect.y = y

    def update(self,health):
        if health <= 5:
            self.image = pygame.image.load('halfheart.png')
            self.image = pygame.transform.smoothscale(self.image, (50, 50))
