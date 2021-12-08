#from numpy import genfromtxt
#a = genfromtxt('advent2-input.txt')

ans = 0
with open('advent-input.txt') as f:
    a = f.readlines()

a = a[0].split()
a = [int(i) for i in a]
#a = [0,2,7,0]

seen = {}
while True:
    if tuple(a) in seen: break
    seen[tuple(a)] = True
    index = a.index(max(a))

    disperse = a[index]
    a[index] = 0
    index  = (index + 1) % len(a)

    for i in range(disperse):
        a[index] += 1
        index = (index + 1) % len(a)

    ans += 1
print(ans)
