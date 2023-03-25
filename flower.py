from turtle import *
import turtle
def fleur():
    speed(100)
    bgcolor('black')
    color("blue")
    for i in range (300):
        circle(190-i,90)
        left(90)
        circle(190-i,90)
        left(18)

t=turtle.Turtle()

t.speed(500)
turtle.bgcolor('black')

for i in range(300):
    t.color('#f28')
    t.circle(i)
    t.left(5)

turtle.title("rainbow spiral")
speed(200)
bgcolor("black")
r,g,b = 255,0,0

for i in range(255*2):
    colormode(255)
    if i<255//3:
        g+=3
    elif i<255*2//3:
        r-=3
    elif i<255:
        b+=3
    elif i<255*4//3:
        g-=3
    elif i<255*5//3:
        r+=3
    else:
        b-=3

    fd(50+i)
    rt(81)
    pencolor(r,g,b)
fleur()
mainloop()