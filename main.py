import pygame
from constants import *


def main():
    pygame.init()
    display = pygame.display
    screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        display.flip()


if __name__ == "__main__":
    main()
