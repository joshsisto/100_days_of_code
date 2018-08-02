

def staircase(n):
    for stairs in range(1, n + 1):
        # print(stairs)
        print(" " * (n - stairs) + "#" * stairs)


# staircase(17)

l = [1, 2, 3, 4, 5]

def miniMaxSum(arr):
    s_list = sorted(arr)
    min_list = s_list[:4]
    max_list = s_list[-4:]
    print(sum(min_list), sum(max_list))
    # print(min_list)
    # print(max_list)


# miniMaxSum(l)

r_time = "07:05:45PM"

def timeConversion(s):
    if s.endswith("PM"):
        l2 = list(s[:2])
        l2 = ''.join(l2)
        l2 = int(l2)
        new24 = l2 + 12
        new_time = list(s[2:-2])
        new_time.insert(0, new24)
        time_24 = "".join(str(new_time))
        print("".join(map(str, time_24)).strip('[]').replace(',', '').replace(' ', '').replace("'", ""))


# timeConversion(r_time)


new_l = [1, 2, 3]

print(sum(new_l))


