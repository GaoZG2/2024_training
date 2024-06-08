from user import User

class Privilege:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print('Your privileges are as follows: ')
        print(self.privileges)

class Admin:
    def __init__(self):
        self.privileges = Privilege()