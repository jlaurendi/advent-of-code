import sys, math
with open('advent-input.txt') as f:
# with open('avent-test.txt') as f:
    a = f.readlines()

pos = []
vel = []
acc = []
order = []
parts = []
idx = 0
for ln in a:
	p,v,a = ln.split(', ')
	p = p.replace("<","").replace(">","").replace('p=','').split(',')
	v = v.replace("<","").replace(">","").replace('v=','').split(',')
	a = a.replace("<","").replace(">","").replace('a=','').split(',')

	p = [int(i) for i in p]
	v = [int(i) for i in v]
	a = [int(i) for i in a]

	pos.append(p)
	vel.append(v)
	acc.append(a)
	parts.append(idx)
	idx+=1

last = len(parts)
i=0
while True:
	# print i

	seen = {}
	elts_to_remove = set()
	# print parts
	for j in parts:
		for _k in seen:
			k = seen[_k]
			if (k[0] == pos[j][0]) and (k[1] == pos[j][1]) and (k[2] == pos[j][2]):
				elts_to_remove.add(j)
				elts_to_remove.add(_k)

		seen[j] = pos[j]
		# print seen

	for j in parts:
		for k in [0,1,2]:
			vel[j][k] += int(acc[j][k])
			pos[j][k] += int(vel[j][k])


	i+=1
	# print elts_to_remove
	parts = [e for e in parts if e not in elts_to_remove]
	if len(parts) != last:
		last = len(parts)
		print len(parts)

	if i > 2000:
		sys.exit()
