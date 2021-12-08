import sys
with open('advent-input.txt') as f:
    a = f.readlines()

gen_a = 591
gen_b = 393

a_factor = 16807
b_factor = 48271

mod = 2147483647
cnt = 0
for i in range(5*10**6):
	while True:
		gen_a = gen_a * a_factor % mod
		if gen_a % 4 == 0:
			break

	while True:
		gen_b = gen_b * b_factor % mod
		if gen_b % 8 == 0:
			break

	if gen_a % 2**16 == gen_b % 2**16:
		cnt += 1

print cnt