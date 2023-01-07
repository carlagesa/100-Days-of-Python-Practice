def prime_checker(number):
    if number % 2 == 0:
        print("It is not a prime number")

    elif number % 1 == 0 and number % number == 0:
        print("It is a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
