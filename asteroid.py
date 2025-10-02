import pygame, random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape): 
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_asteroid_1_vel = pygame.math.Vector2.rotate(self.velocity, random_angle)
            new_asteroid_1_rad = self.radius - ASTEROID_MIN_RADIUS
            asteroid = Asteroid(self.position.x, self.position.y, new_asteroid_1_rad)
            asteroid.velocity = new_asteroid_1_vel * 1.2
            new_asteroid_2_vel = pygame.math.Vector2.rotate(self.velocity, -random_angle)
            new_asteroid_2_rad = self.radius - ASTEROID_MIN_RADIUS
            asteroid = Asteroid(self.position.x, self.position.y, new_asteroid_2_rad)
            asteroid.velocity = new_asteroid_2_vel * 1.2
