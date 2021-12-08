import sys, os, copy, math

low = 134792
high = 675810

def is_valid(password):
    str_p = str(password)
    prev_c = None
    adj_found = False
    curr_run = ''
    for i in xrange(len(str_p)):
        c = str_p[i]

        if c == prev_c:
            curr_run += c
        else:
            if len(curr_run) == 2:
                adj_found = True
            curr_run = c

        if prev_c != None and c < prev_c:
            return False

        prev_c = c

    if len(curr_run) == 2:
        adj_found = True

    return adj_found

num_valid = 0
for i in xrange(low, high + 1):
    if is_valid(i):
        num_valid += 1

print num_valid


#915 too low
#1666 too high
#1749 too high (duh)