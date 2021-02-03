#! /usr/bin/env python3

import impl

import tkinter

window = tkinter.Tk()
window.title("Helloo")

canvas = tkinter.Canvas(window, width=800, height=600, bg="white")
canvas.pack()

q = impl.Queue()

button1 = tkinter.Button(window, text="Enqueue", command=lambda: e(q))
button2 = tkinter.Button(window, text="Dequeue", command=lambda: d(q))

button1.pack()
button2.pack()

counter = 0

def e(q):
    global counter
    counter += 1
    q.enqueue(counter)
    draw_add(q)

def d(q):
    draw_remove(q)

w = 800
def draw_add(q):
    l = len(str(q).splitlines())
    step = w - (l * 30)
    print(step)
    canvas.create_oval(step - 70, 200, (step + 30) - 70, 230, tag=f"o:{q.tail.val}")
    canvas.create_text((step + 15)- 70, 215, text=q.tail.val, tag=f"t:{q.tail.val}")
    for i in range(7):
        canvas.move(f"o:{q.tail.val}", 10, 0)
        canvas.move(f"t:{q.tail.val}", 10, 0)
        canvas.update()
        canvas.after(20)
    
def draw_remove(q):
    last = q.dequeue().val
    for i in range(7):
        canvas.move(f"o:{last}", 10, 0)
        canvas.move(f"t:{last}", 10, 0)
        canvas.update()
        canvas.after(20)
    canvas.delete(f"o:{last}")
    canvas.delete(f"t:{last}")
    canvas.move("all", 30, 0)

canvas.mainloop()
