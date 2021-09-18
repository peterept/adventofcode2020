#!/usr/bin/env python3

# https://adventofcode.com/2020/day/2#

import re

def parse(s):
    # format: <first>-<second> <char>: <password>
    pattern = ''.join([
        "(\d+)",       # One or more digits
        "\-",          # One -
        "(\d+)",       # One or more digits
        "\s*",         # Zero or more spaces
        "([A-Za-z])",  # One alphabet char
        "\:\s*",       # One : followed by zero or more spaces
        "([A-Za-z]*)", # Zero or more alphabet chars
        "(.*)"
    ])
    m = re.search(pattern, s)
    #print(s + ": " + m.group(1) + "," + m.group(2) + "," + m.group(3) + "," + m.group(4))
    return {'first': int(m.group(1)), 'second': int(m.group(2)), 'char': m.group(3)[0], 'password': m.group(4)}

def load_data(filename) -> [dict]:
    data = []
    with open(filename) as my_file:
        for line in my_file:
            data.append(parse(line.strip()))
    return data


def main():
    data = load_data('input.txt')
    #print(data)

    # count valid passwords
    valid = 0
    for rec in data:
        i = rec['first'] - 1
        j = rec['second'] - 1
        s = rec['password']
        slen = len(s)
        c = rec['char']
        if i < slen and j < slen and ( (s[i] == c and s[j] != c) or (s[i] != c and s[j] == c) ):
            valid += 1

    print(f'Valid passwords: {valid}')

if __name__ == "__main__":
    main()
