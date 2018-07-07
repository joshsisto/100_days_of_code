
# https://codechalleng.es/bites/5/
NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    names = (set(names))
    title_names = [name.title() for name in names]
    return title_names


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    split_list = []
    new_list = []
    for name in names:
        split_list.append(name.split())
        # print(name)
    split_list.sort(key=lambda x: x[1])
    for name in split_list:
        new_list.append(" ".join(name))
    new_list = reversed(new_list)
    return list(new_list)


def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    names = dedup_and_title_case_names(names)
    split_list = []
    first_names = []
    for name in names:
        split_list.append(name.split())
    for first, last in split_list:
        first_names.append(first)
    first_names.sort(key=len)
    return first_names[0]


# print(dedup_and_title_case_names(NAMES))
# print(sort_by_surname_desc(NAMES))
# print(shortest_first_name(NAMES))


# Solutions for first exercise
def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    return list({name.title() for name in names})


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    return sorted(names,
                  key=lambda x: x.split()[-1],
                  reverse=True)


def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    names = dedup_and_title_case_names(names)
    names = [name.split()[0] for name in names]
    return min(names, key=len)


# https://codechalleng.es/bites/promo/awesome-dict-comprehensions
bites = {6: 'PyBites Die Hard',
         7: 'Parsing dates from logs',
         9: 'Palindromes',
         10: 'Practice exceptions',
         11: 'Enrich a class with dunder methods',
         12: 'Write a user validation function',
         13: 'Convert dict in namedtuple/json',
         14: 'Generate a table of n sequences',
         15: 'Enumerate 2 sequences',
         16: 'Special PyBites date generator',
         17: 'Form teams from a group of friends',
         18: 'Find the most common word',
         19: 'Write a simple property',
         20: 'Write a context manager',
         21: 'Query a nested data structure'}
exclude_bites = {6, 10, 16, 18, 21}


def filter_bites(bites=bites, bites_done=exclude_bites):
    """return the bites dict with the exclude_bites filtered out"""
    for key, value in list(bites.items()):
        if key in bites_done:
            del bites[key]
    return bites


print(filter_bites())

# Solution
def filter_bites(bites=bites, bites_done=exclude_bites):
    """return the bites dict with the exclude_bites filtered out"""
    return {k: v for k, v in bites.items() if k not in bites_done}


# https://codechalleng.es/challenges/11/
