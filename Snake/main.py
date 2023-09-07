import time
from turtle import *
import random

delay = 0.1
score = 0


# Assigning key headings
def goup():
    if head.heading() != 270:
        head.setheading(90)


def godown():
    if head.heading() != 90:
        head.setheading(270)


def goleft():
    if head.heading() != 0:
        head.setheading(180)


def goright():
    if head.heading() != 180:
        head.setheading(0)


# Function to trigger head movement
def move():
    if head.heading() == 90:
        y = head.ycor()
        head.sety(y + 20)
    if head.heading() == 270:
        y = head.ycor()
        head.sety(y - 20)
    if head.heading() == 180:
        x = head.xcor()
        head.setx(x - 20)
    if head.heading() == 0:
        x = head.xcor()
        head.setx(x + 20)


# Screen setup
screen = Screen()
screen.screensize(600, 600)
screen.setup(620, 620)
screen.title("Snake game")
screen.bgcolor("black")
screen.tracer(0)

# Writing on top
pen = Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Score: {score}", align="center", font=("candara", 24, "bold"))

# Initial food setup
food = Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-280, 280), random.randint(-280, 280))

# Head of snake setup
head = Turtle()
head.shape("square")
head.color("white")
head.goto(0, 0)
head.penup()

# Movement listeners
screen.listen()
screen.onkeypress(goup, "Up")
screen.onkeypress(godown, "Down")
screen.onkeypress(goleft, "Left")
screen.onkeypress(goright, "Right")

# List for segments of snake
segments = []

while True:
    # Every time everything is done update screen
    screen.update()

    # Head collision detection
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        exit()

    # Food collistion detection, adding segment, adding score
    if head.distance(food) < 20:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        new_segment = Turtle()
        new_segment.penup()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        segments.append(new_segment)
        score += 10
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("candara", 24, "bold"))

    # Movement of the segments behind the head
    # One before goes to place of the next one (-1 to head, -2 to -1), at the end move head
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()

    # Snake collision detection
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            exit()
    time.sleep(delay)

screen.mainloop()
