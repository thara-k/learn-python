def add_two_numbers(leftSide, rightSide):
    result = leftSide + rightSide
    return result
    

for i in range(1):
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter another number: "))

    answer = add_two_numbers(num1, num2)
    print("The result of your math is: ", answer)