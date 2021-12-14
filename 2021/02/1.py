import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = os.path.join(__location__,'input.txt')

def solve_problem(input_path):
	with open(input_path) as f:
		moves = [ln.split() for ln in f.readlines()]

	curr_location = [0,0]
	aim = 0
	for mv in moves:
		direction = mv[0]
		length = int(mv[1])

		curr_location[0] += length if direction == 'forward' else 0
		curr_location[1] += length * aim if direction == 'forward' else 0
		aim += length if direction == 'down' else 0
		aim -= length if direction == 'up' else 0

	return curr_location[0] * curr_location[1]

answer = solve_problem(input_path)
print(answer)