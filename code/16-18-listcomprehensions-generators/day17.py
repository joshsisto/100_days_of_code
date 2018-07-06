import random
import itertools

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

# name_titles = [name.title() for name in name_list]


# title_names = []
#
#
# def titler(name_list=name_list):
#     for first, last in name_list:
#         fs_list = (first.title(), last.title())
#         title_names.append(fs_list)
#     return title_names
#
#
# titles = titler()
# print(titles[0])
#
# arnold = titles[0]
# print(arnold[0])

# new_names2 = [name.title() for name in names if name[0] in first_half_alphabet]

name_list = [name.title() for name in NAMES]
print(name_list)


def reverse_first_last_names(name):
    first, last = name.split()
    return f'{last} {first}'


print([reverse_first_last_names(name) for name in NAMES])


def gen_pairs():
    # again a list comprehension is great here to get the first names
    # and title case them in just 1 line of code (this comment took 2)
    first_names = [name.split()[0].title() for name in NAMES]
    while True:

        # added this when I saw Julian teaming up with Julian (always test your code!)
        first, second = None, None
        while first == second:
            first, second = random.sample(first_names, 2)

        yield f'{first} teams up with {second}'


pairs = gen_pairs()

for _ in range(10):
    print(next(pairs))

first_ten = itertools.islice(pairs, 10)
print(list(first_ten))


