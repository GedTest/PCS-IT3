import pygame
from pygame.locals import (
    K_u,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

while running:
    for e in pygame.event.get():
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                running = False

        elif e.type == QUIT:
            running = False

    # Fill the screen with white color
    screen.fill((255, 255, 255))
    surf = pygame.Surface((50, 50))

    surf.fill((0, 0, 0))
    rect = surf.get_rect()

    surf_center = (
        (SCREEN_WIDTH - surf.get_width()) / 2,
        (SCREEN_HEIGHT - surf.get_height()) / 2
    )

    # Draw surface on the screen
    screen.blit(surf, surf_center)
    pygame.display.flip()