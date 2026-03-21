#!/usr/bin/python
# -*- coding: utf-8 -*-
# Importando biblioteca Pygame e inicializando-a
import pygame

from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) # Define o tamanho da janela

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass



