#!/usr/bin/env python3

# https://adventofcode.com/2020/day/10

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


def insertionSort(a):
    for step in range(1, len(a)):
        key = a[step]
        j = step - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = key


def main(): 
    data = load_data('input.txt', parser)
    #print(data)

    # sort the power adapters in order
    insertionSort(data)
    #print(data)

    # loop through the array counting the differences between numbers
    # if the difference is > 3 then fail
    results = [0,0,0,0]

    current = 0 # seat power
    for i in range(len(data)):
        difference = data[i] - current
        print(f"current: {current} {i}:{data[i]} delta={difference}")
        if difference >= len(results):
            raise Exception(f"Faral: Invalid input data: {difference}")
        results[difference] += 1
        current = data[i]

    # add one 3 difference for the internal adapter
    results[3] += 1

    print(results)
    print(f"ones ({results[1]}) x threes ({results[3]}): {results[1] * results[3]}")


if __name__ == "__main__":
    main()
