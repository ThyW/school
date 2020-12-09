#! /usr/bin/env python3

import turtle
import random

def stvorec(t, d):
    if t != 0:
        stvorec(t-1, d/3)
        turtle.fd(d)
        turtle.rt(90)
        stvorec(t-1, d/3)
        turtle.fd(d)
        turtle.rt(90)
        stvorec(t-1, d/3)
        turtle.fd(d)
        turtle.rt(90)
        stvorec(t-1, d/3)
        turtle.fd(d)
        turtle.rt(90)
    else:
        return

stvorec(3, 300)
turtle.mainloop()
