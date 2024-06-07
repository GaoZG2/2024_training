places = []
while True:
    place = input('If you could visit one place in the world, where would you go?')
    if place == 'quit':
        break
    else:
        places.append(place)
print(places)