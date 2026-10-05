#!/usr/bin/env python3
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TUNR_SPEED
import pygame

class Player(CircleShape):

    def __init__(self, x: float, y: float):
        #parent's constructor
        super().__init__(x, y, radius=PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, deltatime):
        self.rotation += PLAYER_TUNR_SPEED * deltatime

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # reverse delta time
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
