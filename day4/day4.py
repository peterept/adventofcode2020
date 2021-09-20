#!/usr/bin/env python3

# https://adventofcode.com/2020/day/4#

import re

def load_data(filename, parser) -> []:
    data = []
    with open(filename) as my_file:
        # records are concatenated multiple lines until EOR (empty line) or EOF
        rec = ""
        while True:
            line = my_file.readline()
            if not line or line == "\n": # EOF or EOR
                if rec:
                    data.append(parser(rec))
                    rec = ""
            else:
                # concatenate lines into one string (removing trailing EOL)
                rec = ' '.join(filter(None, [rec, line.rstrip('\n')]))
            if not line: # EOF abort
                break

    return data


def parse_passport(s):
    rec = dict()
    for keyvalue in s.split(' '): # split by whitespace
        # format: <key>:<value>
        pattern = ''.join([
            "(\w+)",       # One or more alphanumeric
            "\:\s*",       # One : followed by zero or more spaces
            "(.*)"         # remainder of string
        ])
        m = re.search(pattern, keyvalue)
        rec[m.group(1)] = m.group(2)
    #rec['_raw'] = s
    return rec


def main():
    data = load_data('input.txt', parse_passport)
    #print(len(data))
    #print(data)

    # solution: required fields set to validate passport
    required_fields = {
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
    }

    valid = 0
    for rec in data:
        # print(rec.keys())
        # print(required_fields)
        if required_fields.issubset(set(rec.keys())):
            valid += 1

    print(f'Valid Passports: {valid}')

if __name__ == "__main__":
    main()
