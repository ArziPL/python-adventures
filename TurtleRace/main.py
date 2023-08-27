import turtle
import random

screen = turtle.Screen()

tim = turtle.Turtle()
tom = turtle.Turtle()
jack = turtle.Turtle()

list_of_turtles = [tim, tom, jack]


def setup_turtle(turtle_object, color, x, y):
    turtle_object.penup()
    turtle_object.color(color)
    turtle_object.shape("turtle")
    turtle_object.setx(x)
    turtle_object.sety(y)


setup_turtle(tim, "red", -450, 0)
setup_turtle(tom, "green", -450, 40)
setup_turtle(jack, "blue", -450, -40)

while True:
    for turtle_name in list_of_turtles:
        turtle_name.forward(random.randint(5, 30))
        if turtle_name.pos()[0] >= 460:
            turtle.textinput("End", f"{turtle_name.color()[0].capitalize()} turtle won! Click ok to end")
            screen.bye()
