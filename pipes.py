import pygame
import random
from objects import *

def pipesInit(numPipesInit):
    pipes = []
    reX=0
    for i in range(numPipesInit) :
        yDis = random.randint(140, h-230)
        dis = random.randint(120,200)
        x = random.randint(w/2-200, w)
        reX=x

        if(i>0):
            lastPipeX = pipes[i-1].topPipe.shape.x
            if(abs(lastPipeX-x)<80):
                if(x>lastPipeX): 
                    x+=132
                    reX=x
                else: 
                    lastPipeX+=132
                    reX=lastPipeX
        p = pipe('./assets/sprites/pipe-green.png',reX,yDis,dis)
        pipes.append(p)
    return pipes

def pipesDisplay(pipes, des):
    for p in pipes:
        p.display(des)

def pipesUpdate(pipes):
    for p in pipes:
        p.move()

def appendPipes(pipes, step):
    speed=300
    if(step%speed==1):
        yDis = random.randint(140, h-230)
        dis = random.randint(120,200)
        x = random.randint(w, w*2)
        p = pipe('./assets/sprites/pipe-green.png',x,yDis,dis)
        pipes.append(p)
    i=0
    while(pipes[i].topPipe.shape.right<0):
        del pipes[i]

    
