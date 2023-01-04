age = input('what is your current age?')
max_age = 90
age_left = int(max_age) - int(age)
age_left_in_days = age_left * 365
age_left_in_weeks = age_left * 52
age_left_in_months = age_left * 12
print(f'You have {age_left_in_days} days, {age_left_in_weeks} weeks, and {age_left_in_months} months left.')