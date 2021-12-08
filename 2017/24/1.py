import sys,math,copy
with open('advent-input.txt') as f:
# with open('advent-test.txt') as f:
    a = f.readlines()

ports = []
for ln in a:
	prt = ln.replace('\n','').split('/')
	prt = [int(a) for a in prt]
	ports.append(prt)



def paths(cur_path, ports):

	last = cur_path[-1]
	last_out = last[1]

	poss_paths = []
	i = 0
	for port in ports:

		if last_out in port:
			path = copy.deepcopy(cur_path)

			next = []
			if port[0] == last_out:
				next.append(port[0])
				next.append(port[1])
			else:
				next.append(port[1])
				next.append(port[0])

			path.append(next)

			next_ports = [elt for elt in ports if elt != port]
			poss_paths += paths(path, next_ports)
		i += 1

	# print poss_paths
	if poss_paths == []:
		return [cur_path]
	return poss_paths

paths = paths([[0,0]], ports)

strongest = 0
longest = 0
for p in paths:
	s = 0
	if len(p) > longest:
		longest = len(p)

		for e in p:
			s += e[0] + e[1]

		strongest = s
	elif len(p) == longest:
		for e in p:
			s += e[0] + e[1]
		if s > strongest:
			strongest = s




print strongest
sys.exit()
