from random import randint


class Die():
    def __init__(self, sides=6):
        """based cube"""
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)
