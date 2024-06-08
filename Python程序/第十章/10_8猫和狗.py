try:
    with open('cats.txt', 'r') as file1, open('dogs.txt', 'r') as file2:
        cats = file1.read().splitlines()
        dogs = file2.read().splitlines()

        print("The names of these cats are: ")
        for cat in cats:
            print(f' {cat}', end='')
        
        print("\nThe names of these dogs are: ")
        for dog in dogs:
            print(f' {dog}', end='')
except FileNotFoundError:
    print('Error: The file was not found!')

