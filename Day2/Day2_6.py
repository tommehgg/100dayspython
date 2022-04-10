#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total_price = input("What was the total price of the food? €")
amount_people = input("How many people did you eat food with? ")
tip = input("What tip would you like to give? ")

total_price_tip = float(total_price) * (float(tip) / 100) + float(total_price)

final_price = total_price_tip / int(amount_people)
final_price_coverted = "{:.2f}".format(final_price)

print("Each person should pay: " + "€" + final_price_coverted)