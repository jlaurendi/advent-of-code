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
                asteroids.append((j, i))
                grid[j][i] = True

def can_see(grid, ast_1, ast_2):
    (j1, i1) = ast_1
    (j2, i2) = ast_2

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

def get_next_to_destroy(grid, asteroids, center, target_angle):
    min_angle_past_target = None
    min_angle_past_target_ast = None
    min_angle_past_zero = None
    min_angle_past_zero_ast = None

    for ast in asteroids:
        if not can_see(grid, center, ast) or ast == center:
            continue

        curr_angle = calculate_angle(center, ast)
        if target_angle is not None and (
            curr_angle > target_angle
                and (min_angle_past_target is None or curr_angle < min_angle_past_target)
        ):
            min_angle_past_target = curr_angle
            min_angle_past_target_ast = ast
        elif min_angle_past_zero_ast is None or curr_angle < min_angle_past_zero:
            min_angle_past_zero = curr_angle
            min_angle_past_zero_ast = ast

    # print(min_angle_past_target_ast)
    # print(min_angle_past_zero_ast)
    if min_angle_past_target_ast is None:
        return min_angle_past_zero_ast
    else:
        return min_angle_past_target_ast

# tan theta = (x2 - x1) / (y1 - y2)
def calculate_angle(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    xdiff = x2 - x1
    ydiff = y2 - y1

    if y1 == y2:
        if x1 == x2:
            return 0


        elif x2 > x1:
            return 90
        else:
            return 270
    elif x1 == x2:
        if y2 > y1:
            return 180
        else:
            return 0

    if x2 > x1:
        if y2 > y1:
            base_angle = 90
            partial_angle = math.atan(ydiff / xdiff)
        else:
            base_angle = 0
            partial_angle = math.atan(xdiff / ydiff)
    else:
        if y2 > y1:
            base_angle = 180
            partial_angle = math.atan(ydiff / xdiff)
        else:
            base_angle = 270
            partial_angle = math.atan(ydiff / xdiff)

    return base_angle + abs(math.degrees(partial_angle))


asteroid_counts = {}
for asteroid1 in asteroids:
    curr_count = 0
    for asteroid2 in asteroids:
        if asteroid1 == asteroid2:
            continue

        if can_see(grid, asteroid1, asteroid2):
            curr_count += 1

    asteroid_counts[asteroid1] = curr_count

center = max(asteroid_counts, key=asteroid_counts.get)
curr_angle = None
num_destroyed = 0

while True:

    next_asteroid = get_next_to_destroy(grid, asteroids, center, curr_angle)
    curr_angle = calculate_angle(center, next_asteroid)

    grid[next_asteroid[0]][next_asteroid[1]] = False
    asteroids.remove(next_asteroid)
    num_destroyed += 1
    # print("Asteroid - ", num_destroyed)
    # print(curr_angle)
    # print(next_asteroid)
    # if num_destroyed in [1,2,3,10,20,50,100,199,200,201,299]:
    #     print(next_asteroid)

    if num_destroyed == 200:
        # print(asteroids)
        break


x = next_asteroid[0]
y = next_asteroid[1]
answer = 100 * x + y
print(x, y)
print(answer)