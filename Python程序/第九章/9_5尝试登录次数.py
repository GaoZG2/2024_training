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

user0 = User('zg', 'g')
user0.increment_login_attempts()
user0.increment_login_attempts()
user0.increment_login_attempts()
print(user0.login_attempts)

user0.reset_login_attempts()
print(user0.login_attempts)