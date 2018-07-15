# https://codechalleng.es/bites/65/
# Some of this code is from the Pybites challenge in the link above

import itertools
import os
import urllib.request
import random
import string

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://www-personal.umich.edu/~jlawler/wordlist', DICTIONARY)

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
    for i in range(1, 14):
        yield from list(itertools.permutations(draw, i))


def my_word_combos(letters):
    print('Searching over 69,000 words from http://www-personal.umich.edu/~jlawler/wordlist\n')
    word_options = list(get_possible_dict_words(letters))
    sorted_list = sorted(word_options, key=len, reverse=True)
    return sorted_list


def scrabble_helper():
    word_list = []
    my_letters = input("Add letter followed by a space\n e.g. y l n o p a u\n\n")
    # letters_plus = my_letters.split()
    # letters_plus.append(letter)
    combos = my_word_combos(my_letters.split())
    word_list.append(combos)
    print(sorted(combos, key=len, reverse=True))


while __name__ == "__main__":
    scrabble_helper()
