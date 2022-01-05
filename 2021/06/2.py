import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = os.path.join(__location__, 'input.txt')
# input_path = os.path.join(__location__, 'test-input.txt')


def solve(input_path):

	# Parse input
	with open(input_path) as f:
		fish = [int(elt) for elt in f.read().split(',')]

		tmp_fish = {}
		for f in fish:
			if f not in tmp_fish:
				tmp_fish[f] = 0
			tmp_fish[f] += 1
			fish = tmp_fish
	print(fish)
	n = 256
	fish = simulate_n_days(fish, n)
	return sum(fish.values())

def simulate_n_days(fish, n):
	for i in range(n):
		tmp_fish = {}
		for num_days in fish.keys():
			if num_days == 0:

				# New fish
				tmp_fish[8] = fish[0]

				# Reset fish to 6 days
				if 6 not in tmp_fish:
					tmp_fish[6] = 0
				tmp_fish[6] += fish[0]

			else:
				if (num_days - 1) not in tmp_fish:
					tmp_fish[num_days - 1] = 0
				tmp_fish[num_days - 1] += fish[num_days]
		fish = tmp_fish
	return fish

print(solve(input_path))
