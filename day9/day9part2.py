#!/usr/bin/env python3

# https://adventofcode.com/2020/day/9#part2

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

def calculate_invalid_number(data: [int]) -> int:
    window_size = 25

    # i is index for the item we want to see if the proceeding 25 has a pair for
    for i in range(window_size,len(data)):
        window_values = data[i-window_size:i]
        #print(window_values)
        #print(f"Checking index {i} value {data[i]} for values: {window_values}")
        if not has_valid_pair(window_values, data[i]):
            print(f"No pair found for {i}th value: {data[i]}")
            return data[i]
    raise Exception("Fatal: Failed to find invalid number!")


def find_contiguous_numbers_sum_to_number(data: [int], num: int) -> [int]:
    # start from the beginning, add each number until it either equals or exceeds our number
    for i in range(0, len(data)):
        n = 0
        for j in range(i, len(data)):
            n += data[j]
            if n == num:
                return data[i:j+1]
            elif n > num:
                break
    raise Exception(f"Fatal: No contiguous set that equals {num}!")


def main():
    data = load_data('input.txt', parser)
    #print(data)

    invalid_number = calculate_invalid_number(data)    
    print(f"invalid number: {invalid_number}")

    list = find_contiguous_numbers_sum_to_number(data, invalid_number)
    print(f"Coniguous block is: {list}")

    result = min(list) + max(list) 
    print(f"Result is sum of smallest and largest number = {result}")

if __name__ == "__main__":
    main()
