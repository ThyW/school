#!/usr/bin/env python3

import tkinter as tk
from trie import Trie

trie = Trie()

w, h = 800, 600

window = tk.Tk()
window.title("Yes")

canvas = tk.Canvas(window, width = w, height = h, bg = "white")
canvas.pack(side = "right")

button1 = tk.Button(window, text="Insert", command = lambda:insert(trie, canvas, int(entry.get())))
entry = tk.Entry(window)

button1.pack()
entry.pack()

def insert(trie, canvas, val):
    trie.insert(val)
    draw(trie, canvas)

def draw(trie, canvas):
    canvas.create_rectangle(w/2, 10, w/2, 30, color = "green") 
    canvas.create_text(w/2, 20, text = "root")

    keys = trie.root.children.keys()
    len = len(keys)

    for key in tries:
        if len == 1:
            print("todo")

def draw_node(node, canvas):
