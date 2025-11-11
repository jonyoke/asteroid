import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, color="white", center=self.position, radius=self.radius, width=LINE_WIDTH)
        #print(f"Drawing Asteroid at position: {self.position} with radius {self.radius} and width {LINE_WIDTH}")

def update(self, dt):
        print(f"Updating Asteroid position")
        print(f"From: {self.position}")
        self.position += self.velocity * dt
        print(f"To  : {self.position}")

        


