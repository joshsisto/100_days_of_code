import re

text = 'Awesome, I am doing the #100DaysOfCode challenge'

if text.startswith("Awesome") == True and text.endswith("challenge") == True:
    print("the variable text starts with Awesome and ends with challenge")

if '100daysofcode' in text.lower():
    print("do Something")

updated_text = text.replace('100', '200')
print(updated_text)

new_text = 'Awesome, I am doing the #100DaysOfCode challenge'

print(re.search(r'I am', new_text))

print(re.match(r'I am', new_text))

print(re.match(r'Awesome.*challenge', text))


hundred = 'Awesome, I am doing the #100DaysOfCode challenge'
two_hundred = 'Awesome, I am doing the #200DaysOfCode challenge'

m = re.match(r'.*(#\d+DaysOfCode).*', hundred)
print(m.groups()[0])

m = re.search(r'(#\d+DaysOfCode)', two_hundred)
print(m.groups()[0])

output_text = '''
$ python module_index.py |grep ^re
re                 | stdlib | 005, 007, 009, 015, 021, 022, 068, 080, 081, 086, 095
'''

print(re.findall(r'\d+', output_text))

generic_text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum"""

print(generic_text.split())

from collections import Counter

cnt = Counter(re.findall(r'[A-Z][a-z0-9]+', generic_text))
print(cnt.most_common(5))


# Grabbing all movies with 2 words in the title
movies = '''1. Citizen Kane (1941)
2. The Godfather (1972)
3. Casablanca (1942)
4. Raging Bull (1980)
5. Singin' in the Rain (1952)
6. Gone with the Wind (1939)
7. Lawrence of Arabia (1962)
8. Schindler's List (1993)
9. Vertigo (1958)
10. The Wizard of Oz (1939)'''.split('\n')

pat = re.compile(r'''
                  ^             # start of string
                  \d+           # one or more digits
                  \.            # a literal dot
                  \s+           # one or more spaces
                  (?:           # non-capturing parenthesis, so I don't want store this match in groups()
                  [A-Za-z']+\s  # character class (note inclusion of ' for "Schindler's"), followed by a space
                  )             # closing of non-capturing parenthesis
                  {2}           # exactly 2 of the previously grouped subpattern
                  \(            # literal opening parenthesis
                  \d{4}         # exactly 4 digits (year)
                  \)            # literal closing parenthesis
                  $             # end of string
                  ''', re.VERBOSE)

for movie in movies:
    print(movie, pat.match(movie))


days_text = '''Awesome, I am doing #100DaysOfCode, #200DaysOfDjango and of course #365DaysOfPyBites'''

# I want all challenges to be 100 days, I need a break!
print(days_text.replace('200', '100').replace('365', '100'))
# Same as above but using re.sub
print(re.sub(r'\d+', '100', days_text))
# Change hashtags to DaysofPython
print(re.sub(r'(#\d+DaysOf)\w+', r'\1Python', days_text))

# Day 29
bite_text = 'regexes are powerful but use with care, some more text, lets play!'
# Overkill
print(re.sub(r'some', 'a bit', bite_text))
print(re.match(r'^regex', bite_text))

# Instead use this
print(bite_text.replace('some', 'a bit'))

if bite_text.startswith('regex'):
    print('that line starts with regex')

# re.match() vs re.search()
match_text = 'Use match vs search appropriately'
# Do this
print(re.match('search', match_text))
# Don't do this
print(re.match('.*search', match_text))
# Better
print(re.search('search', match_text))

# Non capture parenthesis
tweet = 'New PyBites article: Module of the Week - Requests-cache for Repeated API Calls - http://pybit.es/requests-cache.html … #python #APIs'
print(re.findall(r'((?:#|http)\S+)', tweet))
# When we don't use (?:) it goes wrong
print(re.findall(r'((#|http)\S+)', tweet))

# HTML
html = """<div><p>Today a quick article on a nice caching module when working with APIs.</p><p>Read more ...</p></div>"""
m = re.search('<p>.*</p>', html)    # This grabs too much
print(m.group())
m2 = re.search('<p>.*?</p>', html)  # This grabs what we want (notice the ?)
print(m2.group())

# Backreferences
p = re.compile(r'(\b\w+)\s+\1')
p2 = p.search('Paris in the the spring').group()
print(p2)


def search_file(file):
    file_content = open(file).read()  # should have used with
    time_regex = re.compile(r'\(\d+:\d+\)')  # seems we needed literal parenthesis as part of the match
    return time_regex.findall(file_content)




