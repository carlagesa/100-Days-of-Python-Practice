print('Welcome to our rollercoaster!')
height = int(input('What is your height?cm'))
if height >= 120:
    print('Climb aboard mate!')
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print('Barnicles! Me little shortstick cannot ride')