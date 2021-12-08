#from numpy import genfromtxt
#a = genfromtxt('advent2-input.txt')

ans = 0
with open('advent-input.txt') as f:
    a = f.readlines()

nodes = {}
all_nodes = []
all_children = []
for ln in a:
	parts = ln.split()
	node = parts[0]
	weight = int(parts[1].replace("(","").replace(")",""))

	children = []
	if len(parts) > 2:
		children = [a.replace(",", "") for a in parts[3:]]


	all_nodes.append(node)
	all_children += children
	nodes[node] = {'children': children, 'weight': weight, 'd': None}


for n in all_nodes:
	if n not in all_children:
		root = n

print root