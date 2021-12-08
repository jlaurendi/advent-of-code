import sys

num_steps = 363

buf = [0]
curr = 0
for i in xrange(2017):

	curr = (curr + num_steps) % len(buf)

	buf.insert(curr+1, i+1)

	curr = (curr + 1) % len(buf)


print buf
print buf[(buf.index(2017)+1)%len(buf)]