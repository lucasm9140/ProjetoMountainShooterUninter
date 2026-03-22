#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import random

from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:
    @staticmethod
    def get_entity(window, entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(window, f'Level1Bg{i}', position=(0,0)))
                    list_bg.append(Background(window, f'Level1Bg{i}', position=(WIN_WIDTH,0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player('Player2', (WIN_WIDTH - 50, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))