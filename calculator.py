def add(num1, num2):
    """Addition function that takes in two parameters and
     returns the sum of both numbers."""
    return num1 + num2


def subtract(num1, num2):
    """Subtract function that takes in two numbers and
     returns the subtraction value"""
    return num1 - num2


def multiply(num1, num2):
    """Multiply function that takes in two numbers and
         returns the multiplication of both values"""
    return num1 * num2


def divide(num1, num2):
    """Division function that takes in two numbers and
         returns the division of the values"""
    return num1 / num2


operations = {
    "+": "addition",
    "-": "subtraction",
    "*": "multiplication",
    "/": "division",
}
num1 = int(input("Whats the first number?: "))
num2 = int(input("Whats the second number?: "))


for operation in operations:
    print(operation)

operation_symbol = input("Pick an operation symbol from the line above: ")

if operation_symbol == "+":
    answer = num1 + num2
elif operation_symbol == "-":
    answer = num1 - num2
elif operation_symbol == "*":
    answer = num1 * num2
elif operation_symbol == "/":
    answer = num1 / num2


print(f"{num1} {operation_symbol} {num2} = {answer}")

num3 = int(input("What's the next number?: "))
operation_symbol = input("Pick an operation symbol from the line above: ")
if operation_symbol == "+":
    new_answer = answer + num3
elif operation_symbol == "-":
    new_answer = answer - num3
elif operation_symbol == "*":
    new_answer = answer * num3
elif operation_symbol == "/":
    new_answer = answer / num3

print(f"{answer} {operation_symbol} {num3} = {new_answer}")


