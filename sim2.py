import numpy as np
import math
import matplotlib.pyplot as plt
import cv2
import scipy
from render import Renderer
#  Rendere is a class(package) which helps to plot in cv2
class object(Renderer):
    def __init__(self, recordLocation=None):
        super().__init__(recordLocation=recordLocation)
        self.its = 0
        self.x = 50
        self.y = 500
        self.vel = 70
        self.theta=45
        self.velx=self.vel*math.cos(self.theta*math.pi/180)
        self.vely=self.vel*math.sin(self.theta*math.pi/180)
        self.points = set()
    
    def getInfo(self):
        info = {
            'x' : round(self.x, 4),
            'y' : round(self.y, 4),
            'vely' : round(self.vely, 4)
        }
        return info
    
    def plot(self):
        data=np.array(list(self.points))
        plt.scatter(data[:,0],data[:,1],)
        plt.show()
    
    def step(self,dt):
        g=9.81
        m=1
        self.vely += -g*dt
        x = self.x+self.velx*dt
        y = self.y-self.vely*dt
        self.x=x
        self.y=y
        
        self.its += 1
        if self.its % 50 == 0:
            self.points.add((self.x, self.y))

    def draw(self,image):
        for x,y in self.points:
            cv2.circle(image,(int(x),int(y)),1,(0,0,255),-1)
        cv2.circle(image,(int(self.x),int(self.y)),6,(0,255,0),-1)
        return image


anim=object(recordLocation='anim.mp4')
for i in range(5045):
    anim.step(0.002)
    if i % 10== 0:
        anim.render(height= 600, pause = 1)
anim.plot()        
    
            
            
            
        

# m=1

# vel=70

# theta=45
# x=50
# y=500

# dt=0.01
# g=9.81

# velx=vel*np.cos(theta*math.pi/180)
# vely=vel*np.sin(theta*math.pi/180)
# # vely +=-g*dt

# for i in range(int(2*vely/g)*100):
#     vely +=-g*dt
#     x += velx*dt
#     y += vely*dt
#     print(x,y)