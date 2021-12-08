#from numpy import genfromtxt
#a = genfromtxt('advent2-input.txt')
import sys
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
	nodes[node] = {'children': children, 'weight': weight, 'total_weight': None}


for n in all_nodes:
	if n not in all_children:
		root = n

def calc_weights(n, nodes):
	if nodes == []:
		return 0
	else:
		childrens_weight = sum([calc_weights(c, nodes) for c in nodes[n]['children']])
		curr_node_weight = nodes[n]['weight'] + childrens_weight
		nodes[n]['total_weight'] = curr_node_weight
		return curr_node_weight

calc_weights(root, nodes)

curr_node = root
curr_children_dict = {}
diff_needed = None
while True:
	children = nodes[curr_node]['children']
	curr_children_dict = {}
	for c in children:
		if nodes[c]['total_weight'] not in curr_children_dict:
			curr_children_dict[nodes[c]['total_weight']] = [c]
		else:
			curr_children_dict[nodes[c]['total_weight']].append(c)

	found = False
	for c in curr_children_dict:
		if len(curr_children_dict[c]) == 1:
			found = True
			curr_node = curr_children_dict[c][0]
			diff_top = c
		else:
			diff_bottom = c

	if diff_needed == None:
		diff_needed = diff_top - diff_bottom

	if not found:
		print nodes[curr_node]['weight'] - diff_needed
		sys.exit()
