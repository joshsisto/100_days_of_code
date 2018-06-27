import random


outcomes = ["rock", "paper", "scissors"]


class Player:
    def __init__(self, name):
        self.name = name
        print(name)


class Roll(Player):
    def __init__(self, name):
        super().__init__(name)

    def player_rolls(self, roll):


        print(roll)
        return roll
