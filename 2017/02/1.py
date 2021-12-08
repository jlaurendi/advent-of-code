from numpy import genfromtxt
a = genfromtxt('advent2-input.txt')

checksum = 0
for row in a:
    checksum += max(row) - min(row)

print(checksum)
