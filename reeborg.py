# reeborg.ca - Solutions
# type: ignore

# Hurdle 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    else:
        turn_right()
        move()
        turn_right()
        move()
        while not wall_in_front():
            move()
        else:
            turn_left()
        
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()

# Maze
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if wall_in_front() and wall_on_right():
        turn_left()
        continue
    elif not wall_in_front() and wall_on_right():
        move()
    else:
        turn_right()
        move()
