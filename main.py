import pygame

pygame.init()

window_size = window_width, window_height = 1280, 720
# size = [1280, 720]
window = pygame.display.set_mode(window_size, pygame.RESIZABLE)

pygame.display.set_caption('FOR3G3U')

# Create some color constants for later use.
# The colors are created by RGB mixture.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# window.fill(GREEN) This command sets the background color
background_image = pygame.image.load("test2.jpg")
# window.fill(RED)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.blit(background_image, [0, 0])
    # Now we need to update the screen(display) since we're setting the color
    # of the background manually:  the "window.fill(GREEN)" statement does that.
    # Try to comment out this line and run the program if you don't believe you need it.
    pygame.display.update()

pygame.quit()