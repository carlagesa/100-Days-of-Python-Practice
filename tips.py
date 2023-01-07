import random
#
# random_side = random.randint(0, 1)
# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails")

# state_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia",
#                     "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia"]
# print(state_of_america[-1])

names_string = input("Give me everybody's names, separated by a comma.")
names = names_string.split(", ")
# random_name = names.random()

person_who_will_pay = random.choice(names)
print(f"{person_who_will_pay} is going to buy the meal today!")