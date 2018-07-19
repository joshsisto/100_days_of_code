from functools import wraps
import time


def mydecorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # do something before the original function is called
        # call the passed in function
        result = function(*args, **kwargs)
        # do something after the original function call
        return result
    # return wrapper = decorated function
    return wrapper


@mydecorator
def my_function(args):
    pass


def get_profile(name, active=True, *sports, **awards):
    print('Positional arguments (required): ', name)
    print('Keyword arguments (not required, default values): ', active)
    print('Arbitrary argument list (sports): ', sports)
    print('Arbitrary keyword argument dictionary (awards): ', awards)


# get_profile() # this would cause error because it is missing argument

# get_profile('josh')
#
# get_profile('josh', active=False)
#
# get_profile('julian', False, 'basketball', 'soccer')
#
# get_profile('Cameron', False, 'basketball', 'soccer',
#             pythonista='special honor of the community', topcoder='2017 code camp')


def show_args(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print('hi from decorator - args:')
        print(args)
        result = function(*args, **kwargs)
        print('hi again from decorator - kwargs:')
        print(kwargs)
        return result
    # return wrapper as a decorated function
    return wrapper


@show_args
def get_profile(name, active=True, *sports, **awards):
    print('\n\thi from the get_profile function\n')


get_profile('bob', True, 'basketball', 'soccer',
            pythonista='special honor of the community', topcoder='2017 code camp')


def timeit(func):
    '''Decorator to time a function'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        # before calling the decorated function
        print('== starting timer')
        start = time.time()

        # call the decorated function
        func(*args, **kwargs)

        # after calling the decorated function
        end = time.time()
        print(f'== {func.__name__} took {int(end-start)} seconds to complete')

    return wrapper


def generate_report():
    '''Function to generate revenue report'''
    time.sleep(2)
    print('(actual function) Done, report links ...')


# generate_report()


@timeit
def generate_report2():
    '''Function to generate revenue report'''
    time.sleep(2)
    print('(actual function) Done, report links ...')


# generate_report2()

# print(generate_report2.__doc__)


def print_args(func):
    '''Decorator to print function arguments'''

    @wraps(func)
    def wrapper(*args, **kwargs):

        # before
        print()
        print('*** args:')
        for arg in args:
            print(f'- {arg}')

        print('**** kwargs:')
        for k, v in kwargs.items():
            print(f'- {k}: {v}')
        print()

        # call func
        func(*args, **kwargs)

    return wrapper


# def generate_report2(*months, **parameters):
#     time.sleep(2)
#     print('(actual function) Done, report links ...')


@timeit
@print_args
def generate_report2(*months, **parameters):
    time.sleep(2)
    print('(actual function) Done, report links ...')


parameters = dict(split_geos=True, include_suborgs=False, tax_rate=33)

# generate_report2('October', 'November', 'December', **parameters)

