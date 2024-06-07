while True:
    age = input("What's your age?")
    age = int(age)
    if age < 0 or age > 150:
        print("Input error!")
    elif age < 3:
        print("Your ticket is free.")
    elif age < 12:
        print("Your ticket price is 10 dollars.")
    else:
        print("Your ticket price is 15 dollars.")