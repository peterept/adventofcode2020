#!/usr/bin/env python3

# https://adventofcode.com/2020/day/12
from collections import OrderedDict

def load_data(filename, parser = None) -> []:
    data = []
    with open(filename) as my_file:
        for line in my_file:
            if parser:
                line = parser(line)
            data.append(line)
    return data

def parser(s):
	""" Each line is in format of [cmd letter, number]"""
	cmd = s[:1]
	val = int(s[1:])
	return [cmd,val]


def main():

	data = load_data('input.txt', parser)
	#print(data)

	dirs = OrderedDict()
	dirs["N"] = [ 0,  1]
	dirs["E"] = [ 1,  0]
	dirs["S"] = [ 0, -1]
	dirs["W"] = [-1,  0]

	current_dir = "E"
	x = 0
	y = 0

	for cmd in data:
		c = cmd[0]
		n = cmd[1]
		if c == "F":
			c = current_dir
			print(f"forward is: {c}")
		if c in dirs:
				direction = dirs[c]
				x += (n * direction[0])
				y += (n * direction[1])
				print(f"move {c} by {n} to {x},{y}")
		elif c == "R" or c == "L":
				# rotating in stepping clockwide through our vald roations
				turn90times = n/90
				if c == "L":
					turn90times *= -1	
				# move direction number of 90 degree steps
				current_dir_index = list(dirs).index(current_dir)				
				current_dir_index = int(current_dir_index + turn90times) % len(dirs)
				current_dir = list(dirs.items())[current_dir_index][0]	
				print(f"rotate {c} {n} to {current_dir}")

	print(f"x={x} y={y} manhatten={abs(x)+abs(y)}")


if __name__ == "__main__":
    main()





