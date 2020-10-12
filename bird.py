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
        self.images = [
            pygame.image.load(os.path.join("images", "midflap.png")),
            pygame.image.load(os.path.join("images", "downflap.png")),
            pygame.image.load(os.path.join("images", "midflap.png")),
            pygame.image.load(os.path.join("images", "upflap.png")),
        ]
        self.frame = 0

    def draw(self):
        screen.blit(self.images[self.frame], (self.x, round(self.y)))

    def update(self):
        self.frame += 1
        if self.frame >= len(self.images):
            self.frame = 0
        self.speed += self.gravity
        self.y += self.speed

    def flap_wings(self):
        self.speed = -self.flap
