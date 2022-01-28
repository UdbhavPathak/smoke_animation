import pygame
import math
import random
pygame.init()
class Smoke:
    def __init__(self,**kwargs):
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.cy = kwargs["y"]
        self.radius = kwargs["radius"]
        self.color = kwargs["color"]
        self.size = kwargs['size']
        self.x_limit = kwargs['x_limit']
        self.speed = 1

    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

    def move(self,heading):
        self.y += -self.speed*math.sin(heading*(math.pi/180))
        self.x += -self.speed*math.cos(heading*(math.pi/180))
        if self.speed <= 0:
            self.y = self.cy
            self.radius = random.randint(*self.size)
            self.x = random.randint(*self.x_limit)
            self.speed = self.radius
        else:
            self.speed -= 0.2
            self.radius -= 0.2


class Smoke_Animation:
    def __init__(self,**kwargs):
        self.x = kwargs["x"]
        self.y = kwargs["y"]
        self.limit = kwargs["limit"]
        self.color = kwargs["color"]
        self.x_limit = [self.x-self.limit,self.x+self.limit]
        self.smokes = []
        self.angle = 0
        for i in range(kwargs["nof"]):
            smokes = Smoke(x = random.randint(*self.x_limit),y = self.y,color=(self.color)
                           ,radius = random.randint(*kwargs['size']),size=kwargs['size']
                           ,x_limit =self.x_limit)
            smokes.speed = smokes.radius
            self.smokes.append(smokes)

    def updatepos(self,x,y):
        for i in self.smokes:
            i.x_limit = [x-self.limit,x+self.limit]
            i.cy = y

    def show(self,win):
        for i in self.smokes:
            i.draw(win)
            i.move(self.angle)

if __name__ == "__main__":
    win = pygame.display.set_mode((1000,700))
    clock = pygame.time.Clock()
    fps=60
    run = True
    smokes = Smoke_Animation(x=500, y=350, limit=20, nof=100, size=[1,11]
                             ,color=(150,150,150))
    smokes.angle = 270

    while run:
        win.fill((0,0,0))
        smokes.show(win)
        #smokes.angle += 1
        pygame.draw.rect(win,(150,150,150),(470,320,60,50))
        clock.tick(fps)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run  = False
