from collections import Counter
import calendar
import itertools
import random
import re
import string

import requests
import IPython

print(IPython.extract_module_locals())


names = 'pybites mike bob julian tim sara guido'.split()
for name in names:
    print(name.title())

first_half_alphabet = list(string.ascii_lowercase)[:13]
# print(first_half_alphabet)

# print(string.__all__) # shows methods for string


# this example is how I would normally take care of a task like this
new_names = []
for name in names:
    if name[0] in first_half_alphabet:
        new_names.append(name.title())
print(new_names)
# list comprehension that does the same as the code above
new_names2 = [name.title() for name in names if name[0] in first_half_alphabet]
print(new_names2)
# a small example leading up to the code above
print([name for name in names])     # notice how this line does the same as lines 12-13
assert new_names == new_names2

# load in harry potter
resp = requests.get('http://projects.bobbelderbos.com/pcc/harry.txt')
words = resp.text.lower().split()
print(words[:5])

cnt = Counter(words)
print(cnt.most_common(5))
print('-' in words)
print(len(words))

new_words = [re.sub(r'\W+', r'', word) for word in words]
print('-' in new_words)
print('the' in new_words)
print(len(new_words))


resp = requests.get('http://projects.bobbelderbos.com/pcc/stopwords.txt')
stopwords = resp.text.lower().split()
print(stopwords[:5])


newer_words = [word for word in words if word.strip() and word not in stopwords]
print(newer_words[:5])
print('the' in newer_words)

new_cnt = Counter(newer_words)
print(new_cnt.most_common(5))


# Generators
def num_gen():
    for i in range(5):
        yield i


gen = num_gen()
print(next(gen))

for i in gen:
    print(i)

# print(next(gen)) # we have exhausted the sequence this will cause error if not commented out

options = 'red yellow blue white black green purple'.split()
print(options)


# old code example
def create_select_options(options=options):
    select_list = []

    for option in options:
        select_list.append(f'<option value={option}>{option.title()}</option>')

    return select_list


from pprint import pprint as pp
pp(create_select_options())


# Same code using generator
def create_select_options_gen(options=options):
    for option in options:
        yield f'<option value={option}>{option.title()}</option>'


print(create_select_options_gen())  # prints the object
print(list(create_select_options_gen()))  # prints list showing all items of generator


# Leap year
# list
def leap_years_lst(n=10000000):
    leap_years = []
    for year in range(1, n+1):
        if calendar.isleap(year):
            leap_years.append(year)
    return leap_years


# generator
def leap_years_gen(n=10000000):
    for year in range(1, n+1):
        if calendar.isleap(year):
            yield year


print(leap_years_lst())
print(leap_years_gen())
print(list(leap_years_gen()))
assert leap_years_lst() == list(leap_years_gen())


# %timeit -n1 leap_years_lst()  # unable to use this code. instead use the clock in the top right.


