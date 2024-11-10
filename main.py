import pygame
from pygame.color import Color
from pygame.time import Clock
from asteroidfield import AsteroidField
from asteroids import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from shots import Shot


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    plyr = Player(x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(Color("black"))
        for pl in updatable:
            pl.update(dt)
        for ast in asteroids:
            if ast.collision(plyr):
                print("Game over!")
                return
        for pl in drawable:
            pl.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()