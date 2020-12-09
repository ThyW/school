#! /usr/bin/env python3 
import random
import tkinter
import time

def load_frames(frames):
    for i in range(4):
        if i == 0:
            frames.append([])
            for j in range(49):
                frames[i].append(tkinter.PhotoImage(file="images/v" + str(i+1) + ".gif", format = "gif -index " + str(j)))
        else:
            frames.append([])
            for j in range(43):
                frames[i].append(tkinter.PhotoImage(file="images/v" + str(i+1) + ".gif", format = "gif -index " + str(j)))
    return frames

class Vojak:
    def __init__(self, x, y, name, canvas, frames):
        self._x = x
        self._y = y
        self._name = name
        self._tag = self._name + str(random.randint(0, 100000))
        self._canvas = canvas
        self._index = 15
        self._smer = 2
        self._frames = frames
        self.kresli()

    def kresli(self):
        self._canvas.delete(self._tag)
        self._canvas.create_image(self._x, self._y, image = self._frames[self._smer][self._index], tag = self._tag)
        self._canvas.create_text(self._x, self._y - 30, text=self._name, tag=self._tag)
        self._canvas.update()

    def up(self, event):
        self._index = 15
        self._smer = 0
        for _ in range(8):
            self._index += 1
            self._y -= 3
            self.kresli()
            time.sleep(0.05)
        self._index = 15
        
    def down(self, event):
        self._index = 15
        self._smer = 2
        for _ in range(8):
            self._index += 1
            self._y += 3
            self.kresli()
            time.sleep(0.05)
        self._index = 15

    def left(self, event):
        self._index = 15
        self._smer = 1
        for _ in range(8):
            self._index += 1
            self._x -= 3
            self.kresli()
            time.sleep(0.05)
        self._index = 15

    def right(self, event):
        self._index = 15
        self._smer = 3
        for _ in range(8):
            self._index += 1
            self._x += 3
            self.kresli()
            time.sleep(0.05)
        self._index = 15
    
    def attack(self, event):
        self._index = 8
        if self._smer == 0:
            for _ in range(8):
                self._index += 1
                self.kresli()
                time.sleep(0.03)
            self._index = 15

        if self._smer == 1:
            for _ in range(8):
                self._index += 1
                self.kresli()
                time.sleep(0.03)
            self._index = 15
        if self._smer == 2:
            for _ in range(8):
                self._index += 1
                self.kresli()
                time.sleep(0.03)
            self._index = 15
        if self._smer == 3:
            for _ in range(8):
                self._index += 1
                self.kresli()
                time.sleep(0.03)
            self._index = 15
        self._index = 15

    def sword(self, event):
        self._index = 22
        if self._smer == 0:
            for _ in range(7):
                self._index += 1
                self.kresli()
                time.sleep(0.03)
            self._index = 15

        if self._smer == 1:
            for _ in range(7):
                self._index += 1
                self.kresli()
                time.sleep(0.03)
            self._index = 15
        if self._smer == 2:
            for _ in range(7):
                self._index += 1
                self.kresli()
                time.sleep(0.03)
            self._index = 15
        if self._smer == 3:
            for _ in range(7):
                self._index += 1
                self.kresli()
                time.sleep(0.03)
            self._index = 15
        self._index = 15

    def bow(self, event):
        self._index = 29

        if self._smer == 0:
            for i in range(11):
                self._index += 1
                self.kresli()
                time.sleep(0.03)
            self._index = 15

        if self._smer == 1:
            for i in range(11):
                self._index += 1
                self.kresli()
                time.sleep(0.03)
            self._index = 15

        if self._smer == 2:
            for i in range(11):
                self._index += 1
                self.kresli()
                time.sleep(0.03)
            self._index = 15

        if self._smer == 3:
            for i in range(11):
                self._index += 1
                self.kresli()
                time.sleep(0.03)
            self._index = 15
        self._index = 15


    def deth(self, event):
        self._smer = 0
        self._index = 43

        for i in range(5):
            self._index += 1
            self.kresli()
            time.sleep(0.06)
        self._index = 48
