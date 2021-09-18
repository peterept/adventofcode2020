#!/usr/bin/env python3

# https://adventofcode.com/2020/day/3#

from functools import reduce

def load_data(filename) -> [int]:
    data = []
    with open(filename) as my_file:
        for line in my_file:
            data.append(line.strip())
    return data

class Map:
    def __init__(self, data):
        self._data = data
        self.height = len(data)

    def get(self, x: int, y: int) -> str:
        if x < 0 or y < 0 or y >= self.height:
            return ""
        row_width = len(self._data[y])
        return self._data[y][x % row_width]


def main():
    data = load_data('input.txt')
    #print(data)

    map = Map(data)
    #print(map.height)

    #s = ""
    #for x in range(0, 150):
    #    s += map.get(x,0)
    #print(map.get(0,2))
    #print(s)

    # count trees hit for multiple slopes
    slopes = [
        [1,1],
        [3,1],
        [5,1],
        [7,1],
        [1,2]
    ]
    slopes_trees = []
    for slope in slopes:
        trees = 0
        xy = [0,0]
        while xy[1] < map.height:
            if map.get(xy[0],xy[1]) == "#":
                trees += 1
            xy[0] += slope[0]
            xy[1] += slope[1]

        slopes_trees.append(trees)
        #print(f'On slope {slope} trees hit: {trees}. Ouch!')

    # solution multiply all trees
    total_trees = reduce((lambda x, y: x * y), slopes_trees)
    print(f'Multiplied trees: {total_trees}')


if __name__ == "__main__":
    main()
