#! /usr/bin/env python3 

import tkinter
from ball import *

canvas=tkinter.Canvas(width=600,height=400,bg='white')
canvas.pack()

misko=Ball("Fero", "right", 10, 200, )
boni=Ball("boni", "right", 210, 300, )

while True:
    misko.move()
    misko.draw(canvas)

    boni.move()
    boni.draw(canvas)

    canvas.update()
    canvas.after(50)


canvas.mainloop()
