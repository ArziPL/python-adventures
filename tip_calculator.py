# Day 2 - project 1
bill = float(input("What was the bill? $"))
tip_percent = float(input("What percentage tip would you like to give? %"))
people = float(input("How many people to split the bill? "))

final_bill = bill + (bill * (tip_percent / 100))
each_person_bill = round(final_bill / people, 2)

print(f"Each person should pay ${each_person_bill}")