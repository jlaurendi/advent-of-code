import sys, copy

limit = '505961'
# limit = '51589'
# limit = '1245'
# limit = '92510'
# limit = '59414'
recipes = '37'
p0 = 0
p1 = 1

s = ''
i = 0
curr_trailing = recipes[:]
while True:
	i+=1
	r0 = recipes[p0]
	r1 = recipes[p1]
	new_recipes = str(int(r0)+int(r1))
	for rec in new_recipes:
		recipes+=rec
		# print recipes

	p0 = (p0+int(r0)+1) % len(recipes)
	p1 = (p1+int(r1)+1) % len(recipes)


	# curr = recipes[len(recipes)-len(limit):]
	# curr = [str(i) for i in curr]
	# curr = ''.join(curr)
	# print curr, limit
	# print recipes, limit
	if recipes[len(recipes)-len(limit):] == limit:
		print len(recipes)-len(limit)
		sys.exit()
		break
	elif recipes[len(recipes)-len(limit)-1:-1] == limit:
		print len(recipes)-len(limit)-1
		sys.exit()

print recipes

