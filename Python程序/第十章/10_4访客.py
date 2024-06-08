with open('guest.txt', 'a') as file:
    name = input("Please input your name: ")
    file.write(f'{name.title()}\n')
