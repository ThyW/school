#! /usr/bin/env python3 

import tkinter

canvas = tkinter.Canvas(width = 800, height = 600, bg = "white")
canvas.pack()

a = [[], [], [], []]
for i in range(4):
    if i == 0: 
        for x in range(49):
            a[0].append(tkinter.PhotoImage(file="images/r1.gif", format="gif -index " + str(x)))
            canvas.create_image((x % 10) * 64 + 32, (x // 10) * 64 + 32, image = a[0][x]) 
    else: 
        for x in range(43):
            a[i].append(tkinter.PhotoImage(file="images/r" + str(i) + ".gif", format="gif -index " + str(x)))

canvas.mainloop()
