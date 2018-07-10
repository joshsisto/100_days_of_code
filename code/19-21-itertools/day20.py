from time import sleep
import itertools
import random

colors = 'Red Green Amber'.split()
rotation = itertools.cycle(colors)


def rg_timer():
    return random.randint(3, 7)

def light_rotation(rotation):
    for color in rotation:
        if color == 'Amber':
            print('Caution! The light is {}'.format(color))
            sleep(3)
        elif color == "Red":
            print('STOP! The light is {}'.format(color))
            sleep(rg_timer())
        else:
            print('Go! The light is {}'.format(color))
            sleep(rg_timer())


if __name__ == '__main__':
    light_rotation(rotation)