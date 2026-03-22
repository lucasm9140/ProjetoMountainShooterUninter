#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Entity import Entity
from code.EntityFactory import EntityFactory

import pygame


class Level:
    def __init__(self, window, name, selected_mode):
        self.window = window
        self.name = name
        self.entity_list = []  # lista de entidades do nível (jogadores, inimigos, objetos, etc.)
        self.selected_mode = selected_mode  # modo de jogo selecionado (1P, 2P cooperativo, 2P competitivo)
        self.entity_list.extend(EntityFactory.get_entity(self.window, 'Level1Bg', position=(0,0)))  # Adiciona o plano de fundo do nível à lista de entidades

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect) # Desenha cada entidade na janela do jogo
                ent.move() # Atualiza a posição de cada entidade (futuro: implementar lógica de movimento para jogadores, inimigos, etc.)
            pygame.display.flip() # Atualiza a tela para mostrar as entidades desenhadas
            pygame.time.Clock().tick(60) # Limita a taxa de atualização para 60 FPS
        
