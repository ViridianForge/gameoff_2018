"""
Super Tutorial Level stuff to set ground work for GameOff when that kicks off.
"""

import pygame

def main():

    pygame.init()

    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Totem")

    screen = pygame.display.set_mode((240,180))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()