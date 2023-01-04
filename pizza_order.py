print("Welcome to Pizza Python Deliveries!")
size = input("What size pizza do yo want? S, M or L")
add_pepperoni =  input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")
price = 0
if size == "S":
    price += 15
elif size == "M":
    price += 20
else:
    price += 25
# This if elif statement checks for the size of the pizza and ingredients.
if size == "S" and add_pepperoni == "Y":
    price += 2
elif size == "M" or size == "L" and add_pepperoni == "Y":
    price += 3
else:
    price

# If statement to check whether customer wants extra cheese on pizza.
if extra_cheese == "Y":
    price += 1
else:
    price
print(f"Your final bill is: ${price}. A python will arrive with the pizza shortly!")
