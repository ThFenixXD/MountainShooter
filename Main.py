import pygame

pygame.init()
print('Setup Start')
display = pygame.display.set_mode((640, 480)) #Display Size
print('Setup End')

while True:
    # Check for all events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Close Window
            quit()  # end pygame
