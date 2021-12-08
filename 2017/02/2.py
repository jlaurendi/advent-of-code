from numpy import genfromtxt
a = genfromtxt('advent2-input.txt')
#a = genfromtxt('advent2-test2.txt')

checksum = 0
for row in a:
    div_result = 0
    for curr_i, elt in enumerate(row):
        if div_result > 0:
            break
        for i in range(len(row)):
            if (elt % row[i]) == 0 and curr_i != i:
                div_result = elt / row[i]
                break
    checksum += div_result

print(checksum)
