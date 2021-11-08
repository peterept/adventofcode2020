#!/usr/bin/env python3

# https://adventofcode.com/2020/day/14#part2

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


def process(mask, addr, val, memory):
    """convert to binary string format to be used directly"""
    # https://stackoverflow.com/questions/1523465/binary-numbers-in-python

    # create the new address
    # only change is a 1 in the mask is a 1 in the address
    print(mask)
    addr_str = '{0:036b}'.format(addr)
    print(addr_str)
    for i, v in enumerate(mask):
        if v == "1":
            addr_str = addr_str[:i] + '1' + addr_str[i+1:]
        if v == "X":
            addr_str = addr_str[:i] + 'X' + addr_str[i+1:]
    print(addr_str)

    # total combos
    x_count = addr_str.count('X')
    total_addresses = pow(2, x_count)
    # print(x_count)
    # print(total_addresses)

    # generate all possible cases for X
    for i in range(0, total_addresses):
        # print the case with leading 0s, eg: 4 x's i = 2 will be 0010
        x_values = f'{{0:0{x_count}b}}'.format(i)
#        print(x_values)

        # replace all x's with the x_values
        temp_addr_str = addr_str
        for ix, vx in enumerate(x_values):
            jx = temp_addr_str.find('X')   
            temp_addr_str = temp_addr_str[:jx] + vx + temp_addr_str[jx+1:]
#        print(temp_addr_str)
     
        # set the memory
        temp_addr = int(f'0b{temp_addr_str}', 2)
        memory[temp_addr] = val
        print(f"{temp_addr_str}  (decimal {temp_addr})")


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

    # process("000000000000000000000000000000X1001X", 42, 100, memory)
    # process("00000000000000000000000000000000X0XX", 26, 1, memory)
    # print(memory) 
    result = sum(memory.values())

    print(f'Sum of memory = {result}')



if __name__ == "__main__":
    main()
