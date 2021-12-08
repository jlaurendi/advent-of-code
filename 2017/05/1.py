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
    l[curr] += 1
    curr += l[curr] - 1

    num_steps += 1

    if curr < 0 or curr > end:
        break

print(num_steps)
