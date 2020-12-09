#! /usr/bin/env python3 

import tkinter
import random

win = tkinter.Tk()
win.title("Horse game")

w, h = 800, 800
can = tkinter.Canvas(win, width=w, height=h, bg="white")
can.pack(side="right")

button1 = tkinter.Button(win, text="Run", command=lambda:chessboard(int(entry1.get())))
label1 = tkinter.Label(win, text="width and height of chessboard")
entry1 = tkinter.Entry(win)

entry1.pack()
label1.pack()
button1.pack()

def chessboard(n):
    # max amount of barricades, depends on the size of the board
    mb = n*n / 2
    # number of blocks in a single row
    mrr = mb / 2

    cb = []
    mc = 0
    for i in range(n):
        cb.append([])
        mr = 0

        for j in range(n):
            ch = random.randint(0, 1)
            if ch == 1 and mc <= mb and mr <= mrr:
                mc += 1
                mrr += 1
                cb[i].append(1)
            else:
                cb[i].append(0)
    # insert start and end
    cb[0][0] = 3
    cb[n-1][n-1] = 4
    can.delete("all")

    # draw new field
    for a in range(n):
        for b in range(n):
            if cb[a][b] == 3:
                can.create_rectangle(b * 30 + 30, a * 30 + 30, b * 30 + 60, a * 30 + 60, fill="green")
            if cb[a][b] == 4:
                can.create_rectangle(b * 30 + 30, a * 30 + 30, b * 30 + 60, a * 30 + 60, fill="purple")
            if cb[a][b] == 1:
                can.create_rectangle(b * 30 + 30, a * 30 + 30, b * 30 + 60, a * 30 + 60, fill="blue")
            if cb[a][b] == 0:
                can.create_rectangle(b * 30 + 30, a * 30 + 30, b * 30 + 60, a * 30 + 60, fill="white")
    # solve the puzzle
    solve(cb, 0, 0, n-1)

def solve(cb, x, y, n):
    # set field as visited
    cb[x][y] = 2
    # left up 2
    if x - 2 >= 0 and y - 1 >= 0:
        if cb[x-2][y-1] == 0:
            solve(cb, x-2, y-1, n)
        if cb[x-2][y-1] == 4:
            can.create_text(w-300, h-20, text="has a solution")
    # right up 1
    if x - 1 >= 0 and y + 2 <= n:
        if cb[x-1][y+2] == 0:
            solve(cb, x-1, y+2, n)
        if cb[x-1][y+2] == 4:
            can.create_text(w-300, h-20, text="has a solution")
    # left up 1
    if x - 1 >= 0 and y - 2 >= 0:
        if cb[x-1][y-2] == 0:
            solve(cb, x-1, y-2, n)
        if cb[x-1][y-2] == 4:
            can.create_text(w-300, h-20, text="has a solution")
    # right up 2
    if x - 2 >= 0 and y + 1 <= n:
        if cb[x-2][y+1] == 0:
            solve(cb, x-2, y+1, n)
        if cb[x-2][y+1] == 4:
            can.create_text(w-300, h-20, text="has a solution")
    # left down 1
    if x + 1 <= n and y - 2 >= 0:
        if cb[x + 1][y - 2] == 0:
            solve(cb, x + 1, y - 2, n)
        if cb[x + 1][y - 2] == 4: 
            can.create_text(w-300, h-20, text="has a solution")
    # left down 2 
    if x + 2 <= n and y - 1 >= 0:
        if cb[x + 2][y - 1] == 0:
            solve(cb, x + 2, y - 1, n)
        if cb[x + 2][y - 1] == 4: 
            can.create_text(w-300, h-20, text="has a solution")
    # right down 1
    if x + 1 <= n and y + 2 <= n:
        if cb[x + 1][y + 2] == 0:
            solve(cb, x + 1, y + 2, n)
        if cb[x + 1][y + 2] == 4:
            can.create_text(w-300, h-20, text="has a solution")
    # right down 2
    if x + 2 <= n and y + 1 <= n:
        if cb[x + 2][y + 1] == 0:
            solve(cb, x + 2, y + 1, n)
        if cb[x + 2][y + 1] == 4:
            can.create_text(w-300, h-20, text="has a solution")



tkinter.mainloop()

inp = [1, 2 , 3, [4, 5, [6], [8, 9, [1], 10]], 10, ['r']]

out = []

def sol(l, out):
    for e in range(len(l)):
        if str(type(l[e])) == "<class 'list'>":
            sol(l[e], out)
        else:
            out.append(l[e])

sol(inp, out)
print(out)
