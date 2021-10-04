#!/usr/bin/env python3

import tkinter as tk
import graph

g = graph.Graph()

w, h = 800, 600

window = tk.Tk()
window.title("graph")

canvas = tk.Canvas(window, width=w, height=h, bg="white")

entry = tk.Entry(window)
canvas.pack()
entry.pack()


def lclick(event):
    g.insert(event.x, event.y)
    g.draw(canvas)

def rclick(event):
    a = 0
    try:
        a = int(entry.get())
    except:
        ValueError
    g.select(event.x, event.y, a)
    g.draw(canvas)

def remv(event):
    g.remove(event.x, event.y)
    g.draw(canvas)

canvas.bind("<Button-1>", lclick)
canvas.bind("<Button-3>", rclick)
canvas.bind("<Button-2>", remv)
canvas.mainloop()
