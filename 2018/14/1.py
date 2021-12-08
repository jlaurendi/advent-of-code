import sys, copy

limit = 505961

recipes = [3,7]
p0 = 0
p1 = 1

while True:
	r0 = recipes[p0]
	r1 = recipes[p1]
	new_recipes = str(r0+r1)
	for rec in new_recipes:
		recipes.append(int(rec))

	p0 = (p0+r0+1) % len(recipes)
	p1 = (p1+r1+1) % len(recipes)


	if len(recipes) > limit+10:
		break


ans = recipes[limit:limit+10]
ans = [str(i) for i in ans]
print ''.join(ans)
