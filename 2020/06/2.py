import os, copy, sys
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = os.path.join(__location__,'input.txt')

groups = []
with open(input_path) as f:
    lns = f.readlines()

    group = []
    for ln in lns:
        if ln == "\n":
            groups.append(group)
            group = []
            continue
        group.append(ln.strip())
groups.append(group)

print(groups)

def count(group):
    uniq_qs = {}

    for person in group:
        for ch in person:
            if ch not in uniq_qs:
                uniq_qs[ch] = 0
            uniq_qs[ch] += 1

    result = 0
    for q in uniq_qs:
        if uniq_qs[q] == len(group):
            result += 1

    return result


answer = 0
for g in groups:
    answer += count(g)

print(answer)


# 6265 - too low