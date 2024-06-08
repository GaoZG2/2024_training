from random import randint
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

die = Die()
for i in range(1, 11):
    print(die.roll_die())

die1 = Die(10)
for i in range(1, 11):
    print(die1.roll_die())

die2 = Die(20)
for i in range(1, 11):
    print(die2.roll_die())