#!/bin/python3

#
# leetspeak.py - generate a list of leetspeak passwords from an input string, 'companyA' to 'C0mP4nj@' etc
#

import random
import sys


# main func
def main():
    # sanity checks
    if len(sys.argv) != 3:
        print("Usage:\r\n"
              "./leetspeak.py <inputStr> <numIterations>\r\n"
              "\r\n"
              "Examples:\r\n"
              "./leetspeak.py companyA 100\r\n"
              "\r\n")
        exit()


    # param init
    inputStr = str(sys.argv[1])
    numIterations = int(sys.argv[2])
    
    # generate specified number of leetspeak strings
    print("\n[+] Generating leetspeak results\n\n")
    leetspeak_list = []
    for i in range(0, numIterations):
        leetspeak = gen_leetspeak(inputStr)
        leetspeak_list.append(leetspeak)
    
    # sort the results and remove duplicates
    leetspeak_list_unique = unique(leetspeak_list)
    leetspeak_list_unique.sort()
    for item in leetspeak_list_unique:
        print(item)

    # done!
    print("\n\n[+] Done! Generated " + str(len(leetspeak_list_unique)) + " unique leetspeak strings.\n")


# to convert a string to leetspeak
def gen_leetspeak(inputStr):
    # leet chars
    char_map = {
        "a": ["4", "@"],
        "b": ["8"],
        "c": ["[", "{", "<", "("],
        "e": ["3"],
        "g": ["6"],
        "h": ["#", "4"],
        "i": ["1", "!", "|"],
        "l": ["1", "7","|"],
        "o": ["0"],
        "r": ["7"],
        "s": ["$", "5", "z"],
        "t": ["7", "+"],
        "u": ["V"],
        "v": ["U"],
        "y": ["j"],
    }
    # our resulting string
    leetspeak = ""
    # process each char in string
    for char in inputStr:
        # include lower and upper case as possiblities
        possible_replacements = []
        possible_replacements.append(char.lower())
        possible_replacements.append(char.upper())
        # include leetspeak chars as possibilities
        if char.lower() in char_map:
            for mapItem in char_map[char.lower()]:
                possible_replacements.append(mapItem)
        # pick a random char and append to leet string
        leet_replacement = random.choice(possible_replacements)
        leetspeak = leetspeak + leet_replacement
    return leetspeak


# remove duplicates from a list
def unique(dup_list):
  
    # initialize a null list
    unique_list = []
  
    # loop through all items in list
    for x in dup_list:
        # check if exists in unique_list or not
        if x not in unique_list:
            # append new item to unique list
            unique_list.append(x)

    # return unique items
    return unique_list


# run main
if __name__ == "__main__":
    main()

