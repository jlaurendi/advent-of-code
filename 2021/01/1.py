import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = os.path.join(__location__,'input.txt')

def solve_problem(input_path):
	with open(input_path) as f:
		nums = [int(ln.strip()) for ln in f.readlines()]
		# print(nums)

		prev_measurement = None
		count = 0
		for num in nums:
			if prev_measurement is not None and num > prev_measurement:
				count += 1
			prev_measurement = num

	return count

count = solve_problem(input_path)
print(count)

