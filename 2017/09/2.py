import sys
with open('advent-input.txt') as f:
    a = f.readlines()[0]

print a
depth = 1
total = 0
garbage = False
ignore = False

cnt = 0
for char in a:
	if ignore:
		ignore = False
		continue

	if char == "!":
		ignore = True
	elif not garbage and char == "<":
		garbage = True
	elif char == ">":
		garbage = False
	elif not garbage and char == "{":
		total += depth
		print depth
		depth += 1
	elif not garbage and char == "}":
		depth -= 1
	elif garbage:
		cnt += 1

print cnt