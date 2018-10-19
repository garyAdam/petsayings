import sys
import os
def readfile(filename):
    f = open(filename,"r")
    lines=f.readlines()
    f.close()
    return lines
    

def filterlines(lines):
    templines=[line for line in lines if len(line)>2]
    templines2=[line for line in templines if "'" not in line and "(" not in line and "," in line]
    filtered_lines=[templines2[i] for i in range(0,len(templines2),2)]
    return filtered_lines


def getsaying(lines):
    pass







def main():
    os.system("clear")
    print(filterlines(readfile("sayings.txt")))

if __name__ == '__main__':
    main()