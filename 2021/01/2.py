import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = os.path.join(__location__,'input.txt')

def solve_problem(input_path):
	with open(input_path) as f:
		nums = [int(ln.strip()) for ln in f.readlines()]

		prev_measurement = None
		count = 0
		for i in range(len(nums) - 2):
			curr_measurement = nums[i] + nums[i + 1] + nums[i + 2]
			if prev_measurement is not None and curr_measurement > prev_measurement:
				count += 1
			prev_measurement = curr_measurement

	return count


count = solve_problem(input_path)
print(count)
