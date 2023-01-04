print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad. Where do you want to go? "left" or "right"').lower()
if choice1 == "left":
    choice2 = input("You come to a lake. There is an island in the middle of the lake"
                    'Type wait to "wait" for a boat. Type "swim" to swim across.')
    if choice2 == "wait":
        choice3 = input("You arrive at an island unharmed. There is a house with 3 doors"
                        "One red, one yellow and one blue."
                        "Which color do you choose?").lower()
        if choice3 == "red":
            print("You enter a room full of fire. Game over!")
        elif choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game over!")
        else:
            print("The door you chose is from a different dimension. Game over!")
    else:
        print("You got attacked by an agry trout. Game over")
else:
    print("You fell into a hole. Game over!")
