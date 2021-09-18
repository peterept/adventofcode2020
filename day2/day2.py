#!/usr/bin/env python3

# https://adventofcode.com/2020/day/2#

import re

def parse(s):
    # format: <min>-<max> <char>: <password>
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
    return {'min': int(m.group(1)), 'max': int(m.group(2)), 'char': m.group(3)[0], 'password': m.group(4)}

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
        count = rec['password'].count(rec['char'])
        if count >= rec['min'] and count <= rec['max']:
            valid += 1

    print(f'Valid passwords: {valid}')

if __name__ == "__main__":
    main()
