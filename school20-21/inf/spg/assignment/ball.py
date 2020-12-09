#! /usr/bin/env python3
import random
import math

color_list = ["red", "green", "blue", "brown", "yellow", "grey", "black"]
PI = 3.1415926535

class Ball:
    def __init__(self, name, direction, x, y):
        self.name = name
        self.direction = direction
        self.x = random.randint(x, y)
        self.y = random.randint(x, y)
        # random tag
        self.tag = self.name + str(random.randint(1,1000000))
        # random speed
        self.speed = random.randint(1, 20)
        self.color = random.choice(color_list)
        self.angle = float(0)

    def move(self):
        if self.direction == "left":
            self.x += self.speed
        else:
            self.x -= self.speed
        
        if self.x>600:
            self.direction = "right"
        elif self.x<0:
            self.direction = "left"
            
    def ang(self):
        a = (self.speed * 360) / (2 * PI * self.y / 2)
        self.angle += a

    def draw(self, canvas): 
        canvas.delete(self.tag)
        canvas.create_oval(self.x - self.speed, self.y - self.speed, self.x + self.speed, self.y + self.speed, tag=self.tag, fill=self.color)
        self.ang()
        canvas.create_text(self.x, self.y, text=self.name, angle=self.angle, tag=self.tag, fill="purple")
