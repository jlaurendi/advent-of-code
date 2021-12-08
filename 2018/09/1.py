import sys, copy

num_p = 448
last_marble = 71628

# num_p = 9
# last_marble = 25


curr_marble = 0
marbles = [0]
curr_p = 1
scores = {}
for i in xrange(1, last_marble):
	# print curr_marble, marbles
	if i % 23 == 0:
		if curr_p not in scores:
			scores[curr_p] = 0
		scores[curr_p] += i
		curr_marble = (curr_marble - 7) % len(marbles)
		scores[curr_p] += marbles[curr_marble]
		del marbles[curr_marble]
		curr_marble = curr_marble % len(marbles)
	else:
		curr_marble = (curr_marble + 1) % len(marbles)
		curr_marble = (curr_marble + 1) % (len(marbles)+1)

		if curr_marble == 0:
			marbles.append(i)
		else:
			marbles.insert(curr_marble, i)

	curr_p = (curr_p+1) % num_p


print max(scores.values())
