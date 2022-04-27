import tkinter
import random

tk = tkinter.Tk()
canvas = tkinter.Canvas(tk, width=800, height=600)


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
        if (self.x + self.rad >= o.x
                and self.x <= o.x + o.rad
                and self.y + self.rad >= o.y
                and self.y <= o.y + o.rad):
                return True
        return False

    def update(self):
        if self.player:
            if self.dir == 0:
                self.y -= 3
            if self.dir == 1:
                self.x += 3
            if self.dir == 2:
                self.y += 3
            if self.dir == 3:
                self.x -= 3

    def draw(self, canvas):
        if not self.player:
            canvas.delete(f"jedlo{self.id}")
            canvas.create_oval(self.x, self.y, self.x + self.rad, self.y + self.rad, fill="red", tag=f"jedlo{self.id}")
            return
        canvas.delete("player")
        canvas.create_rectangle(self.x, self.y, self.x + self.rad, self.y + self.rad, fill="blue", tag="player")

    def remove(self, canvas):
        canvas.delete(f"jedlo{self.id}")

def done(canvas):
    canvas.create_text(400, 300, text="winned")

def loop(canvas, objs, player):
    player.update()
    if not objs:
        done(canvas)
    for i, obj in enumerate(objs):
        if obj and player.collision(obj):
            obj.remove(canvas)
            del objs[i]

    for obj in objs:
        obj.draw(canvas)
    player.draw(canvas)
    canvas.after(1000//60, loop, canvas, objs, player)

objs = []
for _ in range(5):
    objs.append(Obj(x=random.randint(1, 500), y=random.randint(1, 500)))
player = Obj(player=True)

def up(event):
    print(event)
    player.dir = 0
def down(event):
    print(event)
    player.dir = 2
def left(event):
    print(event)
    player.dir = 3
def right(event):
    print(event)
    player.dir = 1


tk.bind("<Up>", up)
tk.bind("<Down>", down)
tk.bind("<Left>", left)
tk.bind("<Right>", right)

loop(canvas, objs, player)
canvas.pack()

canvas.mainloop()
