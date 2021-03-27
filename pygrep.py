""" This program can be used to search for an input string within given 
files in the current directory.  If no file name is given, it will ask the 
user to enter a file name.  Upon conclusion of execution if at least one 
match is made it will exits with a 0 value indicating success; otherwise 
it exits with a 'file has no match' message."""

import os
import argparse

# setting up input parameters
parser = argparse.ArgumentParser(prog='pygrep')
parser.add_argument('SEARCH_PATTERN', help='search pattern')
parser.add_argument('--n', action='store_true', help='prepends the file <line number>: to search matches')
parser.add_argument('--H', action='store_true', help='prepends the <filename>: to search matches')
parser.add_argument('--l', action='store_true', help='prints only the filename of files with matches')
parser.add_argument('--c', action='store_true', help='prints only the count of matching lines')
parser.add_argument('--v', action='store_true', help='inverts the search to select lines that do not match')
parser.add_argument('--q', action='store_true', help='quiet operation with zero output so that only the exit code is returned')
parser.add_argument('--files', nargs='*', help='files to be searched')

args = parser.parse_args()

def matching(pattern, file):
    """ This funciton evaluates whether there is a match for the pattern 
    in the file"""

    with open(file) as f:
        counter=0
        match_dic = {}
        for line in f:
            counter +=1
            if pattern in line:
                match_dic[counter] = line
    return match_dic

def check_n(match_dic, file):
    if match_dic:
        for k,v in match_dic.items():
            print(k, v)
    else:
        print(f'{file} has no match')

def check_H(match_dic, file):
    if args.H:
        for k,v in match_dic.items():
            print(file, v)
    else:
        print('no match')
def check_l(match_dic, file):
    if match_dic:
        print(file)
    else:
        print(f'{file} has no match')

def check_c(match_dic, file):
    if match_dic:
        print(len(match_dic.keys()))
    else:
        print(f'{file} has no match')

def check_v(match_dic, file):
    with open(file) as f:
            for line in f:
                if line not in match_dic.values():
                    print(line)

def check_q(match_dic, file):
    if match_dic:
        print(0)
    else:
        print(f'{file} has no match')

def options(match_dic, file):
    """This function evaluate input options and produce approperiate
    output """

    if args.n:
        check_n(match_dic, file)
    elif args.H:
        check_H(match_dic, file)
    elif args.l:
        check_l(match_dic, file)
    elif args.c:
        check_c(match_dic, file)
    elif args.v:
        check_v(match_dic, file)
    elif args.q:
        check_q(match_dic, file)
    else:
        with open(file) as f:
            for line in f:
                print(line)

def search():
    if args.files:
            for file in args.files:
                if file in os.listdir():
                    dic = matching(args.SEARCH_PATTERN, file)
                    options(dic, file)
                else:
                    print("File doesn't exist!")
    else:
        file = input('Please enter a file name: ')
        if file in os.listdir():
            dic = matching(args.SEARCH_PATTERN, file)
            options(dic, file)
        else:
            print("File doesn't exist!")

if __name__ == '__main__':  
    search()