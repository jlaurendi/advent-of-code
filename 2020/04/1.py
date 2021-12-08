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

def calc_num_valid(passports):
    num_valid = 0
    for p in passports:
        if len(p) == 8 or (len(p) == 7 and 'cid' not in p):
            num_valid += 1
    return num_valid

num_valid = calc_num_valid(passports)
print(num_valid)

# 244 - too low