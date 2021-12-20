import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = os.path.join(__location__, 'input.txt')

def check_grid(grid, nums):
	n = len(grid)

	# Short circuit if there are enough nums to possibly have a bingo
	if len(nums) < n:
		return False

	# Check rows
	for row in grid:
		num_matches_row = 0
		for elt in row:
			if elt in nums:
				num_matches_row += 1
			else:
				break
		if num_matches_row == n:
			return True

	# Check columns
	for i in range(n):
		num_matches_col = 0
		for j in range(n):
			if grid[j][i] in nums:
				num_matches_col += 1
			else:
				break
		if num_matches_col == n:
			return True

	return False

def calculate_score(grid, nums):
	n = len(grid)

	unmarked_sum = 0
	for i in range(n):
		for j in range(n):
			if grid[j][i] not in nums:
				unmarked_sum += grid[j][i]
				print(grid[j][i])

	print(unmarked_sum, nums[-1])
	return unmarked_sum * nums[-1]

def print_grid(grid):
	n = len(grid)
	for i in range(n):
		print(grid[i])

def solve(input_path):
	with open(input_path) as f:
		lines = f.read()
		lines = lines.split('\n\n')

		nums = [int(elt) for elt in lines[0].split(',')]
		grids = [elt.split('\n') for elt in lines[1:]]
		grids = [[list(map(int, elt.split())) for elt in grid] for grid in grids]

	board_win_ranks = {}
	curr_rank = 1
	for i in range(5,len(nums)):
		curr_nums = nums[:i]
		# print(curr_nums)

		for i in range(len(grids)):
			grid = grids[i]
			if (i not in board_win_ranks) and check_grid(grid, curr_nums):
				board_win_ranks[i] = curr_rank
				curr_rank += 1
				if curr_rank > len(grids):
					return calculate_score(grid, curr_nums)
				# print(curr_nums)
				# print_grid(grid)
				# score = calculate_score(grid, curr_nums)

print(solve(input_path))