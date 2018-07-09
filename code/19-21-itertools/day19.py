number = list(range(1, 11))

print(number)

for i in number:
    print(i)

print('__iter__' in dir("number"))

it = iter('string')

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))  # This will cause error because it can't be iterated on again

import itertools
import sys
import time

symbols = itertools.cycle('-\|/')

# while True:
#     sys.stdout.write('\r' + next(symbols))
#     sys.stdout.flush()
#     time.sleep(1)


from itertools import product

name = 'joshua'

for letter in product(name, repeat=1):
    print(letter)

for letter in product(name, repeat=5):
    print(letter)


from itertools import permutations, combinations

friends = 'mike bob julian'.split()
print(list(combinations(friends, 2)))

