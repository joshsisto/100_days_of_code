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

with open('dict.txt') as f:
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


def random_seven_letters():
    random_list = []
    for _ in range(7):
        random_list.append(random_letter())
    print(random_list)
    return random_list


def my_word_combos(letters):
    print('Searching over 69,000 words from http://www-personal.umich.edu/~jlawler/wordlist\n')
    word_options = list(get_possible_dict_words(letters))
    sorted_list = sorted(word_options, key=len, reverse=True)
    return sorted_list


def add_word():
    word = input('\nWhat word was added to the board?\n\n')
    board_words.append(word)
    print(board_words)


board_words = []
# board_words = ['vile', 'hiss', 'are', 'tweaks', 'digs', 'touche']
all_combos = []


def longest_word():
    my_letters = input("Put in your seven letters\n e.g. y l n o p a u\n\n")
    no_repeat = []
    for word in board_words:
        for letter in word:
            if letter not in no_repeat:
                no_repeat.append(letter)
                letters_plus = my_letters.split()
                letters_plus.append(letter)
                combos = my_word_combos(letters_plus)
                for word_dos in combos:
                    if word_dos not in all_combos:
                        all_combos.append(word_dos)
    print(sorted(all_combos, key=len, reverse=True))
    add_word()
    add_word()


while __name__ == "__main__":
    longest_word()
