#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import COLOR_ORANGE, COLOR_BLUE, MENU_OPTION, WIN_WIDTH, C_WHITE

# Classe Menu, responsável por exibir o menu do jogo
class Menu:
    def __init__(self, window):
        self.window = window # Recebe a janela do jogo para desenhar o menu
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha() # Carrega a imagem de fundo do menu
        self.rect = self.surf.get_rect(left=0, top=0) # Define a posição do menu (canto superior esquerdo)
# Método run, responsável por desenhar o menu na janela
    def run(self):
        pygame.mixer.music.load('./asset/Menu.mp3') # Carrega a música de fundo
        pygame.mixer.music.play(-1) # Reproduz a música em loop
        while True:
            self.window.blit(source=self.surf, dest=self.rect) # Desenha a imagem do menu na janela
            title_surf, title_rect = self.menu_text(text_size=50, text="Mountain", color=COLOR_ORANGE, text_center=((WIN_WIDTH / 2), 70)) # Cria superfície do título
            self.window.blit(title_surf, title_rect) # Desenha o título na janela
            subtitle_surf, subtitle_rect = self.menu_text(text_size=50, text="Shooter", color=COLOR_BLUE, text_center=((WIN_WIDTH / 2), 120)) # Cria superfície do subtítulo
            self.window.blit(subtitle_surf, subtitle_rect) # Desenha o subtítulo na janela
            
            for i in range(len(MENU_OPTION)):
                title_surf, title_rect = self.menu_text(text_size=20, text=MENU_OPTION[i], color=C_WHITE, text_center=((WIN_WIDTH / 2), 200 + i * 25)) # Cria superfície do título
                self.window.blit(title_surf, title_rect) # Desenha o título na janela
            pygame.display.flip() # Atualiza a tela para mostrar o menu desenhado

            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Se o evento for fechar a janela
                    pygame.quit() # Encerra o Pygame
                    quit() # Encerra o programa
    # Método menu_text, responsável por criar uma superfície de texto para ser desenhada no menu
    def menu_text(self, text_size: int, text: str, color: tuple, text_center: tuple):
        text_font = pygame.font.SysFont(name='Arial', size=text_size) # Cria uma fonte do sistema com o nome e tamanho especificados
        text_surf = text_font.render(text, True, color) # Renderiza o texto em uma superfície
        text_rect = text_surf.get_rect() # Obtém o retângulo da superfície do texto
        text_rect.center = text_center # Define o centro do retângulo do texto para a posição especificada
        return text_surf, text_rect # Retorna a superfície do texto e seu retângulo para ser desenhado na janela
