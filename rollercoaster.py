print('Welcome to our rollercoaster!')
height = int(input('What is your height?cm'))
bill = 0
if height >= 120:
    print('Climb aboard mate!')
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Children tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo take? Y or N.")
    if wants_photo == "Y":
        print(f"Your total bill is ${bill + 3}")
    else:
        print(f"Your total bill is ${bill}.")

else:
    print('Barnacles! Me little shortstick cannot ride')