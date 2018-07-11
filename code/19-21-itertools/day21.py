# https://codechalleng.es/bites/promo/itertools-fun3
# https://codechalleng.es/bites/promo/itertools-fun2
# https://codechalleng.es/bites/promo/itertools-fun1

import itertools

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US'.split()
confirmed = [False, True, True, False, True]


def get_attendees():
    for participant in itertools.zip_longest(names, locations, confirmed, fillvalue='-'):
        # print(participant[0])
        # print(participant[1])
        # print(participant[2])
        print(participant)


if __name__ == '__main__':
    get_attendees()


import itertools
import os
import urllib.request


# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])



def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    pass

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    pass
