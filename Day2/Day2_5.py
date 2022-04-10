# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_new = 90 - int(age)
months = int(age_new) * 12
weeks = int(age_new) * 52
days = int(age_new) * 365
print(f"You have {days} days, {weeks} weeks, and {months} months left.")