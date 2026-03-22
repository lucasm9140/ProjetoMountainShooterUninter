#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.health = 100
        self.score = 0 
        

    def update(self, ):
        pass

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]  # Move up
        if pressed_key[pygame.PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]  # Move down
        if pressed_key[pygame.PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]  # Move left
        if pressed_key[pygame.PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]  # Move right
        # Future: Add boundaries to prevent the player from moving off-screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIN_WIDTH:
            self.rect.right = WIN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > WIN_HEIGHT:
            self.rect.bottom = WIN_HEIGHT
            
