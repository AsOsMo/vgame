from random import uniform

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            r_angle = uniform(20, 50)
            first_velo = self.velocity.rotate(r_angle)
            second_velo = self.velocity.rotate(-r_angle)
            new_size = self.radius - ASTEROID_MIN_RADIUS

            first_ast = Asteroid(self.position[0], self.position[1], new_size)
            second_ast = Asteroid(self.position[0], self.position[1], new_size)
            first_ast.velocity = first_velo * 1.2
            second_ast.velocity = second_velo * 1.2
