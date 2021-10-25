#!/usr/bin/env python3

# https://adventofcode.com/2020/day/13#part2

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
	return s

def main():
	data = load_data('input.txt')
	#print(data)

	assert len(data) == 2, "invalid input data"
	# format: [[bus index, bus id],...]
	buses = [[i, int(e)] for i, e in enumerate(data[1].split(",")) if re.search("\d+", e) != None]
	print(buses)

	t = 1
	jump = 1

	while len(buses):

		to_remove = []
		for bus in buses:
			bus_index = bus[0]
			bus_id = bus[1]
			if (t+bus_index)%bus_id == 0:
				to_remove.append(bus)
				jump *= bus_id
				print(f"Time {t} + idx {bus_index} = {t+bus_index} found match for bus id {bus_id}! New jump is {jump}")

		if len(to_remove):
			# print(f"remove matches = {to_remove}")
			buses = [x for x in buses if x not in to_remove]

		if len(buses):
			t += jump

	print(f"Answer: time={t}")


if __name__ == "__main__":
	main()


# correct = 408270049879073
 