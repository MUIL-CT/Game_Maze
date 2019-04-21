import math
import turtle
import random

__Pen = turtle.Pen()

def dangle(s,t):
    r = ((s - t) % 360)
    if (r > 180):
        r = ((t - s) % 360)
    return r

def wangle(n):
    return ((180 / (math.pi)) / n)

def mxy(radius,angle):
    __Pen.goto((radius * math.cos(math.radians(angle))), (radius * math.sin(math.radians(angle))))

def arc(radius,start,n):
    __Pen.penup()
    mxy(radius, start)
    __Pen.setheading((start + 90))
    __Pen.pendown()
    __Pen.circle(radius, (360 - wangle(n)))

__Pen.hideturtle()
__Pen.speed(0)
nrings = int(turtle.numinput('Complexity','No. of rings',5))
width = turtle.numinput('Path size','Width',40)
r = width
s = random.uniform(0, 360)
arc(r, s, 1)
for i in range(1,nrings):
    t = (s + (180 - wangle(i) / 2))
    __Pen.penup()
    mxy(r, t)
    __Pen.pendown()
    r += width
    mxy(r, t)
    while True:
        s = random.uniform(0, 360)
        if (dangle(s, t) > wangle(i)):
            break
    arc(r, s, i + 1)
width /= 4
__Pen.penup()
__Pen.goto(0,0)
__Pen.pencolor('gold')
__Pen.pensize(width/2)
__Pen.pendown()
__Pen.dot(width)

def up():
    __Pen.setheading(90)
    __Pen.forward(width)

def down():
    __Pen.setheading(270)
    __Pen.forward(width)

def left():
    __Pen.setheading(180)
    __Pen.forward(width)

def right():
    __Pen.setheading(0)
    __Pen.forward(width)

turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')
turtle.listen()
turtle.mainloop()
turtle.done()
