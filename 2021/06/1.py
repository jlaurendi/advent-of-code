import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = os.path.join(__location__, 'input.txt')
# input_path = os.path.join(__location__, 'test-input.txt')


def solve(input_path):

	# Parse input
	with open(input_path) as f:
		fish = [int(elt) for elt in f.read().split(',')]
		# fish = dict(zip(range(len(fish)), fish))
		fish = { i: elt for (i, elt) in enumerate(fish) }

	n = 80
	fish = simulate_n_days(fish, n)
	return len(fish)

def simulate_n_days(fish, n):
	next_dict_key = max(fish.keys()) + 1
	for i in range(n):
		for fish_idx in range(len(fish)):
			if fish[fish_idx] == 0:
				fish[next_dict_key] = 8
				next_dict_key += 1
				fish[fish_idx] = 6
			else:
				fish[fish_idx] -= 1

	return fish

print(solve(input_path))
