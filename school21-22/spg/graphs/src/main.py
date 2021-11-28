#!/usr/bin/env python3

import tkinter as tk
import graph

g = graph.Graph()

w, h = 800, 600

window = tk.Tk()
window.title("graph")

canvas = tk.Canvas(window, width=w, height=h, bg="white")
djikstra_button = tk.Button(window, text="Djikstra", command= lambda: run_dk(g))
prim_button = tk.Button(window, text="Prim", command=lambda: run_prim(g))
color_button = tk.Button(window, text="Colormepretty", command=lambda: run_color(g))

entry = tk.Entry(window)
entry_start = tk.Entry(window)
entry_end = tk.Entry(window)
entry_prim_start = tk.Entry(window)

canvas.pack()

entry.pack()
djikstra_button.pack()
entry_start.pack()
entry_end.pack()
prim_button.pack()
entry_prim_start.pack()
color_button.pack()


def lclick(event):
    g.insert(event.x, event.y)
    g.draw(canvas)


def rclick(event):
    a = None
    try:
        a = int(entry.get())
    except:
        print("emtpy field, default weight assigned")
    finally:
        if a:
            g.select(event.x, event.y, a)
        else:
            g.select(event.x, event.y)
        g.draw(canvas)


def remv(event):
    g.remove(event.x, event.y)
    g.draw(canvas)

def run_dk(graph):
    start = int(entry_start.get())
    finish = int(entry_end.get())
    graph.djikstra(start, finish, canvas)

def run_prim(graph):
    graph.prim(int(entry_prim_start.get()), canvas)

def run_color(graph):
    graph.mapa(canvas)

canvas.bind("<Button-1>", lclick)
canvas.bind("<Button-3>", rclick)
canvas.bind("<Button-2>", remv)
canvas.mainloop()
