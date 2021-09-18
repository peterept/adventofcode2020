#!/usr/bin/env python3

# https://adventofcode.com/2020/day/1#


def load_data(filename) -> [int]:
    data = []
    with open(filename) as my_file:
        for line in my_file:
            data.append(int(line))
    return data


def main():
    data = load_data('input.txt')
    print(data)

    # find 2 numbers that add up to 2020
    desired = 2020
    result = []

    # brute force - try and add each pair to see if they equal 2020 O(N*N)
    for i in range(len(data)):
        for j in range(len(data)):
            # ignore if the same item
            if i == j:
                continue
            if data[i] + data[j] == desired:
                result = [data[i], data[j]]
                break

    #print(result)

    # solution
    if len(result) == 2:
        print(f'{result} = {result[0] * result[1]}')
    else:
        print("Error: No result")

if __name__ == "__main__":
    main()
