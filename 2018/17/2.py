import sys, copy

grid = {}
grid[500] = {}
grid[500][0] = '+'
min_y = None
max_y = None
min_x = None
max_x = None

with open('advent-input2.txt') as f:
    a = f.readlines()

    for line in a:
        # print line
        line = line.split(',')
        part1 = line[0]
        part2 = line[1]
        # print part1, part2
        if part1[0] == 'x':
            x = int(part1[2:])
            y = part2.strip()[2:].split('..')
            if x not in grid:
                grid[x] = {}
            for i in range(int(y[0]), int(y[1])+1):
                grid[x][i] = '#'

                if i < min_y or min_y == None:
                    min_y = i
                if i > max_y or max_y == None:
                    max_y = i

            if min_x == None or x < min_x:
                min_x = x
            if max_x == None or x > max_x:
                max_x = x
        else:
            y = int(part1[2:])
            x = part2.strip()[2:].split('..')
            for i in range(int(x[0]), int(x[1])+1):
                if i not in grid:
                    grid[i] = {}
                grid[i][y] = '#'

                if min_x == None or i < min_x:
                    min_x = i
                if max_x == None or i > max_x:
                    max_x = i

            if y < min_y or min_y == None:
                min_y = y
            if y > max_y or max_y == None:
                max_y = y



reachable_tiles = {}
curr_options = [[500,0,'D']]
opts_explored = set()

def print_grid():
    if None in [min_y,max_y,min_x,max_x]:
        return
    y = min_y
    while y <= max_y:

        x = min_x
        s = ''
        while x <= max_x:
            if x not in grid:
                grid[x] = {}
            if y not in grid[x]:
                grid[x][y] = '.'

            if (x,y) in reachable_tiles:
                s += '|'
            else:
                s += grid[x][y]
            x += 1

        print s

        y += 1
# print grid
# sys.exit()
while True:
    # print_grid()
    # print len(curr_options)
    if len(curr_options) == 0:
        break
    for opt in curr_options:
        curr_options.remove(opt)
        if (opt[0],opt[1]) in opts_explored: continue
        opts_explored.add((opt[0],opt[1]))
        curr_x = int(opt[0])
        curr_y = int(opt[1])
        mode = opt[2]

        if curr_x not in grid:
            grid[curr_x] = {}
        if curr_y+1 not in grid[curr_x]:
            grid[curr_x][curr_y+1] = '.'

        if (curr_x, curr_y) not in reachable_tiles:
            if curr_y >= min_y and curr_y <= max_y:
                reachable_tiles[(curr_x, curr_y)] = 1

        if curr_y >= max_y:
            continue

        if grid[curr_x][curr_y+1] == '#' or grid[curr_x][curr_y+1] == '~':
            orig_x = curr_x

            while True:
                curr_x = orig_x
                right_wall = False
                left_wall = False
                water_to_add = []
                if (orig_x, curr_y) not in reachable_tiles:
                    if curr_y >= min_y and curr_y <= max_y:
                        reachable_tiles[(orig_x, curr_y)] = 1
                while True:
                    curr_x += 1

                    if curr_x not in grid:
                        grid[curr_x] = {}
                    if curr_y not in grid[curr_x]:
                        grid[curr_x][curr_y] = '.'

                    if grid[curr_x][curr_y] == '#':
                        right_wall = True
                        break

                    water_to_add.append((curr_x,curr_y))

                    if (curr_x, curr_y) not in reachable_tiles:
                        if curr_y >= min_y and curr_y <= max_y:
                            reachable_tiles[(curr_x, curr_y)] = 1

                    if curr_y+1 not in grid[curr_x] or grid[curr_x][curr_y+1] == '.':
                        curr_options.append([curr_x,curr_y+1,'D'])
                        break

                curr_x = orig_x

                while True:
                    curr_x -= 1
                    if curr_x not in grid:
                        grid[curr_x] = {}
                    if curr_y not in grid[curr_x]:
                        grid[curr_x][curr_y] = '.'

                    if grid[curr_x][curr_y] == '#':
                        left_wall = True
                        break

                    water_to_add.append((curr_x,curr_y))

                    if (curr_x, curr_y) not in reachable_tiles:
                        if curr_y >= min_y and curr_y <= max_y:
                            reachable_tiles[(curr_x, curr_y)] = 1

                    if curr_y+1 not in grid[curr_x] or grid[curr_x][curr_y+1] == '.':
                        curr_options.append([curr_x,curr_y+1,'D'])
                        break

                if left_wall and right_wall:
                    water_to_add.append((orig_x,curr_y))

                    curr_y -= 1
                    for (x,y) in water_to_add:
                        grid[x][y] = '~'
                else:
                    break

        else:
            curr_options.append([curr_x,curr_y+1,'D'])

print len(reachable_tiles.keys())



# reachable_tiles = sorted(reachable_tiles, key=lambda x: x[0])

# print len(reachable_tiles)
# print_grid()
# 659, 679, 29591, 29741

num_water = 0
for x in grid:
    for y in grid[x]:
        if grid[x][y] == '~':
            num_water += 1
print num_water