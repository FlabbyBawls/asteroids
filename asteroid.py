import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def ___init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, player):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            player.score += 2
            return
        else:
            random_angle = random.uniform(20, 50)
            asteroid1_vector = self.velocity.rotate(random_angle)
            asteroid2_vector = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = asteroid1_vector * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = asteroid2_vector * 1.2
            player.score += 1
