import os
import pygame
import random
import math
import time

from bird import Bird
from pipe import Pipe
from init import *
from const import *


class Game:
    def __init__(self):
        self.bird = Bird()
        self.pipes = []
        self.distance = 0
        self.score = 0

    def init(self):
        self.generate_pipes()

    def generate_pipes(self):
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
        self.pipes.append({"top": top_pipe, "bottom": bottom_pipe})

    def check_pipe_collision(self, bird, pipe):
        return (
            bird.x + bird.width / 2 > pipe["top"].x
            and bird.y - bird.height / 2 < pipe["top"].y + pipe["top"].height
        ) or (
            bird.x + bird.width / 2 > pipe["bottom"].x
            and bird.y + bird.height / 2 > pipe["bottom"].y
        )

    def check_road_collision(self, bird, road):
        return bird.y + bird.height / 2 > SCREEN_HEIGHT - road.get_height()

    def check_points(self, bird, pipe):
        return (
            bird.x + bird.width / 2 > pipe["top"].x
            and bird.y - bird.height / 2 > pipe["top"].y + pipe["top"].height
            and bird.y + bird.height / 2 < pipe["bottom"].y
        )

    def show_game_over_text(self):
        game_over = game_over_font.render(
            f"Score: {math.floor(self.score)}", True, (255, 255, 255)
        )
        screen.blit(game_over, (80, 200))

    def show_score(self):
        score_text = score_font.render(
            f"Score: {math.floor(self.score)}", True, (255, 255, 255)
        )
        screen.blit(score_text, (15, 15))

    def start(self):
        home_screen_running = True
        game_screen_running = False
        game_over_screen_running = False

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

            screen.blit(
                text, (round(SCREEN_WIDTH / 2 - 30), round(SCREEN_HEIGHT / 2 + 5))
            )
            pygame.display.update()
            clock.tick(60)

            while game_screen_running:
                screen.fill((0, 0, 0))
                screen.blit(backgroundImg, (0, 0))

                self.distance += 1

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_screen_running = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.bird.flap_wings()
                        flap_sound.play()

                self.bird.draw()
                self.bird.update()

                if self.distance % 120 == 0:
                    self.generate_pipes()

                for pipe in self.pipes:
                    if pipe["top"].x + pipe["top"].width <= 0:
                        self.pipes.pop(0)

                for pipe in self.pipes:
                    if self.check_pipe_collision(self.bird, pipe):
                        hit_sound.play()
                        die_sound.play()
                        time.sleep(0.5)
                        game_screen_running = False
                        game_over_screen_running = True
                    if self.check_points(self.bird, pipe):
                        self.score += 0.024

                if self.check_road_collision(self.bird, foregroundImg):
                    hit_sound.play()
                    die_sound.play()
                    time.sleep(0.5)
                    game_screen_running = False
                    game_over_screen_running = True

                for pipe in self.pipes:
                    pipe["top"].draw()
                    pipe["top"].update()
                    pipe["bottom"].draw()
                    pipe["bottom"].update()

                screen.blit(
                    foregroundImg, (0, SCREEN_HEIGHT - foregroundImg.get_height())
                )
                self.show_score()
                pygame.display.update()
                clock.tick(60)

            while game_over_screen_running:
                screen.fill((20, 20, 20))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over_screen_running = False

                self.show_game_over_text()
                pygame.display.update()
