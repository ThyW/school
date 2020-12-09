#! /usr/bin/env python3 
import SPGVojak
import tkinter

canvas = tkinter.Canvas(width = 800, height = 600, bg = "white")
canvas.pack()

frames = []

v = SPGVojak.Vojak(64, 64, "lulw", canvas, SPGVojak.load_frames(frames))

canvas.bind_all("w", v.up)
canvas.bind_all("s", v.down)
canvas.bind_all("a", v.left)
canvas.bind_all("d", v.right)
canvas.bind_all("e", v.attack)
canvas.bind_all("t", v.deth)
canvas.bind_all("q", v.sword)
canvas.bind_all("c", v.bow)

canvas.mainloop()
