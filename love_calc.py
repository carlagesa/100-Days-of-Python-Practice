print("Welcome to the love calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()
both_names = lowercase_name2 + lowercase_name1
t = both_names.count("t")
r = both_names.count("r")
u = both_names.count("u")
e = both_names.count("e")

true = t + r + u +e

l = both_names.count("l")
o = both_names.count("o")
v = both_names.count("v")
e = both_names.count("e")

love = l + o + v + e

lovers_score = int(str(true) + str(love))
if lovers_score < 10 or lovers_score > 90:
    print(f"Your love score is {lovers_score}, you look amazing together! ")
elif (lovers_score >= 40) and (lovers_score <= 50):
    print(f"Your love score is {lovers_score}, you are alright together.")
else:
    print(f"Your love score is {lovers_score}.")
# print(lovers_score)
