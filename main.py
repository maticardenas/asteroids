import pygame
from pygame.color import Color
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(Color("black"))
        pygame.display.flip()
        pygame.time.wait(1000)

if __name__ == "__main__":
    main()
    