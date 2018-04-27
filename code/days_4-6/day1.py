from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve


# namedtuple
user1 = ('bob', 'coder')

print(f'{user1[0]} is a {user1[1]}')


User = namedtuple('User', 'name role')

user2 = User(name='bob', role='coder')

print(user2.name, user2.role)

print(f'{user2.name} is a {user2.role}')

# defaultdict
users_d = {'bob': 'coder'}

print(users_d['bob'])

print(users_d.get('bob'))


challenges_done = [('mike', 10), ('julian', 7), ('bob', 5),
                   ('mike', 11), ('julian', 8), ('bob', 6)]
print(challenges_done)


challenges = defaultdict(list)
for name, challenge in challenges_done:
    challenges[name].append(challenge)

print(challenges)


words = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum""".split()
print(words[:5])

common_words = {}

for word in words:
    if word not in common_words:
        common_words[word] = 0
    common_words[word] += 1

# sort dict by values descending and slice first 5 to get most common
for k, v in sorted(common_words.items(),
                   key=lambda x: x[1],
                   reverse=True)[:5]:
    print(k ,v)

print(Counter(words).most_common(5))


lst = list(range(10000000))
deq = deque(range(10000000))


def insert_and_delete(ds):
    for _ in range(10):
        index = random.choice(range(100))
        ds.remove(index)
        ds.insert(index, index)














