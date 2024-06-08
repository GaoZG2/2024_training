class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def describe_user(self):
        print(f'first_name: {self.first_name.title()}\nlast_name: {self.last_name.title()}')
    
    def greet_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()}, good morning!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self):
        super().__init__('zg', 'g')
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
        print('Your privileges are as follows: ')
        print(self.privileges)

admin = Admin()
admin.show_privileges()