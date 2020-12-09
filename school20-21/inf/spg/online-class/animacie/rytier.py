#! /usr/bin/env python3
import SPGVojak
import tkinter

canvas = tkinter.Canvas(width=800, height=600, bg="white")
canvas.pack()

frames = []

class Rytier(SPGVojak.Vojak):
    def __init__(self, x, y, name, canvas, level=str()):
        self.level = level
        super().__init__(x, y, name, canvas, SPGVojak.load_frames(frames))

    def kresli(self):
        super().kresli()
        canvas.create_text(100, 30, text = "Level: " + str(self.level), font = "Cousine 12", fill = "black")

r = Rytier(500, 500, "Jozo", canvas)

canvas.bind_all("w", r.up)
canvas.bind_all("s", r.down)
canvas.bind_all("a", r.left)
canvas.bind_all("d", r.right)

while True:
    r.kresli()

