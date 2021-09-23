#!/usr/bin/env python3

# https://adventofcode.com/2020/day/6#part2

"""
Initial thoughts:
- for first person (set is empty) still add their answers
- for each other person, create a local set, then perform an intersection and save result
"""

def load_data(filename, parser = None) -> []:
    data = []
    with open(filename) as my_file:
        for line in my_file:
            if parser:
                line = parser(line)
            data.append(line)
    return data


def main():
	data = load_data('input.txt')
	# print(data)

	groups = []
	answers = None
	for line in data:
		line = line.strip()
		if answers == None or line == "":
			# process existing set
			if answers != None:
				groups.append(len(answers))
			# start a new group
			answers = None
		# read each character into the set
		if line != "":
			person_answers = set()
			for c in line:
				if c in "abcdefghijklmnopqrstuvwxyz":
					person_answers.add(c)
			# not first person, then perform intersection
			if answers == None:
				answers = person_answers
			else:
				answers = (answers & person_answers)
	# append our last group if we have one
	if answers != None:
		groups.append(len(answers))

	# print(groups)

	total = sum(groups)
	print(f'Answers: {total}')



if __name__ == "__main__":
    main()