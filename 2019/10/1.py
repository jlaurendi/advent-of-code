import sys, os, copy, math, itertools, functools

sign = functools.partial(math.copysign, 1)

asteroids = []
grid = {}
with open('advent-input.txt') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i].strip()
        for j in range(len(line)):
            if j not in grid:
                grid[j] = {}

            if line[j] == '.':
                grid[j][i] = False
            else:
                asteroids.append((i, j))
                grid[j][i] = True

def can_see(grid, ast_1, ast_2):
    (i1, j1) = ast_1
    (i2, j2) = ast_2

    i_diff = abs(i1 - i2)
    j_diff = abs(j1 - j2)
    i_sign = sign(i1 - i2)
    j_sign = sign(j1 - j2)

    ij_gcd = math.gcd(i_diff, j_diff)

    i_step = 0 if i_diff == 0 else i_sign * i_diff / ij_gcd
    j_step = 0 if j_diff == 0 else j_sign * j_diff / ij_gcd

    for inc in range(1, ij_gcd):
        i_try = i2 + inc * i_step
        j_try = j2 + inc * j_step
        if grid[int(j_try)][int(i_try)]:
            return False

    return True


asteroid_counts = {}
for asteroid1 in asteroids:
    curr_count = 0
    for asteroid2 in asteroids:
        if asteroid1 == asteroid2:
            continue

        if can_see(grid, asteroid1, asteroid2):
            curr_count += 1

    asteroid_counts[asteroid1] = curr_count

print(max(asteroid_counts.values()))