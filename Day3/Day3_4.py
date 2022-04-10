year = input("What year do you want to check? ")
year_int = int(year)
if year_int % 4 == 0:
    if year_int % 100 == 0:
        if year_int % 400 == 0:
            print("Leap year.")
        else:
            print("not a leap year.")
    else:
        print("Not a leap year.")
else: 
    print("Not leap year.")