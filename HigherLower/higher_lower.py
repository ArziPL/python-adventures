# Day 14 - project 1
import data
import random
import os

# Base variables
data = data.data
list_of_picks = [item for item in range(50)]
def clear(): return os.system('cls')

# Picking random data and deleting it from list with indexes of all available picks, with every pick it returns the pick and deletes possibility of using it again
def random_pick():
    global data
    global list_of_picks
    pick = random.choice(list_of_picks)
    list_of_picks.remove(pick)
    return data[pick]


# Start a game with inital variables
pick_a = random_pick()
pick_b = random_pick()
score = 0

while True:
    # Print first fight, let player input their guess
    print(f"A: {pick_a['name']}, {pick_a['description']} from {pick_a['country']} with followers count of {pick_a['follower_count']}m")
    print(
        f"B: {pick_b['name']}, {pick_b['description']} from {pick_b['country']}")
    player_pick = input("Type 'A' or 'B': ").lower()

    # Check for all loosing scenarios
    lose_scenario_a = pick_a['follower_count'] < pick_b['follower_count'] and player_pick == "a"
    lose_scenario_b = pick_a['follower_count'] > pick_b['follower_count'] and player_pick == "b"
    lose_scenario = lose_scenario_a or lose_scenario_b

    # Check final condition, lose scenario or win scenario
    if lose_scenario:
        clear()
        if lose_scenario_a:
            print(
                f"\nYou lost, {pick_b['name']} has {pick_b['follower_count']}m which is {pick_b['follower_count'] - pick_a['follower_count']}m more followers then {pick_a['name']}")
        if lose_scenario_b:
            print(
                f"\nYou lost, {pick_a['name']} has {pick_a['follower_count']}m which is {pick_a['follower_count'] - pick_b['follower_count']}m more followers then {pick_b['name']}")
        print(f"Your final score was: {score}")
        break
    # Win scenario, in the meantime check if whole game wasn't won by checking len of list_of_picks, if there's no more picks you get "big win", if not, change picks places and find new one
    else:
        score += 1
        clear()
        if len(list_of_picks) == 0:
            print(
                f"You won the game! There'are not other picks, final score: {score}")
            break
        print(f"Good guess, your current score: {score}")
        pick_a = pick_b
        pick_b = random_pick()
