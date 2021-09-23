#!/usr/bin/env python3

# https://adventofcode.com/2020/day/6

"""
Initial thoughts:
- read through line by line
- read all chars into a set
- start a new set for each group (start of file, or blank line)
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
	print(data)

	groups = []
	answers = None
	for line in data:
		if answers == None or line.strip() == "":
			# process existing set
			if answers != None:
				groups.append(len(answers))
			# start a new set
			answers = set()
		# read each character into the set
		for c in line:
			if c in "abcdefghijklmnopqrstuvwxyz":
				answers.add(c)
	# append our last group if we have one
	if answers != None:
		groups.append(len(answers))
	

	print(groups)

	total = sum(groups)
	print(f'Answers: {total}')



if __name__ == "__main__":
    main()