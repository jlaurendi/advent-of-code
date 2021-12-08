import sys
with open('advent-input.txt') as f:
    a = f.readlines()

# p=<39	3,-398,17>, v=<-28,127,-9>, a=<0,-13,1>

pos = []
vel = []
acc = []
order = []
for ln in a:
	p,v,a = ln.split(', ')
	p = [int(i) for i in p[3:len(p)-1].split(',')]
	v = [int(i) for i in v[3:len(v)-1].split(',')]
	a = [int(i.replace(">","")) for i in a[3:len(a)-1].split(',')]

	pos.append(p)
	vel.append(v)
	acc.append(a)


cur_max = 100000
consider = []
for i in xrange(len(acc)):
	ac = acc[i]
	if abs(ac[0]) + abs(ac[1]) + abs(ac[2]) < cur_max:
		cur_max = abs(ac[0]) + abs(ac[1]) + abs(ac[2])
		consider = []
		consider.append(i)
	elif abs(ac[0]) + abs(ac[1]) + abs(ac[2]) == cur_max:
		consider.append(i)

if len(consider) == 1:
	print consider
	sys.exit()

print consider

cur_max = 100000
consider2 = []
for i in consider:
	ve = vel[i]
	d = abs(ve[0]) + abs(ve[1]) + abs(ve[2])
	if d < cur_max:
		cur_max = d
		consider2 = []
		consider2.append(i)
	elif d == cur_max:
		consider2.append(i)

if len(consider2) == 1:
	print consider2
	sys.exit()

print consider2

cur_max = 100000
consider3 = []
for i in consider2:
	po = pos[i]
	d = abs(po[0]) + abs(po[1]) + abs(po[2])
	if d < cur_max:
		cur_max = d
		consider3 = []
		consider3.append(i)
	elif d == cur_max:
		consider3.append(i)

if len(consider3) == 1:
	print consider3
	sys.exit()
print consider3