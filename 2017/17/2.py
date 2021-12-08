import sys

num_steps = 363

curr = 0
buf_len = 1
elt_aft_0 = None
for i in xrange(50000000):

	curr = (curr + num_steps + 1) % buf_len

	if curr == 0:
		elt_aft_0 = i+1

	buf_len += 1


print elt_aft_0