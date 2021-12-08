with open('advent4-1input.txt') as f:
    a = f.readlines()
def is_anagram(a, b):
    return ''.join(sorted(a)) == ''.join(sorted(b))

num_valid = 0
for pp in a:
    p_dict = {}
    is_valid = True
    for p in pp.split():
        for p_test in p_dict:
            if is_anagram(p_test, p):
                is_valid = False
                break 
        p_dict[p] = True
    if is_valid:
        num_valid += 1

print(num_valid)

