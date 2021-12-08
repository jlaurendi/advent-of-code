from sys import exit

def is_nice(s):
    constraint2 = False
    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            constraint2 = True
            constraint2index = i
            break
    if not constraint2:
        return False

    pairs = {}
    prev_char = ''
    for i in range(len(s)):
        char = s[i]

        if i == 0:
            prev_char = char
            continue

        pair = prev_char + char
        if pair in pairs and pairs[pair] != i-1:
            print(pair + "/" + s[constraint2index:constraint2index+3] + ": " + s)
            return True

        if pair not in pairs:
            pairs[pair] = i
        prev_char = char

    return False

# print(is_nice('qjhvhtzxzqqjkmpb')) # nice
# print(is_nice('xxyxx')) # nice
# print(is_nice('uurcxstgmygtbstg')) # naughty
# print(is_nice('ieiodmkazucvgmuyaaaa')) # naughty
# print(is_nice('xxxyx')) # nice


lines = open('input.txt').readlines()

num_nice = 0
for ln in lines:
    print(ln)
    if is_nice(ln):
        num_nice += 1
print(num_nice)

# 50 - wrong
