import pygame
from init import screen

class Pipe:
    def __init__(self, props):
        self.width = 52
        self.height = 242
        self.x = props["x"]
        self.y = props["y"]
        self.image = props["image"]
        self.dx = 2

    def draw(self):
        screen.blit(self.image, (round(self.x), round(self.y)))

    def update(self):
        self.x -= self.dx