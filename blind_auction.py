# Day 9 - project 1
import os
def clear(): return os.system('cls')


bids = {}
while True:
    username = input("Please, write your name: ")
    bid = int(input("Write your bid ($): "))
    bids[username] = bid
    another_bid = input("Is there another person to bid? Type 'yes' or 'no': ")
    clear()
    if another_bid == "no":
        break

biggest_bid_username = max(bids)
print(
    f"{biggest_bid_username} won with bid of {bids[biggest_bid_username]}$ !")
