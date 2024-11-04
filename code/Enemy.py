#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

        if self.name == "Enemy3":
            self.vertical_speed = ENTITY_SPEED[self.name]
            self.moving_up = False

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

        if self.name == "Enemy3":
            screen_top, screen_bottom = 0, WIN_HEIGHT

            if self.rect.top <= screen_top:
                self.moving_up = False
                self.vertical_speed = ENTITY_SPEED[self.name] * 2
            elif self.rect.bottom >= screen_bottom:
                self.moving_up = True
                self.vertical_speed = ENTITY_SPEED[self.name]

            self.rect.centery -= (
                self.vertical_speed if self.moving_up else -self.vertical_speed
            )

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(
                name=f"{self.name}Shot", position=(self.rect.centerx, self.rect.centery)
            )
