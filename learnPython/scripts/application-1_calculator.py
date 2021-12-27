number_1 = float(input("Please enter your first number: "))
number_2 = float(input("Please enter your second number: "))

operator = input("What do you want to do? Add/subtract/multiply/divide/mod/power: ")

calculationSuccess = False

if operator.lower() == "add":
    result = number_1 + number_2
    calculationSuccess = True
elif operator.lower() == "subtract":
    result = number_1 - number_2
    calculationSuccess = True
elif operator.lower() == "multiply":
    result = number_1 * number_2
    calculationSuccess = True
elif operator.lower() == "divide":
    result = number_1 / number_2
    calculationSuccess = True
elif operator.lower() == "mod":
    result = number_1 % number_2
    calculationSuccess = True
elif operator.lower() == "power":
    result = number_1 ** number_2
    calculationSuccess = True
else:
    result = "Unknown operator"    
    calculationSuccess = False

if calculationSuccess:
    print("Your result: ", result)
else:
    print("There was an error:", result)