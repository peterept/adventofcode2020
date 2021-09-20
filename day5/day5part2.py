#!/usr/bin/env python3

# https://adventofcode.com/2020/day/5#part2

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
    """convert to binary string format to be used directly"""
    # https://stackoverflow.com/questions/1523465/binary-numbers-in-python

    # rows
    pattern = ''.join([
        "^([FB]*)",   # exactly six characters 0-9 or a-f
        "([LR]*)",    # exactly six characters 0-9 or a-f
        "(?!.)"       # no additional characters
    ])
    m = re.search(pattern, s)
    rows_part = m.group(1)
    cols_part = m.group(2)

    rows_bsp = rows_part.replace("F", "0")
    rows_bsp = rows_bsp.replace("B", "1")
    cols_bsp = cols_part.replace("L", "0")
    cols_bsp = cols_bsp.replace("R", "1")
    # print(rows_bsp)
    # print(cols_bsp)
    return {
        '_raw': s,
        'rows_bsp_len': int(f'0b{"1" * len(rows_bsp)}',2), 
        'rows_bsp': int(f'0b{rows_bsp}',2), 
        'cols_bsp_len': int(f'0b{"1" * len(cols_bsp)}',2), 
        'cols_bsp': int(f'0b{cols_bsp}',2)
    }


def get_seat_id(s) -> int:
    bsp = parser(s)
    # print(bsp)
    row = bsp['rows_bsp_len'] & bsp['rows_bsp']
    col = bsp['cols_bsp_len'] & bsp['cols_bsp']
    seat_id = row * (bsp['cols_bsp_len'] + 1) + col

    print(f'row={row} col={col} seat={seat_id}')
    return seat_id


def main():
    data = load_data('input.txt')
    #print(data)

    max_rows = 128
    max_cols = 8
    all_seats = [None] * (max_rows*max_cols)

    # populate all the full seats
    for pattern in data:
        seat_id = get_seat_id(pattern)
        all_seats[seat_id] = seat_id

    print(all_seats)

    # test values
    # print(get_seat_id("BFFFBBFRRR") == 567)
    # print(get_seat_id("FFFBBBFRRR") == 119)
    # print(get_seat_id("BBFFBBFRLL") == 820)


if __name__ == "__main__":
    main()
