import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = os.path.join(__location__, 'input.txt')


def solve(input_path):
	with open(input_path) as f:
		lines = [list(map(int, ln.split()[0])) for ln in f.readlines()]

	summed = [0] * len(lines[0])
	for ln in lines:
		for i in range(len(ln)):
			summed[i] += int(ln[i])

	mid = len(lines) / 2
	gamma, epsilon = 0, 0
	n = len(summed)
	for i in range(len(summed)):
		gamma_indicator = 1 if summed[i] > mid else 0
		epsilon_indicator = 1 if summed[i] < mid else 0
		gamma += 2**(n-i-1) * gamma_indicator
		epsilon += 2**(n-i-1) * epsilon_indicator

	print(gamma, epsilon)
	return gamma * epsilon


print(solve(input_path))