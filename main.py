import pygame

pygame.init()

window_size = window_width, widow_height = 1280, 720
window = pygame.display.set_mode(window_size, pygame.RESIZABLE)

pygame.display.set_caption('Skilaverkefni01')

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



pygame.quit()