with open('advent4-1input.txt') as f:
    a = f.readlines()

num_valid = 0
for pp in a:
    p_dict = {}
    is_valid = True
    for p in pp.split():
        if p in p_dict:
            is_valid = False
            break
        else:
            p_dict[p] = True
    if is_valid:
        num_valid += 1

print(num_valid)

