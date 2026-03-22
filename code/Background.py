#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.Entity import Entity


class Background(Entity):
    def __init__(self, window, name, position):
        super().__init__(name, position)
        self.window = window

    def move(self):
        self.rect.x -= 5  # Move the background to the left
        self.rect.centerx -= ENTITY_SPEED[self.name]  # Adjust the speed of the background movement
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH  # Reset position when off-screen

