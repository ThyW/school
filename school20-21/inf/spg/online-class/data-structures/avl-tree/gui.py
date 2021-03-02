#! /usr/bin/env python3
import impl
import tkinter

window = tkinter.Tk()
window.title("Yes")

canvas = tkinter.Canvas(window, width=800, height=600, bg="white")
canvas.pack(side="right")

bt = impl.Tree()

button1 = tkinter.Button(window, text="Insert", command = lambda:insert(bt, canvas, int(entry.get())))
button2 = tkinter.Button(window, text="Remove", command=lambda:delete(bt, canvas, int(entry.get())))
entry = tkinter.Entry(window)

button1.pack()
button2.pack()
entry.pack()

def insert(tree, canvas, val):
    tree.insert(val)
    draw(canvas, tree)

def delete(tree, canvas, val):
    tree.delete(val)
    draw(canvas, tree)

def draw(canvas, tree):
    canvas.delete("all")
    w = 800/2
    h = 50
    tree.rec_draw(canvas, w, h)

canvas.mainloop()
