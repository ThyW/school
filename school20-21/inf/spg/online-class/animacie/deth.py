#! /usr/bin/env python3

from tkinter import *
canvas=Canvas(width=800,height=600,bg='white')
canvas.pack()

a=list()
for i in range(4):
    a.append([])
    for j in range(15,25):
        a[i].append(PhotoImage(file='images/r'+str(i+1)+'.gif',format='gif -index '+str(j)))
#        canvas.create_image(64*(j)+32,64*i+32,image=a[i][j])
umri=list()

for i in range(43,49):
    umri.append(PhotoImage(file='images/r1.gif',format='gif -index '+str(i)))

x=60
y=60
canvas.create_image(x,y,image=a[2][0])

def dole(event):
    global x,y,a
    for i in range(10):
        canvas.delete('all')
        y+=3
        canvas.create_image(x,y,image=a[2][i])
        canvas.update()
        canvas.after(50)

def hore(event):
    global x,y,a
    for i in range(10):
        canvas.delete('all')
        y-=3
        canvas.create_image(x,y,image=a[0][i])
        canvas.update()
        canvas.after(50)

def vlavo(event):
    global x,y,a
    for i in range(10):
        canvas.delete('all')
        x-=3
        canvas.create_image(x,y,image=a[1][i])
        canvas.update()
        canvas.after(50)
def vpravo(event):
    global x,y,a
    for i in range(10):
        canvas.delete('all')
        x+=3
        canvas.create_image(x,y,image=a[3][i])
        canvas.update()
        canvas.after(50)
def umrii(event):
    global x, y, a, umri
    for i in range(len(umri)):
        canvas.delete('all')
        canvas.create_image(x, y, image=umri[i])
        canvas.update()
        canvas.after(50)


canvas.bind_all('<s>',dole)
canvas.bind_all('<w>',hore)
canvas.bind_all('<a>',vlavo)
canvas.bind_all('<d>',vpravo)
canvas.bind_all('<k>',umrii)

canvas.mainloop()
