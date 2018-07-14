# https://codechalleng.es/bites/65/

import itertools
import os
import urllib.request
import random
import string

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    permutations = [''.join(word).lower()
                    for word in _get_permutations_draw(draw)]
    return set(permutations) & set(dictionary)


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    for i in range(1, 8):
        yield from list(itertools.permutations(draw, i))


def random_letter():
    alpha = list(string.ascii_lowercase)
    random_letter = random.choice(alpha)
    return random_letter


random_list = []

for _ in range(7):
    random_list.append(random_letter())
print(random_list)

# print(get_possible_dict_words(random_list))list(get_possible_dict_words(aj_list)))
# print(list(_get_permutations_draw(random_list)))
my_words = 'i o l t p r l'.split()


def my_word_combos(my_words=my_words):
    word_options = list(get_possible_dict_words(my_words))
    sorted_list = sorted(word_options, key=len, reverse=True)
    return sorted_list


# print(my_word_combos())

board_words = ['wank', 'armor', 'car', 'travel', 'foil', 'iron']

combined_words = my_words + board_words

print(my_word_combos(combined_words))

# print(get_possible_dict_words(combined_words))

