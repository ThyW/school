import tkinter

canvas = tkinter.Canvas(width = 800, height = 600, bg = "white")
canvas.pack()

class Player:
    def __init__(self, name):
        self.images = []
        for i in range(4):
            self.images.append(tkinter.PhotoImage(file = "images/r" + str(i+1) + ".png"))
        self.image = self.images[2]
        self.x = 64
        self.y = 64
        self.tag = name
        self.draw()
    
    def up(self, event):
        self.image = self.images[0]
        self.y -= 32
        self.draw()
    def down(self, event):
        self.image = self.images[2]
        self.y += 32
        self.draw()
    def left(self, event):
        self.image = self.images[1]
        self.x -= 32
        self.draw()
    def right(self, event):
        self.image = self.images[3]
        self.x += 32
        self.draw()
    def draw(self):
        canvas.delete(self.tag)
        canvas.create_image(self.x, self.y, image = self.image, tag = self.tag)
        canvas.after(50)

player = Player("jozko")
canvas.bind_all("w", player.up)
canvas.bind_all("s", player.down)
canvas.bind_all("a", player.left)
canvas.bind_all("d", player.right)

canvas.mainloop()
