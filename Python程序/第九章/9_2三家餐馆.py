class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"restaurant_name: {self.restaurant_name}\ncuisine_type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print("The restaurant is open!")

restaurant = Restaurant('jjb', 'sa')
restaurant.describe_restaurant()

restaurant1 = Restaurant('gzg', 'qi')
restaurant1.describe_restaurant()

restaurant2 = Restaurant('ztl', 'lo')
restaurant2.describe_restaurant()