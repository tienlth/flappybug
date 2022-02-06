import pygame
from objects import *
from init import *

def backgroundFix(bg):
    bg.shape.move(10, 10)
    bg.surface = pygame.transform.scale(bg.surface,[w,h])
    bg.move([0,0])

def backgroundInit():
    bg1 = object('./assets/sprites/background-day.png')
    bg2 = object('./assets/sprites/background-day.png')

    backgroundFix(bg1)
    backgroundFix(bg2)

    bg2.move([w,0])

    return [bg1,bg2]

def backgroundMove(bgs):
    for i in range(len(bgs)):   
        bgs[i].move([-1,0])
        if(bgs[i].shape.x+w==0):
            bgs[i].shape.x=w 

def backgroundsDisplay(bgs, window):
    for bg in bgs:
        bg.display(window)     
