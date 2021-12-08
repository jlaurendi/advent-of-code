with open('advent5-1input.txt') as f:
    a = f.readlines()

l = []
#a = ['0', '3', '0', '1', '-3']
for elt in a:
    l.append(int(elt.strip()))

curr = 0
end = len(l)-1
num_steps = 0

while True:
    old_curr = l[curr]
    if l[curr] >= 3:
        l[curr] -= 1
    else:
        l[curr] += 1
    curr += old_curr

    num_steps += 1

    if curr < 0 or curr > end:
        break

print(num_steps)
