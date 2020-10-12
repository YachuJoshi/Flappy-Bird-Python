import os
import pygame
import sys
from pygame import mixer

from const import SCREEN_WIDTH, SCREEN_HEIGHT, color

# Init pygame
pygame.init()

# Initialize window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Title & Icon
pygame.display.set_caption("Flappy Bird")
icon = pygame.image.load(os.path.join("images", "favicon.png"))
pygame.display.set_icon(icon)

# Background image & sound
backgroundImg = pygame.image.load(os.path.join("images", "bg.png"))
foregroundImg = pygame.image.load(os.path.join("images", "fg.png"))

# Sound effects
hit_sound = mixer.Sound(os.path.join("sounds", "hit.wav"))
die_sound = mixer.Sound(os.path.join("sounds", "die.wav"))
flap_sound = mixer.Sound(os.path.join("sounds", "flap.wav"))

# For fps
clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("Corbel", 32)
text = smallfont.render("Start", True, color)
score_font = pygame.font.Font("freesansbold.ttf", 18)
game_over_font = pygame.font.Font("freesansbold.ttf", 32)