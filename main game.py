
import pygame
#from pygame.locals import *
pygame.init()
screen_info = pygame.display.Info()
size = (width,height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (255, 255, 0)




Player = Ship((LevelData['PlayerX'], 0))


def main():
    while True:
        clock.tick(60)
        screen.fill(color)
        pygame.display.flip()
if __name__ == "__main__":
     main()





def main():
    while True:
        clock.tick(60)
        screen.fill(color)
        screen.blit(Player.image, Player.rect)
        pygame.display.flip()
if __name__ == "__main__":
     main()
