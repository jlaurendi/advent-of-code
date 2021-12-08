lines = open('input.txt').readlines()

total = 0
for ln in lines:
    (l, w, h) = [int(i) for i in ln.split('x')]

    total += 2 * (l * w + l * h + h * w) + min(l * w, l * h, h * w)

print(total)
