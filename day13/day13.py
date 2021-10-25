#!/usr/bin/env python3

# https://adventofcode.com/2020/day/13

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
	depart = int(data[0])
	buses = [int(e) for e in data[1].split(",") if re.search("\d+", e) != None]
	print(buses)

	# find earliest bus
	earliest_bus_id = None
	earliest_bus_time = None 
	for bus in buses:
		time = (depart-(depart%bus)+bus)
		if earliest_bus_time == None or time < earliest_bus_time:
			earliest_bus_time = time
			earliest_bus_id = bus

	print(f"Depart time {depart}. Earlest bus ID {earliest_bus_id} departs at {earliest_bus_time}")
	minutes_to_wait = earliest_bus_time - depart
	answer = earliest_bus_id * minutes_to_wait
	print(f"Answer: {earliest_bus_id} (Bus ID) * {minutes_to_wait} (Mintues to wait) = {answer}")


if __name__ == "__main__":
    main()





