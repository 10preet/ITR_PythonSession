from render import Renderer, scaleAndShow
from mimetypes import init
import numpy as np
import math
import matplotlib.pyplot as plt
import cv2

class ball(Renderer):
    def __init__(self):
        super().__init__()
        self.its = 0
        self.x = 300
        self.y = 30
        self.vel = 20
        self.theta=50
        self.velx=self.vel*math.cos(self.theta*math.pi/180)
        self.vely=self.vel*math.sin(self.theta*math.pi/180)
        self.points = set()

    def get_info(self):
        info = {
            'x' : round(self.x, 4),
            'y' : round(self.y, 4),
            'vely' : round(self.vely,4),
        }
        return info
    
    def plot(self):
        data = np.array(list(self.points))
        plt.scatter(data[:, 0], data[:, 1], )
        plt.show()
    
    def step(self,dt):
        m=1
        g=9.81
        
        self.velx=self.velx
        self.vely += -g*dt
        x=self.x+self.velx*dt
        y=self.y+self.vely*dt
        self.x=x
        self.y=y
        self.its += 1
        if self.its % 2 == 0:
            self.points.add((self.x, self.y))
    
    def draw(self, image):
        for x, y  in self.points:
            cv2.circle(image, (int(self.x), int(self.y)), 1, (0, 0, 255), -1)
        cv2.circle(image, (int(self.x), int(self.y)), 5, (0, 255, 0), -1)
        return image

anim=ball()
# anim.__init__(20,50)
for i in range(3000):
    anim.step(0.01)
    # if i % 10== 0:
    #     anim.render(height= 300, pause = 1)
anim.plot()    

        
        
        
# m=1
# g=9.81

# unit=20
# theta=50
# vely=unit*math.sin(theta*math.pi/180)
# dt=0.01
# posx=0
# posy=0
# t=2*unit*math.sin(theta*math.pi/180)/g
# T=int(t)*100
# print(T)
# for i in range(T):
#     velx=unit*math.cos(theta*math.pi/180)
#     vely += -g*dt
#     posx += velx*dt
#     posy += vely*dt
#     # print(velx,vely,posx,posy)

