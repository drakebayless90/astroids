import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load('ship2.gif')
        self.image = pygame.transform.smoothscale(slef.image,(40, 40))
        self.rect = slef.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector(0, 0)

    def update(self):
        self.rect.move_ip(self.speed)