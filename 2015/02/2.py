lines = open('input.txt').readlines()

total = 0
for ln in lines:
    (l, w, h) = [int(i) for i in ln.split('x')]

    total += l * w * h
    total += 2 * min(l+w, l+h, w+h)

print(total)
