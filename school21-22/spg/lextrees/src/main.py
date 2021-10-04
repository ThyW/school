#!/usr/bin/env python3

import tkinter as tk
from trie import Trie

trie = Trie()

r = 30
d = 30

w, h = 500, 300

window = tk.Tk()
window.title("Yes")

canvas = tk.Canvas(window, width = w, height = h, bg = "white")
canvas.pack(side = "right")

button1 = tk.Button(window, text="Insert", command = lambda:insert(trie, canvas, entry.get()))
entry = tk.Entry(window)

button1.pack()
entry.pack()

def insert(trie, canvas, val):
    trie.insert(val)
    canvas.delete("all")
    draw(trie, canvas)

def draw(trie, canvas):
    y = 30
    canvas.create_rectangle(w / 2 - d, 10, w / 2 + d, y, fill = "green")
    canvas.create_text(w / 2, 20, text="root")

    pairs = trie.root.children.items()
    l = len(pairs)

    for i, key in enumerate(pairs):
        if l == 1:
            canvas.create_line(w / 2, y, w / 2, y + d)
            draw_node(key[0], key[1], canvas, w / 2, y + d)
            return
        else: 
            first, last = 300, w - 300
            left = None

            if i % 2 != 0:
                left = False
            else:
                left = True
           
            if left:
                if i == l - 1 and i % 2 == 0:
                    canvas.create_line(w / 2, y, w / 2, y + d)
                    draw_node(key[0], key[1], canvas, w / 2, y + d)
                else:
                    x = first + (d * i)

                    canvas.create_line(w / 2, y, x, y + d)
                    draw_node(key[0], key[1], canvas, x, y + d)
            else:
                x = last - (d * i)

                canvas.create_line(w / 2, y, x, y + d)
                draw_node(key[0], key[1], canvas, x, y + d)

def draw_node(char, node, canvas, x, y):
    canvas.create_oval(x - r / 2, y, x + r / 2, y + r, fill = "green")
    if node.word_end:
        char = char + "*"
    canvas.create_text(x, y + 15, text=char)

    pairs = node.children.items()
    l = len(pairs)

    for i, key in enumerate(pairs):
        if l == 1:
            canvas.create_line(x, y + d, x, y + d * 2) 
            draw_node(key[0], key[1], canvas, x, y + d * 2)
            return
        else: 
            first = x + 50
            last = x - 50

            left = None

            if i % 2 != 0:
                left = False
            else:
                left = True
           
            if left:
                if i == l - 1 and i % 2 == 0:
                    canvas.create_line(x, y + d, x, y + d * 2)
                    draw_node(key[0], key[1], canvas, x, y + d * 2)
                else:
                    x_n = first + (d * i)

                    canvas.create_line(x, y + d, x_n, y + d * 2)
                    draw_node(key[0], key[1], canvas, x_n, y + d * 2)
            else:
                import math
                x_n = last - math.ceil(d * i)

                canvas.create_line(x, y + d, x_n, y + d * 2)
                draw_node(key[0], key[1], canvas, x_n, y + d * 2)

canvas.mainloop()
