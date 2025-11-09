import pygame
import random
from circleshape import CircleShape
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius,  LINE_WIDTH)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")

        new_rand_angle = random.uniform(20, 50)
        vector_asteroid_01 = self.velocity.rotate(new_rand_angle)
        vector_asteroid_02 = self.velocity.rotate(-new_rand_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        child_asteroid_01 = Asteroid(self.position[0], self.position[1], new_radius)
        child_asteroid_01.velocity = vector_asteroid_01 * 1.2
        child_asteroid_02 = Asteroid(self.position[0], self.position[1], new_radius)
        child_asteroid_02.velocity = vector_asteroid_02 * 1.2



