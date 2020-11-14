import pygame
# Add your favorite background color
background_colour = (0, 0, 255)
# Set the width and the height of the window
(width, height) = (300, 200)
# set the screen fro pygame to the width and height tuple defined above
screen = pygame.display.set_mode((width, height))
# set the name of the pygame project at the top of the window
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
