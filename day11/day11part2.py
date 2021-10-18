#!/usr/bin/env python3

# https://adventofcode.com/2020/day/11#part2
import copy

def load_data(filename, parser = None) -> []:
    data = []
    with open(filename) as my_file:
        for line in my_file:
            if parser:
                line = parser(line)
            data.append(line)
    return data

def parser(s):
    return s.rstrip()


class Grid:
    def __init__(self, data):
        self._data = data
        self.height = len(data)
        if self.height > 0:
            # assume each row is the same width
            self.width = len(data[0])
        else:
            self.width = 0

    def get(self, x: int, y: int) -> str:
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return ""
        return self._data[y][x]

    def set(self, x: int, y: int, v: str):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return
        self._data[y] = self._data[y][:x] + v + self._data[y][x+1:]

    def valid_location(self, x: int, y: int) -> bool:
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        return True

    def __repr__(self):
        s = ""
        for line in self._data:
            s += f"{line}\n"
        return s        

    def count_adjacent_occupied_seats(self, x: int, y: int) -> int:
        # check all seats around this one
        seats_to_check = [
            (-1,-1),( 0,-1),(1,-1),
            (-1, 0),        (1, 0),
            (-1, 1),( 0, 1),(1, 1),
        ]
        count = 0
        for seat in seats_to_check:
            if self.get(x + seat[0], y + seat[1]) == "#":
                count += 1
        return count

    def count_visible_occupied_seats(self, x: int, y: int) -> int:
        # check all seats visible from this one
        directions_to_check = [
            (-1,-1),( 0,-1),(1,-1),
            (-1, 0),        (1, 0),
            (-1, 1),( 0, 1),(1, 1),
        ]
        count = 0
        for direction in directions_to_check:
            # follow each direction until we locate a seat
            ix = x
            iy = y
            while self.valid_location(ix, iy):
                ix += direction[0]
                iy += direction[1]
                v = self.get(ix, iy)
                # empty seat we can abort
                if v == "L":
                    break
                # occupied seat, count it and abort
                if v == "#":
                    count += 1
                    break
        return count


    def count_occupied_seats(self) -> int:
        count = 0
        for row in range(self.width):
            for col in range(self.height):
                if self.get(row, col) == "#":
                    count += 1
        return count



def main():
    data = load_data('input.txt', parser)
    #print(data)

    grid = Grid(data)
    #print(map.height)
    print(grid)

    iteration_count = 0
    grid_copy_dirty = True
    while grid_copy_dirty == True:
        # dupliacate grid
        grid_copy = copy.deepcopy(grid)
        grid_copy_dirty = False
        iteration_count += 1

        for row in range(grid.width):
            for col in range(grid.height):
                # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied
                if grid.get(row, col) == "L" and \
                    grid.count_visible_occupied_seats(row, col) == 0:
                        grid_copy.set(row, col, "#")
                        grid_copy_dirty = True
                # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
                elif grid.get(row, col) == "#" and \
                    grid.count_visible_occupied_seats(row, col) >= 5:
                        grid_copy.set(row, col, "L")
                        grid_copy_dirty = True

        # replace grid
        grid = grid_copy

        print(f"Iteration: {iteration_count}...")
        print(grid)

    occupied_seats = grid.count_occupied_seats()
    print(f"occupied seats = {occupied_seats}")        


if __name__ == "__main__":
    main()
