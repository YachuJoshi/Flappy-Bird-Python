import os
import pygame
import sys
import random

from pygame import mixer

# Init pygame
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 288, 512
# Initialize window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Title & Icon
pygame.display.set_caption("Flappy Bird")
icon = pygame.image.load(os.path.join("images", "favicon.png"))
pygame.display.set_icon(icon)

# Background image & sound
backgroundImg = pygame.image.load(os.path.join("images", "bg.png"))
# mixer.music.load(os.path.join("sounds", "background.wav"))
# mixer.music.play(-1)

# Sound effects
# bullet_sound = mixer.Sound(os.path.join("sounds", "laser.wav"))
# explosion_sound = mixer.Sound(os.path.join("sounds", "explosion.wav"))

# For fps
clock = pygame.time.Clock()


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


# white color
color = (255, 255, 255)

# light shade of the button
button_color = (255, 144, 0)

# dark shade of the button
button_color_dark = (221, 125, 0)

smallfont = pygame.font.SysFont("Corbel", 32)
text = smallfont.render("Start", True, color)

home_screen_running = True
game_screen_running = False

bird = Bird()
pipes = []
distance = 0
GAP = 380


def generate_pipes():
    top_pipe_config = {
        "x": SCREEN_WIDTH,
        "y": random.randint(-150, -10),
        "image": pygame.image.load(os.path.join("images", "pipeTop.png")),
    }
    bottom_pipe_config = {
        "x": SCREEN_WIDTH,
        "y": top_pipe_config["y"] + GAP,
        "image": pygame.image.load(os.path.join("images", "pipeBottom.png")),
    }
    top_pipe = Pipe(top_pipe_config)
    bottom_pipe = Pipe(bottom_pipe_config)
    pipes.append({"top_pipe": top_pipe, "bottom_pipe": bottom_pipe})


generate_pipes()

while home_screen_running:

    screen.fill((0, 0, 0))
    screen.blit(backgroundImg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            home_screen_running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if (
                SCREEN_WIDTH / 2 <= mouse[0] <= SCREEN_WIDTH / 2 + 60
                and SCREEN_HEIGHT / 2 <= mouse[1] <= SCREEN_HEIGHT / 2 + 180
            ):
                home_screen_running = False
                game_screen_running = True

    mouse = pygame.mouse.get_pos()
    if (
        SCREEN_WIDTH / 2 <= mouse[0] <= SCREEN_WIDTH / 2 + 60
        and SCREEN_HEIGHT / 2 <= mouse[1] <= SCREEN_HEIGHT / 2 + 80
    ):
        pygame.draw.rect(
            screen,
            button_color,
            [round(SCREEN_WIDTH / 2 - 70), round(SCREEN_HEIGHT / 2), 140, 40],
        )

    else:
        pygame.draw.rect(
            screen,
            button_color_dark,
            [round(SCREEN_WIDTH / 2 - 70), round(SCREEN_HEIGHT / 2), 140, 40],
        )

    screen.blit(text, (round(SCREEN_WIDTH / 2 - 30), round(SCREEN_HEIGHT / 2 + 5)))
    pygame.display.update()
    clock.tick(60)


while game_screen_running:
    screen.fill((0, 0, 0))
    screen.blit(backgroundImg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_screen_running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            bird.flap_wings()

    bird.draw()
    bird.update()

    for pipe in pipes:
        pipe["top_pipe"].draw()
        pipe["top_pipe"].update()
        pipe["bottom_pipe"].draw()
        pipe["bottom_pipe"].update()

    pygame.display.update()
    clock.tick(60)