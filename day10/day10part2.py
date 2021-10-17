#!/usr/bin/env python3

# https://adventofcode.com/2020/day/10#part2

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


# def bfs_find_combinations_with_memoiz(memoiz, data, index) -> int:
#     if memoiz[index]:
#         return memoiz[index]

#     memoiz[index] = bfs_find_combinations(data, index, )
#     return memoiz[index]


def bfs_find_combinations(data, index) -> int:
    last_index = len(data) - 1

    # at the end only one path 
    if index == last_index:
        return 1

    joltage = data[index]
    max_difference_joltage = 3

    paths = 0
    i = index + 1
    while i <= last_index:
        difference = data[i] - joltage
        if difference <= max_difference_joltage:
            paths += bfs_find_combinations(data, i)
        else:
            # we can abort since we have a sorted input data
            break
        i += 1

    return paths


def bfs_find_combinations_with_memoiz(memoiz, data, index) -> int:
    if memoiz[index]:
        return memoiz[index]

    last_index = len(data) - 1

    # at the end only one path 
    if index == last_index:
        return 1

    joltage = data[index]
    max_difference_joltage = 3

    paths = 0
    i = index + 1
    while i <= last_index:
        difference = data[i] - joltage
        if difference <= max_difference_joltage:
            paths += bfs_find_combinations_with_memoiz(memoiz, data, i)
        else:
            # we can abort since we have a sorted input data
            break
        i += 1

    memoiz[index] = paths
    return paths


def main(): 
    data = load_data('input.txt', parser)
    #print(data)

    # sort the power adapters in order
    insertionSort(data)
    #print(data)

    # add in our start joltage
    data = [0] + data

    # BFS all unique combinations
    memoiz_array = [None] * len(data)
    count = bfs_find_combinations_with_memoiz(memoiz_array, data, 0)
    print(f"valid count using memoiz = {count}")


if __name__ == "__main__":
    main()
