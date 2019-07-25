import pygame

class Asteroid(pygame.sprite.Sprite):
   # screen_info = pygame.display.Info()
    #size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))

    def __init__(self,x,y):
        screen_info = pygame.display.Info()
        size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
        pygame.sprite.Sprite.__init__(self)
        self.movey = x
        self.movex = y
        self.image = pygame.image.load('astroid.png')
        self.image = pygame.transform.smoothscale(self.image, (60, 60))
        self.speed = pygame.math.Vector2(0, 0)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #self.rect.center = pos

    def move(self):
        screen_info = pygame.display.Info()
        size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
        self.rect.x +=
        if self.rect.left < 0:
            self.speed[0] *= -1
        if self.rect.right > width:
            self.speed[0] *= -1
        if self.rect.top < 0:
            self.speed[1] *= -1
        if self.rect.bottom > height:
            self.speed[1] *= -1
        if self.rect.bottom > height:
            speed[1] *= -1