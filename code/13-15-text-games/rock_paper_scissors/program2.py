import random
from player_move import Player, Roll


outcomes = ["rock", "paper", "scissors"]


def main():
    print_header()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)

def build_the_three_rolls():
    rolls_list = []
    for _ in range(3):
        roll = random.choice(outcomes)
        rolls_list.append(roll)
    return rolls_list


def choose_RPS():
    choice = input("[r]ock [p]aper [s]cissors\n")
    if choice == "r":
        print("you chose rock")
        return "rock"
    elif choice == "p":
        print("you chose paper")
        return "paper"
    elif choice == "s":
        print("you chose scissors")
        return "scissors"
    else:
        print("You didn't choose r or p or s")
        choose_RPS()



def print_header():
    print('---------------------------------')
    print('      Rock Paper Scissors')
    print('---------------------------------')
    print()


def get_players_name():
    name = input("Type in your name\n")
    return name


def game_loop(player1, player2, rolls):
    # print(player1)
    # print(player2)
    # print(rolls)
    count = 0
    while count < 3:
        p2_roll = player2.random_roll
        print(p2_roll)
        p1_roll = choose_RPS()

        # outcome = p1_roll.can_defeat(p2_roll)

        # display throws
        # display winner for this round

        count += 1


if __name__ == '__main__':
    main()

