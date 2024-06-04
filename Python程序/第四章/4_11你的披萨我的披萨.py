pizzas = ['p1', 'p2', 'p3']
for pizza in pizzas:
    print(f'I like {pizza}')
print('I really love pizza!')
friend_pizzas = pizzas[:]
friend_pizzas.append('pa')
pizzas.append('pb')
print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)