import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        """Handles asteroid splitting when hit by a shot"""
        self.kill()  # Destroy this asteroid

        # If it's a small asteroid, don't split further
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Generate a random split angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Calculate new radius for smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new velocity vectors
        velocity1 = self.velocity.rotate(random_angle) * 1.2  # First asteroid, faster
        velocity2 = self.velocity.rotate(-random_angle) * 1.2  # Second asteroid, faster

        # Spawn two new asteroids at the current position
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Assign velocities to new asteroids
        new_asteroid1.velocity = velocity1
        new_asteroid2.velocity = velocity2
