#! /usr/bin/env python3

import tkinter
import ll

window = tkinter.Tk()
window.title("Orders")

w, h = 800, 800
can = tkinter.Canvas(window, width=w, height=h, bg="white")
can.pack(side="right")

l = ll.LL("ProductID", "Name", "Amount")

button1 = tkinter.Button(window, text="Order", command=lambda:add(l, can, str(entry1.get()), int(entry2.get())))
button2 = tkinter.Button(window, text="Remove", command=lambda:remove(l, can, int(entry3.get())))
label1 = tkinter.Label(window, text="Product Name")
label2 = tkinter.Label(window, text="Amount:")
label3 = tkinter.Label(window, text="ID to remove:")
entry1 = tkinter.Entry(window)
entry2 = tkinter.Entry(window)
entry3 = tkinter.Entry(window)

label1.pack()
entry1.pack()

label2.pack()
entry2.pack()
button1.pack()

label3.pack()
entry3.pack()
button2.pack()

def add(l, can, name, amount):
    l.append(name, amount)
    can.delete("all")
    for (i, each) in enumerate(l):
        print(i)
        can.create_rectangle(20,  20 * i + 21,  220, 20 * i + 41)
        can.create_rectangle(220, 20 * i + 21,  420, 20 * i + 41)
        can.create_rectangle(420, 20 * i + 21,  620, 20 * i + 41)

        can.create_text(110, 20 * i + 26, text=str(each.id))
        can.create_text(310, 20 * i + 26, text=str(each.name))
        can.create_text(510, 20 * i + 26, text=str(each.amount))

def remove(l, can, id):
    l.delete(id)
    can.delete("all")
    for (i, each) in enumerate(l):
        can.create_rectangle(20,  20 * i + 21,  220, 20 * i + 41)
        can.create_rectangle(220, 20 * i + 21,  420, 20 * i + 41)
        can.create_rectangle(420, 20 * i + 21,  620, 20 * i + 41)

        can.create_text(110, 20 * i + 26, text=str(each.id))
        can.create_text(310, 20 * i + 26, text=str(each.name))
        can.create_text(510, 20 * i + 26, text=str(each.amount))

can.mainloop()

