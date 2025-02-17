import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot  # Ensure Shot class is imported

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0  # Cooldown Timer

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        # Reduce cooldown timer every frame
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        """Create a new shot only if cooldown is over."""
        if self.shoot_timer > 0:
            return  # Prevent shooting if cooldown is active

        self.shoot_timer = PLAYER_SHOOT_COOLDOWN  # Reset cooldown timer

        # Fire a bullet in the direction the player is facing
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        shot_position = self.position + forward * self.radius  # Spawn from the tip
        Shot(shot_position.x, shot_position.y, self.rotation)

    def draw(self, screen):
        """Draws the player as a white triangle on the screen."""
        pygame.draw.polygon(screen, "white", self.triangle(), 2)  # Ensure it's white & visible

    def triangle(self):
        """Returns the 3 points of the player's triangular shape."""
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * (self.radius / 1.5)

        a = self.position + forward * self.radius  # Tip of triangle
        b = self.position - forward * self.radius - right  # Bottom left
        c = self.position - forward * self.radius + right  # Bottom right

        return [a, b, c]

    def rotate(self, dt):
        """Rotates the player by modifying its rotation angle."""
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        """Moves the player in the direction it's facing."""
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
