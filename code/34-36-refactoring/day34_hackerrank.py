



l = [4, 3, 8, 1]


def reverseArray(a):
    r_list = a
    r_list.reverse()
    return r_list


reverseArray(l)


def is_leap(year):
    leap = False

    if year % 4 == 0:
        leap = True
    if year % 400 == 0:
        leap = True
    if year % 100 == 0:
        leap = False

    return leap


print(is_leap(2000))


def range_rover(n):
    l = []
    for num in range(1, n+1):
        l.append(num)
    print(*l, sep="")


range_rover(3)


def count_substring(string, sub_string):
    print(string.count(sub_string))
    return


count_substring("ABCDCCDC", "CDC")









