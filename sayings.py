import sys
import os
import brainfuck
from langdetect import detect
import random
from time import sleep
import getch
import curses


def cursemenu(stdscr, options):
    attributes = {}
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    attributes['normal'] = curses.color_pair(1)

    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    attributes['highlighted'] = curses.color_pair(2)

    c = 0  # last character read
    option = 0  # the current option that is marked
    while c != 10:  # Enter in ascii
        stdscr.erase()
        stdscr.addstr("Choose an option!\n", curses.A_UNDERLINE)
        for i in range(len(options)):
            if i == option:
                attr = attributes['highlighted']
            else:
                attr = attributes['normal']
            stdscr.addstr(f"{i + 1}. ")
            stdscr.addstr(options[i] + '\n', attr)
        c = stdscr.getch()
        if c == curses.KEY_UP and option > 0:
            option -= 1
        elif c == curses.KEY_DOWN and option < len(options) - 1:
            option += 1

    return option


def init():
    brainfuck.evaluate('''++++++++++++++++[>++>++>++>++>++>++>++>++>++>++>++>++>++>++>++>++>++>++>++<<<<<<<<<<<<<<<<<<<-]>>+++++++++++++++++++++++++++++++++
<<++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[
>>>+>+>+>+>+>+>+>+>+>+>+>+>+>+>+>+>+<<<<<<<<<<<<<<<<<<<-]>>>>--->+++++++++[<]>>>>>>----------------------------->+>++++++++++++++>
+++>+++++++++++[<]>>>>>.<.<.>>>>.[<]>.[>]++++++++++<<--.>+++++++++++++++++++++.[<]>.>.>.>.>.<<<<.>>>>>.>.>.>.>.[>]<.
[<]>>>>>>>>>>>++.>+++++.>++++++++.>++++++++++++++++.<<<<<<<.>>>>>>>>++++++++++++++.<<<.>>>>++++++++++.<<<<<<<.[<]>.[>]<<<<<<<<.<.>>>>>+++++++++++++++.<<<.[>]+++++[>+++++++++<-]>+...''')


def readfile(filename):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    return lines


def filterlines(lines):

    filtered_lines = [line for line in lines if len(line) > 2 and detect(
        line) == "hu" and "(" not in line and "/" not in line and line.count(",") == 1]
    return filtered_lines


def getsaying(lines):
    r = random.randint(0, len(lines)-1)
    r2 = random.randint(0, len(lines)-1)
    linepart1 = [line.partition(',')[0] for line in lines]
    linepart2 = [line.partition(',')[2] for line in lines]
    return [linepart1[r], linepart2[r2]]


def main():
    os.system("clear")
    init()
    print('')
    filteredlines = filterlines(readfile("sayings.txt"))
    while True:
        chosen = curses.wrapper(cursemenu, ["Get saying", "Get 10 sayings", "Get filteredlist", "Quit"])
        if chosen == 0:
            os.system("clear")
            saying = getsaying(filteredlines)
            print(saying[0]+" . . .", end="")
            print(saying[1])
            getch.getch()
        elif chosen == 1:
            os.system("clear")

            for i in range(10):
                saying = getsaying(filteredlines)
                print(saying[0]+","+saying[1])
            getch.getch()
        elif chosen == 2:
            os.system("clear")

            print(filteredlines)
            getch.getch()
        else:
            os.system("clear")
            break


if __name__ == '__main__':
    main()
