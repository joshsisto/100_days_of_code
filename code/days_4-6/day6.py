from collections import defaultdict, namedtuple, Counter, deque
import csv
import collections

Player = collections.namedtuple('Players', 'player, team, position, height, weight, age, pc')

baseball_csv = './baseball.csv'
fifa_csv = './fifa.csv'



def get_player_stats(path):
    with open(path, encoding='utf-8') as f:
        reader = csv.DictReader(f)

        player_dict = collections.defaultdict(list)
        for line in reader:
            try:
                player = line['Name']
                team = line['Team']
                position = line['Position']
                height = line['Height']
                weight = line['Weight']
                age = line['Age']
                pc = line['PosCategory']
            except ValueError:
                continue

            p = Player(player=player, team=team, position=position, height=height, weight=weight, age=age, pc=pc)
            player_dict[player].append(p)

        return player_dict


print(get_player_stats(baseball_csv))

