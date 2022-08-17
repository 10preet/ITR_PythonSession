import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
from render import Renderer

class Object(Renderer):
    def __init__(self, recordLocation = None):
        super().__init__(recordLocation = recordLocation)
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
            'x' : round(self.x, 2),
            'y' : round(self.y, 2),
            'vely' : round(self.vely, 2)
        }
        return info
    

    def plot(self):
        data = np.array(list(self.points))
        # print(data[:,1])
        plt.scatter(data[:, 0], data[:, 1], )
        plt.show()

    def step(self, dt):
        m = 1
        g = 9.8

        # y = 0.5*g*dt**2
        
        self.vely += -g*dt
        x = self.x +self.velx*dt
        y = self.y - self.vely*dt
        self.x = x
        self.y =  y
        
        self.its += 1
        if self.its % 10 == 0:
            self.points.add((self.x, self.y))

        


    def draw(self, image):
        for x, y  in self.points:
            cv2.circle(image, (int(x), int(y)), 1, (0, 0, 255), -1)

        cv2.circle(image, (int(self.x), int(self.y)), 5, (0, 255, 0), -1)

        return image



obj = Object(recordLocation = 'obj.mp4')    

for i in range(2018):
    obj.step(0.005)
    if i % 10== 0:
        obj.render(height= 600, pause = 1)


obj.plot()