#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import random

from code.Const import EVENT_ENEMY, MENU_OPTION, SPAWN_TIME, WIN_HEIGHT, C_WHITE, WIN_WIDTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory

import pygame


class Level:
    def __init__(self, window, name, selected_mode):
        self.window = window
        self.name = name
        self.entity_list = []  # lista de entidades do nível (jogadores, inimigos, objetos, etc.)
        self.timeout = 0
        self.selected_mode = selected_mode  # modo de jogo selecionado (1P, 2P cooperativo, 2P competitivo)
        self.entity_list.append(EntityFactory.get_entity(self.window, 'Level1Bg', position=(0,0)))  # Adiciona o plano de fundo do nível à lista de entidades
        self.entity_list.append(EntityFactory.get_entity(self.window, 'Player1', position=(10, WIN_HEIGHT / 2)))
        self.timeout = 20000  # Tempo limite para o nível (20 segundos para teste, futuro: ajustar conforme necessário)
        if self.selected_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity(self.window, 'Player2', position=(WIN_WIDTH - 50, WIN_HEIGHT / 2)))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)  # Define um timer para gerar inimigos a cada 2 segundos

    def run(self, ):
        pygame.mixer.music.load('./asset/Level1.mp3')  # Carrega a música de fundo do nível
        pygame.mixer.music.play(-1)  # Inicia a reprodução da música em loop
        clock = pygame.time.Clock()  # Cria um relógio para controlar a taxa de atualização do jogo
        while True:
            clock.tick(60)  # Limita a taxa de atualização para 60 FPS
            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect) # Desenha cada entidade na janela do jogo
                ent.move() # Atualiza a posição de cada entidade (futuro: implementar lógica de movimento para jogadores, inimigos, etc.)
            for event in pygame.event.get(): # Verifica os eventos do jogo (teclado, mouse, etc.)
                if event.type == pygame.QUIT: # Se o evento for fechar a janela
                    pygame.quit() # Encerra o Pygame
                    quit() # Encerra o programa
                if event.type == EVENT_ENEMY: # Se o evento for o timer de geração de inimigos
                    choice = random.choice(['Enemy1', 'Enemy2']) # Escolhe aleatoriamente entre os tipos de inimigos
                    self.entity_list.append(EntityFactory.get_entity(self.window, choice)) # Adiciona um novo inimigo do tipo escolhido à lista de entidades
            self.timeout -= clock.get_time() # Reduz o tempo restante do nível com base no tempo decorrido desde a última atualização
            if self.timeout <= 0: # Se o tempo do nível acabar
                break # Encerra o loop do nível (futuro: implementar lógica de transição para o próximo nível ou tela de resultados)
            
            # printed text
            self.level_text(text_size=14, text=f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', color=C_WHITE, text_pos=(10, 5))
            self.level_text(text_size=14, text=f'fps: {clock.get_fps():.1f}', color=C_WHITE, text_pos=(10, WIN_HEIGHT - 35))
            self.level_text(text_size=14, text=f'entidades: {len(self.entity_list)}', color=C_WHITE, text_pos=(10, WIN_HEIGHT - 20))

            pygame.display.flip() # Atualiza a tela para mostrar as entidades desenhadas

    def level_text(self, text_size: int, text: str, color: tuple, text_pos: tuple):
        text_font = pygame.font.SysFont(name='Arial', size=text_size) # Cria uma fonte do sistema com o nome e tamanho especificados
        text_surf = text_font.render(text, True, color).convert_alpha() # Renderiza o texto em uma superfície
        text_rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1]) # Obtém o retângulo da superfície do texto
        text_rect.topleft = text_pos # Define a posição do retângulo do texto para a posição especificada
        self.window.blit(text_surf, text_rect) # Desenha o texto na janela do jogo
