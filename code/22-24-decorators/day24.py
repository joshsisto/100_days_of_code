# https://codechalleng.es/bites/22/
# https://codechalleng.es/challenges/14/
# https://dbader.org/blog/python-decorators
# https://dbader.org/blog/python-first-class-functions


from functools import wraps


def make_html(element):
    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{element}>{func(*args, **kwargs)}</{element}>'
        return wrapper
    return real_decorator


@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text


# print(get_text())


def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


@uppercase
def greet():
    return 'Hello!'


# print(greet())
# print(greet)
# print(uppercase(greet))
# print(greet.__name__)
# print(greet.__doc__)


def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper


def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper


@strong
@emphasis
def greet():
    return 'Hello!'


# print(greet())


def proxy(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
              f'with {args}, {kwargs}')

        original_result = func(*args, **kwargs)

        print(f'TRACE: {func.__name__}() '
              f'returned {original_result!r}')

        return original_result
    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


print(say('Josh', 'Hello, World'))


def uppercase(func):
    @wraps(func)
    def wrapper():
        return func().upper()
    return wrapper


@uppercase
def greet():
    """Return a friendly greeting"""
    return "Hello!"


print(greet.__name__)
print(greet.__doc__)

