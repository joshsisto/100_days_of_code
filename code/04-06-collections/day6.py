from collections import defaultdict, namedtuple, Counter, deque
import csv
import collections

Player = collections.namedtuple('Stats', 'player, team, position, height, weight, age, pc')

baseball_csv = './baseball.csv'
fifa_csv = './fifa.csv'



def get_baseball_stats(path=baseball_csv):
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


# print(get_baseball_stats(baseball_csv))

get_player_stat = get_baseball_stats()

ryan = (get_player_stat['Ryan_Sweeney'])
ryan = ryan[0]
print(ryan.height)

cnt = Counter()
for player, item in get_player_stat.items():
    # cnt[director] += len(movies)
    print(player.replace('_', ' '))
    item = item[0]
    print(item.height)



