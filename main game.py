
import pygame
from ship import Ship
from astroids import Asteroid
from health import Health
#from pygame.locals import *
pygame.init()
screen_info = pygame.display.Info()
size = (width,height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 0, 0)
enemy2 = Asteroid(200, 400, 70, 5,3)
enemy = Asteroid(550 ,500, 30, 3,4)
enemy3 = Asteroid(100, 400, 60, 2,4)
enemy4 = Asteroid(300, 100, 40, 1,2)
enemy5 = Asteroid(300, 600, 50, 5, 2)
enemy6 = Asteroid(700, 600, 90, 4, 1)
enemy7 = Asteroid(900, 100, 70, 3, 5)
enemy8 = Asteroid(999, 800, 50, 1, 3)
enemy9 = Asteroid(0, 100, 70, 2, 1)
enemy0 = Asteroid(100, 900, 90, 6, 3)
enemyGroup = pygame.sprite.Group()
enemyGroup.add(enemy)
enemyGroup.add(enemy2)
enemyGroup.add(enemy3)
enemyGroup.add(enemy4)
enemyGroup.add(enemy5)
enemyGroup.add(enemy6)
enemyGroup.add(enemy8)
enemyGroup.add(enemy9)
enemyGroup.add(enemy0)

background = pygame.image.load("space.png")
background = pygame.transform.smoothscale(background,(width,height))
rectb = background.get_rect()


Player = Ship('ship4.png')
Player2 = Ship('ufo2.png')
life = Health('heart2.png', 1200, 50)
life2 = Health('heart2.png', 100, 50)
#screen.blit(background,rectb)
def main():
    while True:
        Player.update(enemyGroup)
        Player2.update(enemyGroup)
        life.update(Player.health)
        life2.update(Player2.health)
        for en in enemyGroup:
            en.move()
        screen.fill(color)
        clock.tick(60)
        screen.blit(Player.image, Player.rect)
        screen.blit(Player2.image, Player2.rect)
        screen.blit(life.image, life.rect)
        screen.blit(life2.image, life2.rect)
        enemyGroup.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                sys.exit()
                main = False

            if event.type == pygame.KEYDOWN:
                if event.key == ord('a'):
                    print('left')
                    Player.speed [0] = -5
                if event.key == ord('d'):
                    print('right')
                    Player.speed[0] = 5
                if event.key == ord('w'):
                    print('jump')
                    Player.speed[1] = -5
                if event.key == ord('s'):
                    print ('down')
                    Player.speed[1] = 5

            if event.type == pygame.KEYUP:
                if event.key == ord('a'):
                    print('left stop')
                    Player.speed[0] = 0
                if event.key == ord('d'):
                    print('right stop')
                    Player.speed[0] = 0
                if event.key == ord('w'):
                    print('up stop')
                    Player.speed[1] = 0
                if event.key == ord('s'):
                    print('down stop')
                    Player.speed[1] = 0
                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()


            if event.type == pygame.QUIT:
                pygame.quit();
                sys.exit()
                main = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print('left')
                    Player2.speed[0] = -5
                if event.key == pygame.K_RIGHT:
                    print('right')
                    Player2.speed[0] = 5
                if event.key == pygame.K_UP:
                    print('jump')
                    Player2.speed[1] = -5
                if event.key == pygame.K_DOWN:
                    print ('down')
                    Player2.speed[1] = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    print('left stop')
                    Player2.speed[0] = 0
                if event.key == pygame.K_RIGHT:
                    print('right stop')
                    Player2.speed[0] = 0
                if event.key == pygame.K_UP:
                    print('up stop')
                    Player2.speed[1] = 0
                if event.key == pygame.K_DOWN:
                    print('down stop')
                    Player2.speed[1] = 0
                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()



if __name__ == "__main__":
    main()


