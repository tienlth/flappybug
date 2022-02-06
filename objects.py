from init import *
from bird import *

class object:
    def __init__(self, src):
        self.src = src
        self.surface = pygame.image.load(src)
        self.shape = self.surface.get_rect()
    
    def display(self,des):
        des.blit(self.surface,self.shape)

    def move(self,vect):
        self.shape = self.shape.move(vect)

    def gravity(self, g):  
        self.move(g)

class bird(object):
    def __init__(self,src):
        super().__init__(src)
        self.flyFlg=True
        self.flyAmount=0

    def fly(self, step, top):
        if(step%60==1): self.flyFlg=True
        if(pygame.key.get_pressed()[pygame.K_SPACE] and self.flyFlg):
            self.flyAmount = 20
            self.flyFlg=False

            self.surface = pygame.image.load('./assets/sprites/bluebird-downflap.png')
            birdFix(self)

        if(self.shape.top-5<=top): self.flyAmount=0
        if(self.flyAmount>0): 
            self.move([0,-5])
            self.flyAmount -= 1
        elif(self.flyAmount==0): 
            self.surface = pygame.image.load('./assets/sprites/bluebird-upflap.png')
            birdFix(self)
            self.flyAmount=-1

class pipe():
    def __init__(self,src, x , disY, dis):
        self.distance = dis
        self.topPipe = object(src)
        self.bottomPipe = object(src)
        self.topPipe.surface = pygame.transform.rotate(self.topPipe.surface, 180)
        self.topPipe.move([x,disY-self.topPipe.shape.height])
        self.bottomPipe.move([self.topPipe.shape.x, disY+dis])

    def display(self, des):
        self.topPipe.display(des)
        self.bottomPipe.display(des)
        
    def move(self):
        self.topPipe.move([-1,0])
        self.bottomPipe.move([-1,0])
        
        