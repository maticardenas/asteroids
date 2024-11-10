

import pygame
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x: int, y: int, radius: int) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen) -> None:
        pygame.draw.circle(
            surface=screen,
            color=pygame.Color("red"),
            center=self.position,
            radius=self.radius,
            width=2
        )

    def update(self, dt: float) -> None:
        self.position = self.position + self.velocity * dt
