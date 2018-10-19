import sys
import os
import brainfuck
from langdetect import detect
def logo():
    brainfuck.execute("brainfuckname.txt")

def readfile(filename):
    f = open(filename,"r")
    lines=f.readlines()
    f.close()
    return lines  

def filterlines(lines):
    
    lines=[line for line in lines if len(line)>2]
    '''templines2=[line for line in templines if "'" not in line and "(" not in line and "," in line]
    filtered_lines=[templines2[i] for i in range(0,len(templines2),2)]'''
    filtered_lines=[line for line in lines if detect(line)=="hu" and "," in line]
    return filtered_lines


def getsaying(lines):
    pass



def main():
    os.system("clear")
    logo()
    print(filterlines(readfile("sayings.txt")))

if __name__ == '__main__':
    main()