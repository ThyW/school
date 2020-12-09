#! /usr/bin/env python3

import turtle

def troj(t, d):
    if t != 1:
        troj(t-1, d/2)
        turtle.fd(d)
        turtle.rt(120)
        troj(t-1, d/2)
        turtle.fd(d)
        turtle.rt(120)
        troj(t-1, d/2)
        turtle.fd(d)
        turtle.rt(120)
    else:
        return 

turtle.lt(60)
troj(3, 200)
turtle.mainloop()

