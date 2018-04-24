
# !/usr/bin/python

# pomodoro script by Oliver Kraitschy
# http://okraits.de okraits@arcor.de
# https://github.com/okraits/omodoro

from __future__ import print_function
from os import system, getenv
from datetime import datetime, timedelta
from time import sleep
from threading import Thread, Lock, ThreadError
from platform import system as platformname
from sys import argv, version_info
from os.path import exists, join

if version_info >= (3, 0):
    get_input = input
    from configparser import ConfigParser, NoOptionError
else:
    get_input = raw_input
    from ConfigParser import ConfigParser, NoOptionError
if platformname() == 'Windows':
    onWindows = True
else:
    onWindows = False

# SETTINGS
# adjust the pomodoro cycle to your needs
num_pomodori = 4  # number of pomodori to do in a cycle
length_pomodori = 25  # length of one pomodori in minutes
length_short_break = 5  # length of a short break in minutes
length_long_break = 15  # length of a long break in minutes
terminal_bell = False  # play the terminal bell at the begin of each pomodoro/break

# path to user-specific configuration file
if onWindows:
    conf_file = join(getenv("APPDATA"), "omodoro.conf")
else:
    conf_file = join(getenv("HOME"), ".omodoro.conf")


def printUsageInfo():
    print("""Usage:
\tomodoro
\tomodoro P-L-S-B-T
with
\tP\tnumber of pomodori to do in a cycle
\tL\tlength of one pomodori in minutes
\tS\tlength of a short break in minutes
\tB\tlength of a long break in minutes
\tT\tterminal bell: 1 = On / 0 = Off\n
Example with the default values:
\tomodoro 4-25-5-15-0
""")


def printCLIInfo():
    print("""Welcome to omodoro. Available commands:\n
 p pause the current pomodoro cycle
 c continue the current pomodoro cycle
 n abort current pomodori/break, start next one
 s get status of current cycle
 t terminal bell on/off
 q quit omodoro""")


# global variables
class States:
    Pomodori, ShortBreak, LongBreak = range(3)


cnt_pomodori = 0  # pomodori left in the current cycle
cnt_short_breaks = 0  # short breaks left in the current cycle
end_time = None  # end time of the current state
time_left = None  # time left after the pause
state = States.Pomodori
command = ""  # input string
lockObject = Lock()
nextState = False  # indicates user-triggered state change


def changeState(newState, length):
    global end_time, state, nextState
    title = ""
    description = ""
    if newState == States.Pomodori:
        title = "Next Pomodori"
        description = "Please start with the next Pomodori!\nEnd Time: "
    elif newState == States.ShortBreak:
        title = "Short Break"
        description = "Please take a short break!\nEnd Time: "
    elif newState == States.LongBreak:
        title = "Long Break"
        description = "Please take a long break!\nEnd Time: "
    else:
        # Something went wrong - exit
        exit(1)
    end_time = datetime.now() + timedelta(minutes=length)
    description = description + end_time.strftime("%H:%M")

    if terminal_bell == True:
        print("\n%s\nEnd Time: %s\a\n$ " % (title, end_time.strftime("%H:%M")), end="")
    else:
        print("\n%s\nEnd Time: %s\n$ " % (title, end_time.strftime("%H:%M")), end="")

    if onWindows:
        system('Msg "%s" "%s"' % (getenv("USERNAME"), description.replace('\n', '   ')))
    else:
        system("terminal-notifier -u critical '%s' '%s'" % (title, description))
    state = newState
    nextState = False  # user-triggered change state finished


class PomodoroThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global cnt_pomodori, cnt_short_breaks, state

        while command != "q":
            lockObject.acquire()
            if state == States.Pomodori:
                # pomodori is not over
                if end_time > datetime.now() and not nextState:
                    pass
                else:
                    # decrease number of pomodori for the current cycle
                    cnt_pomodori -= 1
                    if length_short_break > 0 and cnt_short_breaks > 0:
                        # length of short breaks > 0 and short breaks left -> start short break
                        changeState(States.ShortBreak, length_short_break)
                    elif length_short_break == 0 and cnt_pomodori != 0:
                        # no short breaks -> start next pomodori
                        changeState(States.Pomodori, length_pomodori)
                    elif cnt_pomodori == 0:
                        # last pomodori over -> start long break
                        changeState(States.LongBreak, length_long_break)
                    else:
                        # Something went wrong - exit
                        print("Error - aborting.")
                        exit(1)
            elif state == States.ShortBreak:
                # short break is not over
                if end_time > datetime.now() and not nextState:
                    pass
                else:
                    # decrease number of short breaks for the current cycle
                    cnt_short_breaks -= 1
                    # start next pomodori
                    changeState(States.Pomodori, length_pomodori)
                pass
            elif state == States.LongBreak:
                # long break is not over
                if end_time > datetime.now() and not nextState:
                    pass
                else:
                    # re-init variables, start next cycle
                    cnt_pomodori = num_pomodori
                    cnt_short_breaks = num_pomodori - 1
                    changeState(States.Pomodori, length_pomodori)
            else:
                # Something went wrong - exit
                print("Error - aborting.")
                exit(1)
            lockObject.release()
            sleep(30)
        print("Shutdown finished.")


if __name__ == "__main__":

    if exists(conf_file):
        config = ConfigParser()
        config.read(conf_file)
        try:
            num_pomodori = config.getint('POMODORO', 'number')
            length_pomodori = config.getint('POMODORO', 'length')
            length_short_break = config.getint('POMODORO', 'short_break')
            length_long_break = config.getint('POMODORO', 'long_break')
            terminal_bell = bool(config.getint('POMODORO', 'terminal_bell'))
        except NoOptionError as error:
            print("Error while reading config file: " + str(error))
            exit(1)
    if len(argv) != 1:
        if len(argv) == 2:
            if (argv[1] == "-h") or (argv[1] == "--help"):
                printUsageInfo()
                exit(0)
            else:
                try:
                    user_values = argv[1].split('-')
                    num_pomodori = int(user_values[0])
                    length_pomodori = int(user_values[1])
                    length_short_break = int(user_values[2])
                    length_long_break = int(user_values[3])
                    terminal_bell = bool(int((user_values[4])))
                except:
                    print("Invalid argument: " + str(argv[1]) + "\n")
                    printUsageInfo()
                    exit(1)
        else:
            printUsageInfo()
            exit(1)

    # initialize count variables
    cnt_pomodori = num_pomodori
    cnt_short_breaks = num_pomodori - 1
    printCLIInfo()
    # start first pomodori
    changeState(States.Pomodori, length_pomodori)
    # run pomodoro thread
    pomodorothread = PomodoroThread()
    pomodorothread.start()

    # commandline interface
    while True:
        command = get_input()
        if command == "p":
            if time_left is None:  # if not None, already paused
                if lockObject.acquire(True):
                    time_left = end_time - datetime.now()
                    print("Paused.\n$ ", end="")
            else:
                print("Error: current cycle is already paused.\n$ ", end="")
        elif command == "c":
            try:
                lockObject.release()
            except ThreadError:
                print("Error: current cycle is not paused.\n$ ", end="")
                continue
            end_time = datetime.now() + time_left
            time_left = None
            print("Continuing the current pomodoro cycle.\nNew End Time: %s\n$ " % end_time.strftime("%H:%M"), end="")
        elif command == "n":
            nextState = True
            print("Skipping to next pomodori/break, please wait some seconds.", end="")
        elif command == "s":
            if state == States.Pomodori:
                print("Pomodoro cycle", end="")
            elif state == States.ShortBreak:
                print("Short break", end="")
            elif state == States.LongBreak:
                print("Long break", end="")

            if time_left is None:
                print(", running, %d minutes left\n$ " % round(
                    (end_time - datetime.now()).total_seconds() / 60), end="")
            else:
                print(", paused, %d minutes left\n$ " % round(
                    time_left.total_seconds() / 60), end="")
        elif command == "q":
            try:
                lockObject.release()
            except ThreadError:
                pass  # Lock was not locked - exit anyway
            print("omodoro is shutting down, please wait some seconds.")
            exit(0)
        elif command == "t":
            if terminal_bell == True:
                terminal_bell = False
                print("Terminal bell off")
            elif terminal_bell == False:
                terminal_bell = True
                print("Terminal bell on")
        else:
            print("Unknown command.\n$ ", end="")
