class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        print(f'first_name: {self.first_name.title()}\nlast_name: {self.last_name.title()}')
    
    def greet_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()}, good morning!")

user0 = User('zg', 'g')
user0.describe_user()
user0.greet_user()

user1 = User('jb', 'j')
user1.describe_user()
user1.greet_user()

user2 = User('tl', 'z')
user2.describe_user()
user2.greet_user()