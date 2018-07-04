import random


outcomes = ["rock", "paper", "scissors"]


class Player:
    def __init__(self, name):
        self.name = name
        print(name)


class Roll(Player):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def random_roll(self):
        roll = random.choice(outcomes)
        print(roll)
        return roll