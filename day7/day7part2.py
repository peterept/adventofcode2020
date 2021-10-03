#!/usr/bin/env python3

# https://adventofcode.com/2020/day/7#part2

import re

perf_counter = 0 

def load_data(filename, parser = None) -> []:
    data = []
    with open(filename) as my_file:
        for line in my_file:
            if parser:
                line = parser(line)
            data.append(line)
    return data

def parser(s):
	# for bags that contain no other bags
	# format: <MULTI WORD NAME> bags contain no other bags.
    pattern = ''.join([
        "^([a-z ]*)",
        "(bags contain no other bags.)",  
        "(?!.)"       
    ])
    m = re.search(pattern, s)
    if m != None:
        #print("LONE:")
        #print(m.group(1))
        return {"name": m.group(1).strip(), "contents": None}

	# for bags containing other bags
	# format: <MULTI WORD NAME> bags contain [<N> <MULTI NAME BAG> bags[,]].
    pattern = ''.join([
        "^([a-z ]*)",
        "(bags contain)", 
        "(.*)"
    ])
    m = re.search(pattern, s)
    if m != None:
        # print("MULTI:")
        # print(m.group(1))
        bags = m.group(3).split(",")
        # print(bags)
        name = m.group(1).strip()
        contents = []
        for bag in bags:
            pattern = ''.join([
                "(\d+)\s*",
                "([a-z ]*) bag[s]?[.]?",  
            ])
            m = re.search(pattern, bag)
            if m != None:
                # print("> " + m.group(1) + " : " + m.group(2))
                contents.append({"name": m.group(2), "count": int(m.group(1))})
        return {"name": name, "contents": contents}

# Memoization
def has_memoization(bag_to_check, bags_dict) -> bool:
    key = f"_memoization_inside_bag_count"
    return key in bags_dict[bag_to_check]

def get_memoization(bag_to_check, bags_dict) -> int:
    key = f"_memoization_inside_bag_count"
    return bags_dict[bag_to_check][key]

def set_memoization(bag_to_check, bags_dict, value):
    key = f"_memoization_inside_bag_count"
    bags_dict[bag_to_check][key] = value


def count_bags_in_bag(bags_dict, name, memoization: bool) -> int:
    global perf_counter
    perf_counter += 1

    # check memoization
    if memoization:
        if has_memoization(name, bags_dict):
            return get_memoization(name, bags_dict)

    count = 0
    # recursively search all bags
    bag_contents = bags_dict[name]['contents']
    if bag_contents != None:
        for bag in bag_contents:
            bag_to_check = bag["name"]
            bags_inside = count_bags_in_bag(bags_dict, bag_to_check, memoization)
            set_memoization(bag_to_check, bags_dict, bags_inside)

            count += (bags_inside + 1) * bag["count"]
    return count


def main():
    # parse to return an array of records in the following format:
    #  [{"name": "vibrant olive", contents: None}
    #  or 
    #  [{"name": "vibrant olive", contents: [{"name": "muted turquoise", "count":2}]}
    data = load_data('input.txt', parser)
    # print(data)

    # convert the array into a dict using the name field
    bags_dict = {item['name']:item for item in data}
    # print(bags_dict)
    # print(len(data))
    # print(len(bags_dict))

    # sanity check, length of dict should match records from file
    if len(data) != len(bags_dict):
        print("Error: Input record count should match unique bag names found")
        return

    # brute force
    global perf_counter
    perf_counter = 0
    target_bag = "shiny gold"
    bag_count = count_bags_in_bag(bags_dict, target_bag, False)
    print(f"Bag '{target_bag} contains {bag_count} bags!")
    print(f"Perf Results: recursive count: {perf_counter}")

    # with memoization
    perf_counter = 0
    bag_count = count_bags_in_bag(bags_dict, target_bag, True)
    print(f"[Memoization] Bag '{target_bag} contains {bag_count} bags!")
    print(f"[Memoization] Perf Results: recursive count: {perf_counter}")

 
if __name__ == "__main__":
    main()





