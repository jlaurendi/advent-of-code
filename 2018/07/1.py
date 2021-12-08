import sys, copy

deps = []
dependencies = {}
nodes = set()
adj_list = {}
with open('advent-input2.txt') as f:
	a = f.readlines()
	for i in a:
		step1 = i.split('Step ')[1]
		step1 = step1.split(' must')[0]

		step2 = i.split('before step ')[1]
		step2 = step2.split(' can')[0]

		deps.append((step1, step2))
		nodes.add(step1)
		nodes.add(step2)

		if step1 not in adj_list:
			adj_list[step1] = []
		adj_list[step1].append(step2)

		if step2 not in dependencies:
			dependencies[step2] = []
		dependencies[step2].append(step1)

final_order = []
sources = copy.deepcopy(nodes)

for (i, j) in deps:
	if j in sources:
		sources.remove(j)

sources = sorted(sources)
curr_nodes = copy.deepcopy(sources)

while len(curr_nodes) > 0:
	n = curr_nodes[0]
	if n in final_order:
		curr_nodes.remove(n)
		continue
	final_order.append(n)
	curr_nodes.remove(n)

	if n in adj_list:
		for nn in adj_list[n]:
			add_to_list = True
			if nn not in final_order:
				for d in dependencies[nn]:
					if d not in final_order:
						add_to_list = False
			else:
				add_to_list = False

			if add_to_list:
				curr_nodes.extend(nn)

	curr_nodes = sorted(curr_nodes)
	print curr_nodes

output = ''
for i in final_order:
	output += i
print output