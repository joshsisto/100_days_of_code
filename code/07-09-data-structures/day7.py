

mystring = "josh"

## Lists
l = list(mystring)
print(l)

l.reverse()
print(l)

l.pop()
print(l)

l = list(mystring)
l[0] = l[0].upper()
print(l)

l.append("u"), l.append("a")
print(l)

l.insert(0, "j")
print(l)

## Dicts

people = {'Josh': 29, 'Raf': 50, 'Jafar': 3}
print(people)
print(people['Josh'])

people['Julian'] = 30
print(people)

print(people.keys())
print(people.values())
print(people.items())

for keys, values in people.items():
    # print(keys + str(values))
    print(f'{keys} is {values} years old')


