import turtle as t
import numpy as np
n=50
t.shape("turtle")
t.color("blue")
t.pensize(1)
t.speed(10)
t.penup()
t.goto(0,300)
t.pendown()

def acsel():
    if y > 0:
        return s**2 / 2
    return -s**2 / 2

def jump():
    for s in range(100):
        x =  s * 2
        y =  300 + s - acsel(y) 
        t.goto(x,y)
        
jump()

