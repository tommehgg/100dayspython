# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = float(weight) / float(height) ** 2
bmi_int = int(bmi)
bmi_converted = "{:.0f}".format(bmi)
if bmi <= 18.5:
    print("Your BMI is " + bmi_converted + ", you are underweight.")
if bmi >= 18.5:
    if bmi <= 25:
        print("Your BMI is " + bmi_converted + ", you have a normal weight.")
if bmi >= 25:
    if bmi <= 30:
        print("Your BMI is " + bmi_converted + ", you are slightly overweight.")
if bmi >= 30:
    if bmi <= 35:
        print("Your BMI is " + bmi_converted + ", you are obese.")
if bmi >= 35:
    print("Your BMI is " + bmi_converted + ", you are clinically obese.")