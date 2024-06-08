class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"restaurant_name: {self.restaurant_name}\ncuisine_type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print("The restaurant is open!")

    def set_number_served(self, new_num):
        self.number_served = new_num
    
    def increment_number_served(self, add_num):
        self.number_served += add_num

restaurant = Restaurant('gzg', 'sa')

print(f'How many people have eaten in this restaurant: {restaurant.number_served}')

restaurant.number_served = 102
print(f'How many people have eaten in this restaurant: {restaurant.number_served}')

restaurant.set_number_served(29)
print(f'How many people have eaten in this restaurant: {restaurant.number_served}')

restaurant.increment_number_served(10)
print(f'How many people have eaten in this restaurant: {restaurant.number_served}')