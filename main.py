# Importando biblioteca Pygame e inicializando-a
import pygame
pygame.init()
# Criando a janela do jogo
# Imprime mensagem de início do setup
print("Setup Started") 
# Define o tamanho da janela
window = pygame.display.set_mode(size=(600, 480)) 
# Imprime mensagem de término do setup
print("Setup Finished") 
# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Verifica se o evento é o fechamento da janela
            exit() # Encerra o programa

