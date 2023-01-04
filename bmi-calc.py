weight = int(input("enter your weight in kg "))
height = float(input("enter your height inn m:")) ** 2 
bmi = round(weight / height)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are slightly underweight.")
elif bmi > 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}, you have normal weight.")
elif bmi > 25 and bmi < 30:
    print(f"Your BMI is {bmi}, you are overweight.")
elif bmi > 30 and bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
