import pygame
import random
from constants import *
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, color="white", center=self.position, radius=self.radius, width=LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            #Small Asteroid - just end
            return
        log_event("asteroid_split")
        
        angle = random.uniform(20, 50)
        child_radius = self.radius - ASTEROID_MIN_RADIUS
        
        child1 = Asteroid(self.position.x, self.position.y, child_radius)
        child1.velocity = self.velocity.rotate(angle) * 1.2
        child2 = Asteroid(self.position.x, self.position.y, child_radius)
        child2.velocity = self.velocity.rotate(angle * -1) * 1.2
        

        


