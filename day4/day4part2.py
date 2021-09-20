#!/usr/bin/env python3

# https://adventofcode.com/2020/day/4#part2

import re

def load_data(filename, parser) -> []:
    data = []
    with open(filename) as my_file:
        # records are concatenated multiple lines until EOR (empty line) or EOF
        rec = ""
        while True:
            line = my_file.readline()
            if not line or line == "\n": # EOF or EOR
                if rec:
                    data.append(parser(rec))
                    rec = ""
            else:
                # concatenate lines into one string (removing trailing EOL)
                rec = ' '.join(filter(None, [rec, line.rstrip('\n')]))
            if not line: # EOF abort
                break
    return data


def parse_passport(s):
    rec = dict()
    for keyvalue in s.split(' '): # split by whitespace
        # format: <key>:<value>
        pattern = ''.join([
            "(\w+)",       # One or more alphanumeric
            "\:\s*",       # One : followed by zero or more spaces
            "(.*)"         # remainder of string
        ])
        m = re.search(pattern, keyvalue)
        rec[m.group(1)] = m.group(2)
    #rec['_raw'] = s
    return rec


class Validator:
    def _validate_range(s, at_least, at_most) -> bool:
        try:
            year = int(s)
            return year >= at_least and year <= at_most
        except ValueError:
            return False

    def validate_byr(s) -> bool:
        """byr (Birth Year) - four digits; at least 1920 and at most 2002."""
        return Validator._validate_range(s, 1920, 2002)

    def validate_iyr(s) -> bool:
        """iyr (Issue Year) - four digits; at least 2010 and at most 2020."""
        return Validator._validate_range(s, 2010, 2020)

    def validate_eyr(s) -> bool:
        """eyr (Expiration Year) - four digits; at least 2020 and at most 2030."""
        return Validator._validate_range(s, 2020, 2030)

    def validate_hgt(s) -> bool:
        """hgt (Height) - a number followed by either cm or in:
             - If cm, the number must be at least 150 and at most 193.
             - If in, the number must be at least 59 and at most 76."""
        pattern = ''.join([
            "(\d+)",         # One or more digits
            "(in|cm)",       # in or cm
            "(?!.)"          # no additional characters
        ])
        m = re.search(pattern, s)
        if m != None:
            cm_range = [150, 193]
            in_range = [59, 76]
            return Validator._validate_range(m.group(1), *(cm_range if m.group(2) == "cm" else in_range))
        return False

    def validate_hcl(s) -> bool:
        """hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f."""
        pattern = ''.join([
            "^(#)",             # starts with one #
            "([0-9a-f]{6})",    # exactly six characters 0-9 or a-f
            "(?!.)"             # no additional characters
        ])
        m = re.search(pattern, s)
        return m != None

    def validate_ecl(s) -> bool:
        """ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth."""
        pattern = ''.join([
            "(amb|blu|brn|gry|grn|hzl|oth)", # exactly one of: amb blu brn gry grn hzl oth
            "(?!.)"                          # no additional characters
        ])
        m = re.search(pattern, s)
        return m != None

    def validate_pid(s) -> bool:
        """pid (Passport ID) - a nine-digit number, including leading zeroes."""
        pattern = ''.join([
            "^(\d{9})",  # exactly 9 digits
            "(?!.)"      # no additional characters
        ])
        m = re.search(pattern, s)
        return m != None


def validate_passport(rec) -> bool:

    # solution: required fields set to validate passport
    required_fields = {
        'byr': Validator.validate_byr,
        'iyr': Validator.validate_iyr,
        'eyr': Validator.validate_eyr,
        'hgt': Validator.validate_hgt,
        'hcl': Validator.validate_hcl,
        'ecl': Validator.validate_ecl,
        'pid': Validator.validate_pid
    }

    if set(required_fields.keys()).issubset(set(rec.keys())):
        fields_valid = True
        for key, validator in required_fields.items():
            if validator != None:
                if validator(rec[key]) == False:
                     fields_valid = False
                     break
        return fields_valid
    return False


def main():
    data = load_data('input.txt', parse_passport)
    #print(len(data))
    #print(data)

    # test sample data

    # invalid
    # print(validate_passport(parse_passport("eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926")) == False)
    # print(validate_passport(parse_passport("iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946")) == False)
    # print(validate_passport(parse_passport("hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277")) == False)
    # print(validate_passport(parse_passport("hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007")) == False)
    # # valid
    # print(validate_passport(parse_passport("pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f")) == True)
    # print(validate_passport(parse_passport("eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm")) == True)
    # print(validate_passport(parse_passport("hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022")) == True)
    # print(validate_passport(parse_passport("iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719")) == True)

    # Test validators

    # print(Validator.validate_byr("2002") == True)
    # print(Validator.validate_byr("2003") == False)

    # print(Validator.validate_byr("1920") == True)
    # print(Validator.validate_byr("1919") == False)
    # print(Validator.validate_byr("2002") == True)
    # print(Validator.validate_byr("2003") == False)
    # print(Validator.validate_byr("invalid") == False)

    # print(Validator.validate_iyr("2010") == True)
    # print(Validator.validate_iyr("2009") == False)
    # print(Validator.validate_iyr("2020") == True)
    # print(Validator.validate_iyr("2021") == False)
    # print(Validator.validate_iyr("invalid") == False)

    # print(Validator.validate_hgt("60in") == True)
    # print(Validator.validate_hgt("190cm") == True)
    # print(Validator.validate_hgt("190in") == False)
    # print(Validator.validate_hgt("190") == False)

    # print(Validator.validate_hgt("150cm") == True)
    # print(Validator.validate_hgt("250cm") == False)
    # print(Validator.validate_hgt("59inch") == False)
    # print(Validator.validate_hgt("59IN") == False)
    # print(Validator.validate_hgt("invalid") == False)

    # print(Validator.validate_hcl("#123abc") == True)
    # print(Validator.validate_hcl("#123abz") == False)
    # print(Validator.validate_hcl("123abc") == False)

    # print(Validator.validate_hcl("#18171d") == True)
    # print(Validator.validate_hcl("# 18171d") == False)
    # print(Validator.validate_hcl("#18171D") == False)
    # print(Validator.validate_hcl(" #18171d") == False)
    # print(Validator.validate_hcl("#18171d0") == False)

    # print(Validator.validate_ecl("brn") == True)
    # print(Validator.validate_ecl("wat") == False)
    # print(Validator.validate_ecl("other") == False)

    # print(Validator.validate_ecl("blu") == True)
    # print(Validator.validate_ecl("yel") == False)

    # print(Validator.validate_pid("000000001") == True)
    # print(Validator.validate_pid("0123456789") == False)

    # print(Validator.validate_pid("266021118") == True)
    # print(Validator.validate_pid("26602111") == False)

    # solution - count valid passports
    valid = 0
    for rec in data:
        if validate_passport(rec):
            valid += 1

    print(f'Valid Passports: {valid}')


if __name__ == "__main__":
    main()
