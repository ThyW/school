#!/usr/bin/env python3
import tkinter as tk
import random

tko = tk.Tk()
c = tk.Canvas(tko, width=600, height=400)
c.pack()

balls = [[i, 10] for i in range(10)]
for i, b in enumerate(balls):
    c.create_oval(b[1], i*10, b[1]+10, i*10 + 10, tags=f"{b[0]}")

def run():
    for b in balls:
        acc = random.randint(0, 10)
        b[1] += acc
    m = max(balls, key=lambda x: x[1])
    c.delete("all")
    if m[1] > 400:
        c.create_text(400, 200, text=f"vyhral {m[0]}")
        return
    for i, b in enumerate(balls):
        if i == m[0]:
            print(True)
            c.create_oval(b[1], i*10, b[1]+10, i*10 + 10, fill="red")
        else:
            c.create_oval(b[1], i*10, b[1]+10, i*10 + 10, fill="blue")
    c.after(250, run)

c.after(250, run)
tk.mainloop()
