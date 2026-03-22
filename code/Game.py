#!/usr/bin/python
# -*- coding: utf-8 -*-
# Importando biblioteca Pygame e inicializando-a
import pygame

from code.Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) # Define o tamanho da janela

    def run(self):
        while True:
            menu = Menu(self.window)
            selected = menu.run()
            if selected is None:
                continue

            if selected == MENU_OPTION.index("NEW GAME 1P"):
                print("Starting new game for 1 player...") # Future: Initialize and start the single-player game
                level = Level(self.window, 'Level1', selected) # Future: Create a Level instance to manage the game level
                level.run()
            elif selected == MENU_OPTION.index("NEW GAME 2P - COOPERATIVE"):
                print("Starting new cooperative game for 2 players...") # Future: Initialize and start the cooperative multiplayer game
                level = Level(self.window, 'Level1', selected) # Future: Create a Level instance to manage the game level
                level.run()
            elif selected == MENU_OPTION.index("NEW GAME 2P - COMPETITIVE"):
                print("Starting new competitive game for 2 players...") # Future: Initialize and start the competitive multiplayer game
                level = Level(self.window, 'Level1', selected) # Future: Create a Level instance to manage the game level
                level.run()
            elif selected == MENU_OPTION.index("SCORE"):
                print("Showing scores...") # Future: Show the scores screen 
                continue # Reopen menu after game ends or for now, since game is not implemented
            if MENU_OPTION[selected].upper().startswith("EXIT"):
                pygame.quit()
                quit()
            # For now, other options are not implemented — reopen menu
            # Future: start game, show scores, etc.



