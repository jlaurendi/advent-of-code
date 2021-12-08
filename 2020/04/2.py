import sys, os, copy
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = os.path.join(__location__,'input.txt')

passports = []
with open(input_path) as f:
    lns = f.readlines()

    passport = {}
    for ln in lns:
        ln = ln.strip()
        if ln == '':
            passports.append(passport)
            passport = {}
            continue

        lnsplit = ln.split(' ')
        for cred in lnsplit:
            (name, value) = cred.split(':')
            passport[name] = value
    passports.append(passport)

def is_cred_valid(cred_name, cred_value):
    if cred_name == 'byr':
        return cred_value.isdigit() and int(cred_value) >= 1920 and int(cred_value) <= 2002

    elif cred_name == 'iyr':
        return cred_value.isdigit() and int(cred_value) >= 2010 and int(cred_value) <= 2020

    elif cred_name == 'eyr':
        return cred_value.isdigit() and int(cred_value) >= 2020 and int(cred_value) <= 2030

    elif cred_name == 'hgt':
        if len(cred_value) < 2:
            return False
        l = len(cred_value)
        units = cred_value[l-2:]
        val = cred_value[:l-2]

        if not val.isdigit():
            return False

        val = int(val)
        return (units == 'in' and val >= 59 and val <= 76) or (units == 'cm' and val >= 150 and val <= 193)

    elif cred_name == 'hcl':
        if len(cred_value) != 7 or cred_value[0] != '#':
            return False

        val = cred_value[1:]
        valid_chars = list(range(10)) + ['a', 'b', 'c', 'd', 'e', 'f']
        print(valid_chars)
        for ch in val:
            if ch.isdigit():
                ch = int(ch)
            if ch not in valid_chars:
                print(ch)
                return False
        return True

    elif cred_name == 'ecl':
        return cred_value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    elif cred_name == 'pid':
        if len(cred_value) != 9 or not cred_value.isdigit():
            return False

        for ch in cred_value:
            if int(ch) not in list(range(10)):
                return False
        return True

    elif cred_name == 'cid':
        return True

    else:
        raise Exception("Invalid cred name: " + cred_name)

def calc_num_valid(passports):
    num_valid = 0
    for p in passports:

        valid = False
        if len(p) == 8 or (len(p) == 7 and 'cid' not in p):
            valid = True
            for cred in p:
                value = p[cred]
                if not is_cred_valid(cred, value):
                    print(cred, value, p)
                    valid = False
                    break
        num_valid += 1 if valid else 0

    return num_valid

num_valid = calc_num_valid(passports)
print(num_valid)

