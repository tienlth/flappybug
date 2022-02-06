from init import *

def collisionDetecting(bird, pipes):
    resu = False
    birdR=bird.shape.left+bird.shape.width*3/2
    birdCX=bird.shape.centerx
    birdT=bird.shape.top
    birdB=birdT+bird.shape.height*3/2
    for pipe in pipes:
        topPipeShape=pipe.topPipe.shape
        bottomPipeShape=pipe.bottomPipe.shape
        if(((birdR >= topPipeShape.left and birdR <= topPipeShape.right) or (birdCX >= topPipeShape.left and birdCX <= topPipeShape.right)) and 
        (birdT <= topPipeShape.bottom or birdB >= bottomPipeShape.top)):
            resu = True
            break

    return resu

def score(bird, pipes, scored):
    birdR=bird.shape.left+bird.shape.width*3/2
    for pipe in pipes:
        topPipeShape=pipe.topPipe.shape
        if(birdR == topPipeShape.right):
            scored+=1
            break
    return scored
