try:
    num1 = input("Please enter the first number: ")
    num2 = input("Please enter the second number: ")

    num1 = int(num1)
    num2 = int(num2)

    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}")

except ValueError:
    print("Error: Please make sure you enter two valid integers.")