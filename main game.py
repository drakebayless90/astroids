
import pygame
from ship import Ship
from astroids import Asteroid
#from pygame.locals import *
pygame.init()
screen_info = pygame.display.Info()
size = (width,height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 0, 0)
enemy2 = Asteroid(200, 400)
enemy = Asteroid(550 ,500)
enemyGroup = pygame.sprite.Group()
enemyGroup.add(enemy)
enemyGroup.add(enemy2)

background = pygame.image.load("space.png")
background = pygame.transform.smoothscale(background,(width,height))
rectb = background.get_rect()


Player = Ship()

#screen.blit(background,rectb)
def main():
    while True:
        Player.update(enemyGroup)
        for en in enemyGroup:
            en.move()
        screen.fill(color)
        clock.tick(60)
        screen.blit(Player.image, Player.rect)
        enemyGroup.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                sys.exit()
                main = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    print('left')
                    Player.speed [0] = -5
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print('right')
                    Player.speed[0] = 5
                if event.key == pygame.K_UP or event.key == ord('w'):
                    print('jump')
                    Player.speed[1] = -5
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    print ('down')
                    Player.speed[1] = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    print('left stop')
                    Player.speed[0] = 0
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print('right stop')
                    Player.speed[0] = 0
                if event.key == pygame.K_UP or event.key == ord('w'):
                    print('up stop')
                    Player.speed[1] = 0
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    print('down stop')
                    Player.speed[1] = 0
                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()




if __name__ == "__main__":
    main()


