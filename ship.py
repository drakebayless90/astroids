import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self,filename):
        pygame.sprite.Sprite.__init__(self)
        self.movey = 100
        self.movex =100
        pos = (700,400)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.smoothscale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(0, 0)
        self.health = 10

    def update(self,enemyGroup):
        self.rect.move_ip(self.speed)
        hitlist = pygame.sprite.spritecollide(self,enemyGroup, False)
        for enemy in hitlist:
            self.health -= 5
            print(self.health)
            enemyGroup.remove(enemy)
        if self.health == 0:
            pygame.quit()

        screen_info = pygame.display.Info()
        size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
        if self.rect.left < 0:
            self.speed[0] *= -0.1
        if self.rect.right > width:
            self.speed[0] *= -0.1
        if self.rect.top < 0:
            self.speed[1] *= -0.1
        if self.rect.bottom > height:
            self.speed[1] *= -0.1

