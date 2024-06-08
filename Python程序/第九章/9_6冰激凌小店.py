class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    
    def describe_restaurant(self):
        print(f"restaurant_name: {self.restaurant_name}\ncuisine_type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print("The restaurant is open!")
    


class IceCreamStand(Restaurant):
    def __init__(self):
        super().__init__('gzg', 'sa')
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'matcha']

    def show_favors(self):
        print('There are several flavors of ice cream:', end='')
        for flavor in self.flavors:
            print(' ', flavor, end='')
        print('.')

icecream_stand = IceCreamStand()

icecream_stand.show_favors()