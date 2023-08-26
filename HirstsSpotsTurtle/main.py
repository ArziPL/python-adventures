# Where it came from: https://www.artsy.net/artist-series/damien-hirst-spots

import turtle as t
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def draw_hirst_line():
    for _ in range(20):
        turtle.dot(15, random_color())
        turtle.forward(30)


def next_line_setup():
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(600)
    turtle.left(180)


# Base variable setup
turtle = t.Turtle()
turtle.speed("fast")
t.colormode(255)
turtle.penup()

# Beginning setup
turtle.back(300)
turtle.right(90)
turtle.forward(300)
turtle.left(90)

# Drawing
for _ in range(20):
    draw_hirst_line()
    next_line_setup()
t.Screen().exitonclick()
