

import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):

    def __init__(self, x: int, y: int, radius: int) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            surface=screen,
            color=pygame.Color("grey"),
            center=self.position,
            radius=self.radius,
            width=2
        )
    
    def update(self, dt: float):
        self.move(5, dt)
    
    def move(self, velocity: int, dt: float) -> None:
        self.position +=  pygame.Vector2(0, 1) * velocity * dt