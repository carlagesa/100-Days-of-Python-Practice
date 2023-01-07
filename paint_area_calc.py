# def greet(first, last):
#     print(f"Good morning!{first}")
#     print(f"Good afternoon!{last}")
#     print(f"Good evening!{first}")
#
#
# greet("carl", "agesa")
import math


def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    whole_number_of_cans = math.ceil(number_of_cans)
    print(f"You'll need {whole_number_of_cans} cans of paint")


test_h = int(input("Height of wall:"))
test_w = int(input("Width of wall:"))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)

