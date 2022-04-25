#!/usr/bin/env python3

from typing import Tuple, List
import math
import tkinter
import random


class Ball:
    def __init__(self, y: int,
                 name: str = "ball",
                 size: int = 20,
                 speed: float = 2.5,
                 color: str = "white") -> None:
        self.name = name
        self.size = size
        self.speed = speed
        self.angle: float = 0
        self.x, self.y = 0, y
        self.color = color

    def update(self, canvas: tkinter.Canvas) -> None:
        move = (self.speed / math.pi)
        self.x += move
        if self.x > 800:
            return
        self.angle -= self.speed
        canvas.delete(self.name)
        c = self.coords()
        canvas.create_oval(c[0][0],
                           c[0][1],
                           c[1][0],
                           c[1][1],
                           fill=self.color,
                           tags=self.name)
        canvas.create_text(self.x,
                           float(self.y),
                           angle=self.angle,
                           tags=self.name,
                           text=self.name)

    def coords(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        return ((self.x - self.size, self.y - self.size),
                (self.x + self.size, self.y + self.size))


def update(canvas: tkinter.Canvas, balls: List[Ball]) -> None:
    for b in balls:
        b.update(canvas)

    canvas.after(int(1000/60), update, canvas, balls)


def main() -> None:
    tk = tkinter.Tk()
    canvas = tkinter.Canvas(tk, width=800, height=600)
    canvas.pack()
    b1 = Ball(20, "alfa",
              size=random.randint(10, 20),
              speed=random.randint(1, 20),
              color="red")
    b2 = Ball(100,
              "beta",
              size=random.randint(20, 50),
              speed=random.randint(1, 20),
              color="gray")

    balls = [b1, b2]

    canvas.after(int(1000/60), update, canvas, balls)
    tk.mainloop()


if __name__ == "__main__":
    main()
