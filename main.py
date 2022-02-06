from objects import * 
from bird import * 
from background import * 
from general import * 
from base import * 
from pipes import * 
from general import * 
import init

bird = bird('./assets/sprites/bluebird-midflap.png')
bird.move([32,h/2-bird.shape.height])
birdFix(bird)
 
bgs = backgroundInit()
basesBottom = baseBottomInit()
basesTop = baseTopInit()

pipes = pipesInit(3)

gameOver = object('./assets/sprites/gameover.png')
gameOver.move([w/2-gameOver.shape.width/2,h/2-gameOver.shape.height])

font = pygame.font.Font('./font/font.ttf', 32)
text = font.render('test', True, [255,255,255])
textRect = text.get_rect()
textRect.left=20
textRect.top=92

def gameLoop(): 
    scored = 0
    clock = pygame.time.Clock()
    run = True
    step=0
    gameFlg=False
    gameOverFlag=False

    global pipes, bird, bgs, basesBottom, basesTop
    while(run):
        step+=1
        clock.tick(75)

        window.fill([0,0,255]) 
        backgroundsDisplay(bgs, window)  
         
        pipesDisplay(pipes, window)
        appendPipes(pipes,step)

        baseDisplay(basesBottom, window)  
        baseDisplay(basesTop, window)  

        text = font.render(str(scored), True, [255,255,255])

        window.blit(text, textRect)

        bird.display(window)
        if(gameOverFlag): gameOver.display(window)


        for e in pygame.event.get():
            if(e.type == pygame.QUIT): run = False
            elif(e.type == pygame.KEYDOWN): 
                if(gameOverFlag==False): gameFlg=True
                else: 
                    gameOverFlag=False
                    bird.shape.left=32
                    bird.shape.top=h/2-bird.shape.height
                    pipes = pipesInit(3)
        
        if(gameFlg):
            backgroundMove(bgs)

            baseMove(basesBottom)
            baseMove(basesTop)

            pipesUpdate(pipes)

            bird.gravity([0,1])
            bird.fly(step, basesTop[0].shape.bottom)

            scored = score(bird,pipes,scored)
    
        if(collisionDetecting(bird, pipes) or bird.shape.bottom+10>=basesBottom[0].shape.top):
            gameFlg=False
            gameOverFlag=True
            scored=0
                    
        pygame.display.flip()


    # pygame.quit()

gameLoop()