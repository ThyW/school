import tkinter
import random

N = 5

tk = tkinter.Tk()
canvas = tkinter.Canvas(tk, width=800, height=600)
canvas.pack()

class Obj:
    id = 0
    def __init__(self, player=False,  x=10 , y=10, rad = 20):
        self.x = x
        self.y = y
        self.rad = rad
        self.dir: int = 1
        self.player = player
        Obj.id += 1
        self.id = Obj.id

    def collision(self, o: "Obj"):
        if ((self.x + self.rad) >= o.x and (self.x + self.rad) <= (o.x + o.rad))\
            or ((self.y + self.rad) >= o.y and (self.y + self.rad) <= (o.y + o.rad)):
                return True
        return False

    def update(self):
        if self.player:
            if self.dir == 0:
                self.y -= 3
            if self.dir == 1:
                self.x += 3
            if self.dir == 0:
                self.y += 3
            if self.dir == 0:
                self.x -= 3

    def draw(self, canvas):
        if not self.player:
            canvas.delete("jedlo")
            canvas.create_oval(self.x, self.y, self.x + self.rad, self.y + self.rad, fill="red", tag="jedlo")
            return
        canvas.delete("player")
        canvas.create_rectangle(self.x, self.y, self.x + self.rad, self.y + self.rad, fill="blue", tag="player")

def done(canvas):
    canvas.create_text(400, 300, text="winned")

def loop(canvas, objs, player):
    player.update()
    if not objs:
        done(canvas)
    for obj in objs:
        if player.collision(obj):
            del obj

    for obj in objs:
        obj.draw(canvas)
    player.draw(canvas)
    canvas.after(1000//60, loop, canvas, objs, player)

objs = []
for _ in range(5):
    objs.append(Obj(x=random.randint(1, 500), y=random.randint(1, 500)))
player = Obj(player=True)
loop(canvas, objs, player)

def up():
    player.dir = 0
def down():
    player.dir = 2
def left():
    player.dir = 3
def right():
    player.dir = 1

canvas.bind("W", up)
canvas.bind("S", down)
canvas.bind("A", right)
canvas.bind("D", left)

canvas.mainloop()
