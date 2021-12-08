data = open('input.txt').readlines()

positions = [[0, 0], [0, 0]]
visited = {}
visited[(0, 0)] = True
curr_santa = 0
for char in data[0]:
# for char in '^v^v^v^v^v':
    if char == '^':
        positions[curr_santa][1] += 1
    elif char == '>':
        positions[curr_santa][0] += 1
    elif char == '<':
        positions[curr_santa][0] -= 1
    elif char == 'v':
        positions[curr_santa][1] -= 1

    visited[tuple(positions[curr_santa])] = True
    curr_santa = (curr_santa + 1) % len(positions)

print(len(visited))
