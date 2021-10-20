#!/usr/bin/env python3

# https://adventofcode.com/2020/day/12#part2

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
	waypoint_x = 10
	waypoint_y = 1

	for cmd in data:
		c = cmd[0]
		n = cmd[1]
		if c == "F":
				x += (n * waypoint_x)
				y += (n * waypoint_y)
				print(f"move {c} by {n} to SHIP {x},{y}")
		if c in dirs:
				direction = dirs[c]
				waypoint_x += (n * direction[0])
				waypoint_y += (n * direction[1])
				print(f"move waypoint {c} by {n} to WP {waypoint_x},{waypoint_y}")
		elif c == "R" or c == "L":
				# rotating in stepping clockwide through our vald roations
				turn90times = int(n/90)
				while turn90times > 0:
					if c == "R":
						waypoint_x , waypoint_y = waypoint_y , -waypoint_x
					else:
						waypoint_x , waypoint_y = -waypoint_y , waypoint_x
					turn90times -= 1
				print(f"rotate waypoint {n} to WP {waypoint_x},{waypoint_y}")

	print(f"x={x} y={y} manhatten={abs(x)+abs(y)}")


if __name__ == "__main__":
    main()





