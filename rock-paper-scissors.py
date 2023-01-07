rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choice = input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.\n")
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissors)

computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}")