#!/usr/bin/env python3

import tkinter
import random

tk = tkinter.Tk()
canvas = tkinter.Canvas(tk, width=800, height=600)
canvas.pack()
b1 = tkinter.Button(tk, text="generate", command=lambda: generate())
b1.pack()

ll = []
selected = []

def generate():
    global ll
    ll = [[random.randint(0, 99), i * 20, 20, i] for i in range(0, 10)]
    print(ll)
    draw()

def draw():
    print("here")
    global ll
    global canvas
    canvas.delete("all")
    for x in ll:
        text = str(x[0])
        print(text)
        canvas.create_rectangle(x[1], x[2], x[1]+20, x[2]+20)
        canvas.create_text(x[1] + 10, x[2] + 10, text=text)


def on_click(e):
    global ll
    global selected
    global canvas
    x, y = e.x, e.y
    for s in ll:
        if (x > s[1] and x < s[1] + 20) and (y > s[2] and y < s[2] + 20):
            selected.append(s[3])
            canvas.create_rectangle(s[1], s[2], s[1] + 20, s[2] + 20, outline="red")
            canvas.create_text(s[1]+10, s[2]+10, text=str(s[0]))
            if len(selected) == 2:
                swap()
            else:
                return

def swap():
    global ll
    global selected
    global canvas
    print(selected)
    i1 = selected[0]
    i2 = selected[1]
    temp = ll[i1][0]
    ll[i1][0] = ll[i2][0]
    ll[i2][0] = temp
    selected.clear()
    draw()

canvas.bind("<Button-1>", on_click)

canvas.mainloop()
