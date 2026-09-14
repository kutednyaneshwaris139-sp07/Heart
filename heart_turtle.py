import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(1)

colors = ["red", "blue", "lime", "yellow", "cyan", "magenta", "orange", "pink"]

for i in range(60):
    t.penup()
    t.goto(0, 0)

    angle = i * (math.pi * 2) / 60

    x = 16 * (math.sin(angle) ** 3) * 12
    y = (13 * math.cos(angle)
         - 5 * math.cos(2 * angle)
         - 2 * math.cos(3 * angle)
         - math.cos(4 * angle)) * 12

    t.color(random.choice(colors))
    t.pendown()
    t.goto(x, y)

    for _ in range(4):
        t.forward(6)
        t.backward(6)
        t.right(90)

turtle.done()
