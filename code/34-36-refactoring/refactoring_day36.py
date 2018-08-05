# bad code
def get_workout(day):
    if day == 'Monday':
        return 'Chest+biceps'
    elif day == 'Tuesday':
        return 'Back+triceps'
    elif day == 'Wednesday':
        return 'Core'
    elif day == 'Thursday':
        return 'Legs'
    elif day == 'Friday':
        return 'Shoulders'
    elif day in ('Saturday', 'Sunday'):
        return 'Rest'
    raise ValueError('Not a day')


# instead use a dict

workouts = {
    'Monday': 'Chest+biceps',
    'Tuesday': 'Back+triceps',
    'Wednesday': 'Core',
    'Thursday': 'Legs',
    'Friday': 'Shoulders',
    'Saturday': 'Rest',
    'Sunday': 'Rest',
}
# print(workouts)

days = 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()
routines = 'Chest+biceps Back+triceps Core Legs Shoulders Rest Rest'.split()

workouts2 = dict(zip(days, routines))
# print(workouts2)


# much better than the first bit of code up top
def get_workout(day):
    routine = workouts.get(day)
    if routine is None:
        raise ValueError('Not a day')
    print(routine)
    return routine


get_workout("Monday")
# get_workout("nonsense")


### counting inside a loop

# example of how to count
i = 0
for day in days:
    i += 1
    print(f'{i}. {day}')

# better example using enumerate
for i, day in enumerate(days):
    print(f'{i + 1}. {day}')

# this example starts index at 1. Removes the need to do i + 1 manually in the example above
for i, day in enumerate(days, 1):
    print(f'{i}. {day}')

### use builtins

# sequence of numbers
numbers = range(1, 11)
print(list(numbers))

# sum of numbers
total = 0
for num in numbers:
    total += num
print(total)

routines = 'Chest+biceps Back+triceps Core Legs Shoulders'.split()
timings = '45 45 30 55 45'.split()

workout_times = dict(zip(routines, timings))

# we are going to return the max (longest) routine
max_routine = None
max_timing = 0
for routine, timing in workout_times.items():
    timing = int(timing)
    if timing > max_timing:
        max_routine = routine
        max_timing = timing
print(max_routine, max_timing)

# using max builtin
get_max_std = max(workout_times.items(), key=lambda x: x[1])
print(get_max_std)

get_min_std = min(workout_times.items(), key=lambda x: x[1])
print(get_min_std)

### tuple unpacking and namedtuples

# swap variables
a, b = 1, 2
a, b = b, a
print(a, b)

# from earlier example
routine, minutes = max(workout_times.items(), key=lambda x: x[1])
print(routine, minutes)

# cleaning up code using namedtuples
m_workout = ('Chest+biceps', 'Monday', 45)
print(f'On {m_workout[1]} I train {m_workout[0]} for {m_workout[2]} minutes')
# above example is hard to read

# using named tuple
from collections import namedtuple

Workout = namedtuple('Workout', 'routine day duration')

nt_workout = Workout(routine='Chest+biceps', day='Monday', duration=45)
print(f'On {nt_workout.day} I train {nt_workout.routine} for {nt_workout.duration} minutes')


# get days that start with T
def get_t_days(days=days):
    t_days = []
    for day in days:
        if day[0].lower() == 't':
            t_days.append(day)
    print(t_days)
    return t_days


get_t_days()


# alternatively we can use a list comprehension
def get_t_days(days=days):
    return [day for day in days if day[0].lower() == 't']


print(get_t_days())


# or we can use a generator
def get_t_days_gen(days=days):
    for day in days:
        if day[0].lower() == 't':
            yield day


print(list(get_t_days_gen()))

from random import choice


def get_random_day(days=days):
    i = 0
    while True:
        i += 1
        yield i, choice(days)


days_gen = get_random_day()
print(days_gen)
print(next(days_gen))
print(next(days_gen))

for _ in range(5):
    print(next(days_gen))

from itertools import islice

slice_ = islice(days_gen, 100, 110)
print(list(slice_))


### Exceptions
def calc_value_improved(num1, num2):
    try:
        ret = num1/num2
    except ZeroDivisionError:
        print('cannot divide by 0')
        return 0
    except TypeError:
        print('check if all input variables are int')
        raise
    except Exception as exc:
        print(f'other exception: {exc}, reraising')
        raise


calc_value_improved("l", 2)
calc_value_improved(2, 0)






