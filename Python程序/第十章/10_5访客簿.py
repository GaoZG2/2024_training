with open('guest_book.txt', 'a') as file:
    while True:
        name = input("Please input your name (or input 'quit' to exit): ")
        if name == 'quit':
            break
        file.write(f'{name.title()}\n')
