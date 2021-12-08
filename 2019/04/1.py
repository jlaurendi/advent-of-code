import sys, os, copy, math

low = 134792
high = 675810

def is_valid(password):
    str_p = str(password)
    prev_c = None
    adj_found = False
    for i in xrange(len(str_p)):
        c = str_p[i]

        if c == prev_c:
            adj_found = True

        if prev_c != None and c < prev_c:
            return False

        prev_c = c

    return adj_found

num_valid = 0
for i in xrange(low, high + 1):
    if is_valid(i):
        num_valid += 1

print num_valid

