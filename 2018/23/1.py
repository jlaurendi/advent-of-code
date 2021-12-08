import sys, copy
bots = []
with open('advent-input2.txt') as f:
	a = f.readlines()

	for i in a:
		line = i.strip().split('>, r=')
		r = int(line[1])
		p = line[0].split('pos=<')[1]
		(p1, p2, p3) = p.split(',')
		bot = [r, int(p1), int(p2), int(p3)]
		bots.append(bot)

def dist(bot1, bot2):
	d = 0
	for i in range(1,4):
		d += abs(bot1[i]-bot2[i])
	return d

bots = sorted(bots, key=lambda x: -x[0])

def does_intersect(bot1, bot2):
	if dist(bot1, bot2) <= bot1[0] + bot2[0]:
		return True
	return False

def does_all_intersect(bots):


intersections = {}
i = 0
for b1 in bots:
	intersections[i] = {}
	j = 0
	for b2 in bots:
		if b1 == b2: continue
		if does_intersect(b1, b2):
			intersections[i][j] = True
		j += 1
	i += 1

print intersections

for i in intersections:
	bot1 = bots[i]
	neighbors = intersections[i]
	print neighbors

# max_num = 0
# max_bot = None
# max_bot_neighbors = None
# for bot0 in bots:
# 	num_in_range = 0
# 	neighbors = [bot0]
# 	for bot1 in bots:
# 		if bot0 == bot1:
# 			continue
# 		d = dist(bot0, bot1)

# 		if d <= bot0[0]:
# 			num_in_range += 1
# 			neighbors.append(bot1)
# 	if num_in_range > max_num:
# 		max_num = num_in_range
# 		max_bot = bot0
# 		max_bot_neighbors = copy.deepcopy(neighbors)

# max_bot_neighbors = sorted(max_bot_neighbors, key=lambda x: x[0])
# print max_bot, max_num, max_bot_neighbors

# min_bot = max_bot_neighbors[0]
# min_bot_r = min_bot[0]
# mb_i = min_bot[1]
# mb_j = min_bot[2]
# mb_k = min_bot[3]
# min_dist = None
# for i in xrange(-min_bot_r, min_bot_r+1):
# 	if abs(i) > min_bot_r:
# 		if i > 0:
# 			break
# 		continue
# 	for j in xrange(-min_bot_r, min_bot_r+1):
# 		if abs(i) + abs(j) > min_bot_r:
# 			if j > 0:
# 				break
# 			continue
# 		for k in xrange(-min_bot_r, min_bot_r+1):
# 			d = abs(i) + abs(j) + abs(k)
# 			if d > min_bot_r:
# 				if k > 0:
# 					break
# 				continue
# 			else:
# 				num_in_range = 0
# 				fake_bot = [1, mb_i+i, mb_j+j, mb_k+k]
# 				for bot1 in max_bot_neighbors:
# 					d = dist(fake_bot, bot1)

# 					# print d, bot1, fake_bot
# 					if d <= bot1[0]:
# 						num_in_range += 1

# 				# print num_in_range, fake_bot
# 				d_to_0 = dist(fake_bot, [1, 0, 0, 0])
# 				if num_in_range == max_num and min_dist == None or d_to_0 < min_dist:
# 					min_dist = d_to_0
# 					print min_dist

# print min_dist

# def intersect(bot1, bot2):


# min_bot = max_bot_neighbors[0]
# min_bot_r = min_bot[0]
# mb_i = min_bot[1]
# mb_j = min_bot[2]
# mb_k = min_bot[3]
# min_dist = None

# coords = [0]*3
# for b in max_bot_neighbors:
# 	for c in [0, 1, 2]:
# 		coords[c] += b[c+1]
# coords = [c / len(max_bot_neighbors) for c in coords]
# curr_i = coords[0]
# curr_j = coords[1]
# curr_k = coords[2]
# while True:
# 	orig = [curr_i, curr_j, curr_k]
# 	print orig
# 	while True and curr_i != 0:
# 		curr_i = curr_i-1 if curr_i > 0 else curr_i+1
# 		done = False
# 		for bot in max_bot_neighbors:
# 			if dist(bot, [0, curr_i, curr_j, curr_k]) > bot[0]:
# 				curr_i = curr_i+1 if curr_i > 0 else curr_i-1
# 				done = True
# 				break
# 		if done:
# 			break

# 	while True and curr_j != 0:
# 		curr_j = curr_j-1 if curr_j > 0 else curr_j+1
# 		done = False
# 		for bot in max_bot_neighbors:
# 			if dist(bot, [0, curr_i, curr_j, curr_k]) > bot[0]:
# 				curr_j = curr_j+1 if curr_j > 0 else curr_j-1
# 				done = True
# 				break
# 		if done:
# 			break

# 	while True and curr_k != 0:
# 		curr_k = curr_k-1 if curr_k > 0 else curr_k-1
# 		done = False
# 		for bot in max_bot_neighbors:
# 			if dist(bot, [0, curr_i, curr_j, curr_k]) > bot[0]:
# 				curr_k = curr_k+1 if curr_k > 0 else curr_k-1
# 				done = True
# 				break
# 		if done:
# 			break

# 	print orig
# 	if orig == [curr_i, curr_j, curr_k]:
# 		break

# print [curr_i, curr_j, curr_k]
# print dist([0, curr_i, curr_j, curr_k], [0, 0, 0, 0])