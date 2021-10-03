#!/usr/bin/env python3

# https://adventofcode.com/2020/day/7

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
def has_memoization(name, bag_to_check, bags_dict) -> bool:
    key = f"_memoization_searched_for_{name}"
    return key in bags_dict[bag_to_check]

def get_memoization(name, bag_to_check, bags_dict) -> bool:
    key = f"_memoization_searched_for_{name}"
    return bags_dict[bag_to_check][key]

def set_memoization(name, bag_to_check, bags_dict, value):
    key = f"_memoization_searched_for_{name}"
    bags_dict[bag_to_check][key] = value


def bag_in_bag(name, bag_to_check, bags_dict, memoization: bool) -> bool:
    global perf_counter
    perf_counter += 1

    # our bag can't be contained by our own bag
    if name == bag_to_check:
        return False

    bag_to_check_contents = bags_dict[bag_to_check]['contents']
    # this bag doesn't contain any bags, so ignore
    if bag_to_check_contents == None:
        return False

    # check memoization
    if memoization:
        if has_memoization(name, bag_to_check, bags_dict):
            return get_memoization(name, bag_to_check, bags_dict)

    # if this bag contains our bag directly then return it
    if next((item for item in bag_to_check_contents if item["name"] == name), None) != None:
        set_memoization(name, bag_to_check, bags_dict, True)
        return True

    # our bag isn't in this bag but check each bag this bag contains
    for bag in bag_to_check_contents:
        found = bag_in_bag(name, bag["name"], bags_dict, memoization)
        set_memoization(name, bag_to_check, bags_dict, found)
        if found:           
            return True


def bags_that_contain_bag(bags_dict, name, memoization: bool = False) -> int:
    count = 0
    for bag_to_check in bags_dict.keys():
        if bag_in_bag(name, bag_to_check, bags_dict, memoization):
            count += 1
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

    # find if bag contains desired bag
    target_bag = "shiny gold"

    # brute force
    global perf_counter
    perf_counter = 0
    bags_found = bags_that_contain_bag(bags_dict, target_bag, False)
    print(f"Given {len(bags_dict)} bags, the count of bags that can contain '{target_bag}' is {bags_found}")
    print(f"Perf Results: recursive count: {perf_counter}")

    # with memoization
    perf_counter = 0
    bags_found = bags_that_contain_bag(bags_dict, target_bag, True)
    print(f"[Memoization] Given {len(bags_dict)} bags, the count of bags that can contain '{target_bag}' is {bags_found}")
    print(f"[Memoization] Perf Results: recursive count: {perf_counter}")


if __name__ == "__main__":
    main()





