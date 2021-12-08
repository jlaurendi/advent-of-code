from sys import exit
lines = open('input.txt').readlines()


grid = {}
for ln in lines:
    mode = None

    if "turn on" in ln:
        mode = "on"
    elif "turn off" in ln:
        mode = "off"
    elif "toggle" in ln:
        mode = "toggle"

    ln = ln.replace('turn on', '').replace('turn off', '').replace('toggle', '').strip()
    parts = ln.split(' through ')
    (i0, j0) = [int(i) for i in parts[0].split(',')]
    (i1, j1) = [int(i) for i in parts[1].split(',')]

    for i in range(i0, i1+1):
        if i not in grid:
            grid[i] = {}

        for j in range(j0, j1+1):
            if j not in grid[i]:
                grid[i][j] = 0

            if mode == "on":
                grid[i][j] += 1

            elif mode == "off":
                grid[i][j] -= 1
                grid[i][j] = max(grid[i][j], 0)

            elif mode == "toggle":
                grid[i][j] += 2

            else:
                "ERROR wrong mode " + mode
                exit()

brightness = 0
for i in grid:
    row = grid[i]
    for j in row:
        brightness += row[j]
print(brightness)