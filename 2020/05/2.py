import sys, os, copy
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = os.path.join(__location__,'input.txt')

passes = []
with open(input_path) as f:
    passes = [ln.strip() for ln in f.readlines()]
    passes = [(ln[:7], ln[7:]) for ln in passes]

def get_seat_id(row, col):
    return row * 8 + col

def get_row(row_code):
    output = 0
    power = len(row_code)-1
    for bit in row_code:
        if bit == 'B':
            output += 2**power

        power -= 1
    return output

def get_col(col_code):
    output = 0
    power = len(col_code)-1
    for bit in col_code:
        if bit == 'R':
            output += 2**power

        power -= 1
    return output

# print(get_row('BFFFBBF'))
# print(get_col('RRR'))
# print(get_seat_id(get_row('BFFFBBF'), get_col('RRR')))

seats_filled = {}
max_seat = None
max_seat_id = 0
for p in passes:
    row = get_row(p[0])
    col = get_col(p[1])
    curr_seat_id = get_seat_id(row, col)
    if curr_seat_id > max_seat_id:
        max_seat_id = curr_seat_id
        max_seat = (row, col)
    seats_filled[curr_seat_id] = True

for i in range(max_seat_id):
    prv = i-1
    nxt = i+1
    if i not in seats_filled and prv in seats_filled and nxt in seats_filled:
        print(i)
        sys.exit()



