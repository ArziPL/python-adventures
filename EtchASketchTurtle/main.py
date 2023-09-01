import turtle
import keyboard

tim = turtle.Turtle()
screen = turtle.Screen()
screen.listen()


def tim_forward():
    tim.forward(10)


def tim_backward():
    tim.back(10)


def tim_left():
    tim.left(10)


def tim_right():
    tim.right(10)


screen.onkey(key="Up", fun=tim_forward)
screen.onkey(key="Down", fun=tim_backward)
screen.onkey(key="Left", fun=tim_left)
screen.onkey(key="Right", fun=tim_right)
screen.exitonclick()
