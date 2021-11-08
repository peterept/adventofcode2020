#!/usr/bin/env python3

# https://adventofcode.com/2020/day/14

import re

def load_data(filename, parser = None) -> []:
    data = []
    with open(filename) as my_file:
        for line in my_file:
            if parser:
                line = parser(line, data)
            data.append(line)
    return data


def parser(s, data):
    return s


def process(mask, index, val, memory):
    """convert to binary string format to be used directly"""
    # https://stackoverflow.com/questions/1523465/binary-numbers-in-python
    mask_ones_str = mask.replace("X", "0")
    mask_ones = int(f'0b{mask_ones_str}', 2)
    mask_not_zeros_str = mask.replace("X", "1")
    mask_not_zeros = int(f'0b{mask_not_zeros_str}', 2)

    val = (val | mask_ones) & mask_not_zeros
    # print( 'value:  {0:036b}'.format(val))
    # print(f'mask:   {mask}')
    # print('result: {0:036b}'.format(val))
    # print(val)
    memory[index] = val


def main():
    data = load_data('input.txt', parser)
  #  print(data)

    memory = {}
    mask = None
    for line in data:
        # mask
        m = re.search('^mask = ([X10]*)', line)
        if m:
            mask = m.group(1)

        # mem operation
        m = re.search('^mem\[(\d*)\]\s=\s(\d*)', line)
        if m:
            process(mask, int(m.group(1)), int(m.group(2)), memory)

    # process("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 8, 11, memory)
    # process("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 7, 101, memory)
    # process("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 8, 0, memory)
    # print(memory) 
    result = sum(memory.values())

    print(f'Sum of memory = {result}')



if __name__ == "__main__":
    main()
