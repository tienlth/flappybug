from objects import *
import pygame


def setBase(base, pos, ag):
    base.move(pos)
    base.surface = pygame.transform.scale(base.surface, [w,base.shape.height])
    base.surface = pygame.transform.rotate(base.surface, ag)

def baseBottomInit():
    base1 = object('./assets/sprites/base.png')
    base2 = object('./assets/sprites/base.png')

    setBase(base1,[0,h-base1.shape.height+30],0)
    setBase(base2,[w,h-base2.shape.height+30],0)

    return [base1,base2]

def baseTopInit():
    base1 = object('./assets/sprites/base.png')
    base2 = object('./assets/sprites/base.png')

    setBase(base1,[0,-30],180)
    setBase(base2,[w,-30],180)

    return [base1,base2]

def baseMove(bases):
    for i in range(len(bases)):   
        bases[i].move([-1,0])
        if(bases[i].shape.x+w==0):
            bases[i].shape.x=w 

def baseDisplay(bases, window):
    for base in bases:
        base.display(window)   
