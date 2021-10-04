#!/usr/bin/env python3

# https://adventofcode.com/2020/day/9

import re

def load_data(filename, parser = None) -> []:
    data = []
    with open(filename) as my_file:
        for line in my_file:
            if parser:
                line = parser(line)
            data.append(line)
    return data

def parser(s):
    return int(s)


def has_valid_pair(list, value) -> bool:
    # check each value
    for i,v in enumerate(list):
        for j,w in enumerate(list):
            # can't use the same number
            if i != j:
                if (v+w) == value:
                    return True
    return False


def main():
    data = load_data('input.txt', parser)
    #print(data)

    window_size = 25

    # i is index for the item we want to see if the proceeding 25 has a pair for
    for i in range(window_size,len(data)):
        window_values = data[i-window_size:i]
        #print(window_values)
        #print(f"Checking index {i} value {data[i]} for values: {window_values}")
        if not has_valid_pair(window_values, data[i]):
            print(f"No pair found for {i}th value: {data[i]}")
            return
            

if __name__ == "__main__":
    main()
