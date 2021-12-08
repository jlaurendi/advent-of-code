import sys, os, copy
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = os.path.join(__location__,'input.txt')


with open(input_path) as f:

    nums = [int(elt) for elt in f.readlines()]

nums.sort()

found = False
for a in nums:
    for b in nums:
        if a + b == 2020:
            found = True
            break
        elif a + b >= 2020:
            break

    if found:
        break

print(a, b)
print(a * b)
