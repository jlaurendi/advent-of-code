import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = os.path.join(__location__, 'input.txt')

def array_to_binary(arr):
	result = 0
	n = len(arr)
	for i in range(len(arr)):
		result += 2**(n-i-1) * arr[i]
	return result

def get_oxy_rating(lines):
	i = 0
	while len(lines) > 1:
		mid = len(lines) / 2
		summed = 0
		new_lines = []
		for ln in lines:
			summed += int(ln[i])

		target = 1 if summed >= mid else 0
		for ln in lines:
			if ln[i] == target:
				new_lines.append(ln)

		i += 1
		lines = new_lines
	return array_to_binary(lines[0])

def get_co2_rating(lines):
	i = 0
	while len(lines) > 1:
		mid = len(lines) / 2
		summed = 0
		new_lines = []
		for ln in lines:
			summed += int(ln[i])

		target = 1 if summed < mid else 0
		for ln in lines:
			if ln[i] == target:
				new_lines.append(ln)

		i += 1
		lines = new_lines
	return array_to_binary(lines[0])

def solve(input_path):
	with open(input_path) as f:
		lines = [list(map(int, ln.split()[0])) for ln in f.readlines()]

	oxy_rating = get_oxy_rating(lines)
	co2_rating = get_co2_rating(lines)

	print(oxy_rating, co2_rating)
	return oxy_rating * co2_rating


print(solve(input_path))