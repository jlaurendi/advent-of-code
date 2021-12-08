import sys, copy

deps = []
dependencies = {}
nodes = set()
adj_list = {}
with open('advent-input.txt') as f:
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

num_workers = 5
workers = [0] * num_workers
workers_nodes = [''] * num_workers
time = 0
n = curr_nodes[0]
while True:

	for i in xrange(num_workers):
		if workers[i] > 0:
			workers[i] -= 1

			if workers[i] == 0:
				n = workers_nodes[i]
				final_order.append(n)
				if n in adj_list:
					for nn in adj_list[n]:
						add_to_list = True
						if nn not in final_order:
							for d in dependencies[nn]:
								if d not in final_order:
									add_to_list = False
						else:
							add_to_list = False

						if add_to_list and nn not in curr_nodes:
							curr_nodes.extend(nn)

				curr_nodes = sorted(curr_nodes)


	for i in xrange(len(workers)):
		if workers[i] == 0:
			if len(curr_nodes) == 0:
				break
			nxt = curr_nodes[0]
			workers[i] = 60 + ord(nxt.upper())-64
			workers_nodes[i] = nxt

			curr_nodes.remove(nxt)


	done = True
	for i in xrange(len(workers)):
		if workers[i] != 0:
			done = False

	# print workers
	if done:
		break
	time += 1

print time

output = ''
for i in final_order:
	output += i
