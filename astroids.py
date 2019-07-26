import pygame

class Asteroid(pygame.sprite.Sprite):
   # screen_info = pygame.display.Info()
    #size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))

    def __init__(self,x,y, ast, xyz,zyx):
        screen_info = pygame.display.Info()
        size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
        pygame.sprite.Sprite.__init__(self)
        self.movey = x
        self.movex = y
        self.image = pygame.image.load('astroid.png')
        self.image = pygame.transform.smoothscale(self.image, (int(ast),(int(ast))))
        self.speed = pygame.math.Vector2(xyz, zyx)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #self.rect.center = pos

    def move(self):
        screen_info = pygame.display.Info()
        size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        if self.rect.left < 0:
            self.speed[0] *= -1
        if self.rect.right > width:
            self.speed[0] *= -1
        if self.rect.top < 0:
            self.speed[1] *= -1
        if self.rect.bottom > height:
            self.speed[1] *= -1
