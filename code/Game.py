#!/usr/bin/python
# -*- coding: utf-8 -*-
# Importando biblioteca Pygame e inicializando-a
import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((600, 480)) # Define o tamanho da janela

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()




