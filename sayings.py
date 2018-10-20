import sys
import os
import brainfuck
from langdetect import detect


def logo():
    brainfuck.execute("brainfuckname.txt")


def readfile(filename):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    return lines


def filterlines(lines):

    filtered_lines = [line for line in lines if len(line) > 2 and detect(
        line) == "hu" and "," in line and "(" not in line and "/" not in line and line.count(",") < 2]
    return filtered_lines


def getsaying(lines):
    pass


def main():
    os.system("clear")
    logo()
    filteredlines = filterlines(readfile("sayings.txt"))
    print(filteredlines)


if __name__ == '__main__':
    main()
