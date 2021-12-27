height = int(input("Please enter your height in inches: "))
age    = int(input("Please enter your age in years: "))

can_ride_rollercoaster = height > 48 and age >= 10

if can_ride_rollercoaster:
    print("Welcome aboard the Iron Dragon")

    print("Please keep your hands an feed inside the coaster at all times")
else:
    print("Sorry, but you cannot ride this ride")
    if height <= 48 and age < 10:
        print("Please visit the kids park by the food court")
    elif height <= 48:
        print("You are too short to be safe on this ride")
    elif age < 10:
        print("You are too young to ride this ride")
    else:
        print("Something went wrong...")
