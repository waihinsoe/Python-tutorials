import turtle
import tkinter as TK

t = turtle.Turtle()
t.penup()
t.goto(-100, 0)
t.pendown()
t.setheading(0)

t.color('red', 'blue')
t.begin_fill()

t.circle(50)
t.end_fill()

t.penup()
t.goto(-30, 100)
t.pendown()

t.color('white', 'white')
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(0, -50)
t.pendown()

t.color('black', 'black')
t.begin_fill()
t.circle(30)
t.penup()
t.goto(0, 0)
t.pendown()
t.right(45)
for i in range(8):
    t.forward(30)
    t.backward(30)
    t.left(45)
t.end_fill()

t.hideturtle()

turtle.done()