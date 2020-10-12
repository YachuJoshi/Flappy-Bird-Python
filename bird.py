import os
import pygame
from init import screen

from const import SCREEN_HEIGHT

class Bird:
    def __init__(self):
        self.width = 26
        self.height = 38
        self.x = 70
        self.y = SCREEN_HEIGHT / 2 - self.width / 2
        self.speed = 0
        self.gravity = 0.2
        self.flap = 5
        self.image = pygame.image.load(os.path.join("images", "midflap.png"))

    def draw(self):
        screen.blit(self.image, (self.x, round(self.y)))

    def update(self):
        self.speed += self.gravity
        self.y += self.speed

    def flap_wings(self):
        self.speed = -self.flap
