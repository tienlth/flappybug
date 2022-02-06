import pygame

def birdFix(bird):
    bird.surface = pygame.transform.scale(bird.surface,[34*3/2,24*3/2])
    pass
