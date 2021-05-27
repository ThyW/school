#! /usr/bin/env python3 

import tkinter
from stack import Stack

window = tkinter.Tk()
window.title("Helloo")

canvas = tkinter.Canvas(window, width=800, height=600, bg="white")
canvas.pack()

s1 = Stack()
s2 = Stack()

button1 = tkinter.Button(window, text="Insert", command=lambda: insert(str(entry1.get()), s1, s2))
button2 = tkinter.Button(window, text="Undo", command=lambda: undo(s1, s2))
button3 = tkinter.Button(window, text="Redo", command=lambda: redo(s1, s2))
label1 = tkinter.Label(window, text="Text to insert")
entry1 = tkinter.Entry(window)

label1.pack()
entry1.pack()
button1.pack()
button2.pack()
button3.pack()


def insert(seq: str, main: Stack, undo: Stack):
    undo.clear()
    main.push(seq)
    kresli(main, undo)

def undo(main: Stack, undo: Stack):
    undo.push(main.pop().value)
    kresli(main, undo)

def redo(main: Stack, undo: Stack):
    main.push(undo.pop().value)
    kresli(main, undo)

def kresli(main: Stack, undo: Stack):
    canvas.delete("all")
    lines1 = str(main)
    lines2 = str(undo)

    for (x, line) in enumerate(lines1.splitlines()):
        if line:
            canvas.create_rectangle(100, x * 30 + 30, 200, x * 30 + 60,)
            canvas.create_text(150, x * 30 + 50, text=line)
    for (x, line) in enumerate(lines2.splitlines()):
        if line:
            canvas.create_rectangle(300, x * 30 + 30, 400, x * 30 + 60)
            canvas.create_text(350, x * 30 + 50, text=line, fill='blue')

canvas.mainloop()
