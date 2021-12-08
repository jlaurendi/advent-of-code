d = 'cqjxjnds'
d = 'cqjxxyzz' # part 2

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def is_valid_password(p):
    if 'i' in p or 'o' in p or 'l' in p:
        return False


    num_pairs = 0
    streak = False
    i = 0
    pairs = {}
    while i < len(p)-1:
        if i+2 < len(p) and ord(p[i]) == ord(p[i+1])-1 and ord(p[i]) == ord(p[i+2])-2:
            streak = True

        if p[i] == p[i+1] and (i-1) not in pairs:
            pairs[i] = True
            num_pairs += 1

        i += 1

    if num_pairs < 2 or not streak:
        return False
    return True

def increment_string(s):
    result = list(s)

    char = result[-1]
    i = len(s)-1
    while ord(char) == 122 and i >= 0:
        result[i] = 'a'

        i -= 1
        if i >= 0:
            char = result[i]

    if i >= 0:
        result[i] = chr(ord(char)+1)

    return "".join(result)

# print(is_valid_password('ghjaabcc'))
# print(is_valid_password('cqjxjnds'))
# print(is_valid_password('abcdffaa'))

d = increment_string(d)
while not is_valid_password(d):
    d = increment_string(d)
    # print(d)

print(d)