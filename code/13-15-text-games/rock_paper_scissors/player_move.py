import random


outcomes = ["rock", "paper", "scissors"]


class Player:
    def __init__(self, name):
        self.name = name
        print(name)

    def random_roll(self):
        roll = random.choice(outcomes)
        print(roll)
        return roll


class Roll:
    def __init__(self, roll):
        self.roll = roll
        if self.roll not in outcomes:
            self.roll = random.choice(outcomes)


    # def name_of_roll(self):

