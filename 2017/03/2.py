import sys
input_value = int(raw_input("Input value: "))
i = 1
direction = "R"
dir_map = {"L": "D", "D": "R", "R": "U", "U": "L"}
num_moves_in_direction = 1
num_moves_iter_num = 0
cur_row = 0
cur_col = 0

grid_values = { 0: { 0: 1 } }

while True:

    for i in range(num_moves_in_direction):
        if direction == "R":
            cur_row += 1
        elif direction == "L":
            cur_row -= 1
        elif direction == "U":
            cur_col += 1
        elif direction == "D":
            cur_col -= 1

        val = 0

        if cur_row in grid_values:
            row = grid_values[cur_row]
            if cur_col in row:
                val += row[cur_col]
            if (cur_col-1) in row:
                val += row[cur_col-1]
            if (cur_col+1) in row:
                val += row[cur_col+1]
        if (cur_row-1) in grid_values:
            row = grid_values[cur_row-1]
            if cur_col in row:
                val += row[cur_col]
            if (cur_col-1) in row:
                val += row[cur_col-1]
            if (cur_col+1) in row:
                 val += row[cur_col+1]
        if (cur_row+1) in grid_values:
            row = grid_values[cur_row+1]
            if cur_col in row:
                 val += row[cur_col]
            if (cur_col-1) in row:
                 val += row[cur_col-1]
            if (cur_col+1) in row:
                 val += row[cur_col+1]

        if cur_row not in grid_values: grid_values[cur_row] = {}
        grid_values[cur_row][cur_col] = val

        print(val)
        print("\n")
        if val > input_value:
            print("The answer:"+ str(val))
            sys.exit()

    direction = dir_map[direction]
    num_moves_iter_num += 1
    if num_moves_iter_num == 2:
        num_moves_in_direction += 1
        num_moves_iter_num = 0
