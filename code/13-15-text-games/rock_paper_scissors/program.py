import random
from player_move import Player


outcomes = ["rock", "paper", "scissors"]


def main():
    print_header()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    # game_loop(player1, player2, rolls)

def build_the_three_rolls():
    rolls_list = []
    roll = random.choice(outcomes)
    for _ in range(3):
        rolls_list.append(roll)
    return rolls_list



def print_header():
    print('---------------------------------')
    print('      Rock Paper Scissors')
    print('---------------------------------')
    print()


def get_players_name():
    name = input("Type in your name\n")
    return name


def game_loop(player1, player2, rolls):
    count = 1
    while count < 3:
        p2_roll = None # TODO: get random roll
        p1_roll = None # TODO: have player choose a roll

        # outcome = p1_roll.can_defeat(p2_roll)

        # display throws
        # display winner for this round

        # count += 1


if __name__ == '__main__':
    main()

