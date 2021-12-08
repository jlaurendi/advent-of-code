import sys, copy
with open('advent-input.txt') as f:
	a = f.readlines()[0].split(' ')
	a = [int(i) for i in a]

tree = {}
i = 0
node_num = 0
q = [0]
curr_stack = []
meta_sum = 0
stack_pop = False
while i < len(a):
	# print curr_stack, q
	while stack_pop:
		if len(curr_stack) == 0:
			break
		popped_node = curr_stack[-1]
		done = True
		for n in tree[popped_node]['children']:
			if n not in tree or len(tree[n]['meta']) != tree[n]['num_meta']:
				done = False
				break
		if done:
			num_meta = tree[popped_node]['num_meta']
			meta = a[i:i+num_meta]
			tree[popped_node]['meta'] = meta
			i += num_meta
			meta_sum += sum(meta)
			curr_stack.pop()
			# print popped_node, meta
		else:
			stack_pop = False

	if i >= len(a):
		break
	curr_node = q.pop()
	curr_stack.append(curr_node)
	num_children = a[i]
	num_meta = a[i+1]

	# print num_children, num_meta

	tree[curr_node] = { 'num_children': num_children, 'children': [], 'num_meta': num_meta, 'meta': [] }
	if num_children == 0:
		meta = a[i+2:i+2+num_meta]
		tree[curr_node]['meta'] = meta
		meta_sum += sum(meta)
		i += num_meta
		stack_pop = True
		curr_stack.pop()
		# print meta

	for j in xrange(num_children):
		node_num += 1
		q.append(node_num)
		tree[curr_node]['children'].append(node_num)

	i += 2


def find_value(n, tree):
	node = tree[n]

	print node
	if node['num_children'] == 0:
		# print sum(node['meta'])
		return sum(node['meta'])

	s = 0
	for m in node['meta']:
		if m <= node['num_children'] and m > 0:
			nc = node['num_children']
			s += find_value(node['children'][nc-m], tree)
			print n,m, s

	return s

print find_value(0, tree)
