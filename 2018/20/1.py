import sys, copy


with open('advent-input2.txt') as f:

	a = f.readlines()[0]
	a = a[1:-1] # remove ^ and $

door_dirs = []
queue = []
i = 0

def parse_regex(regex): # assumes starts with ( and ends with )
	i = 0
	branch_num = 0
	options = []
	options.append([])
	options[branch_num].append('')
	print i, regex, options
	while i < len(regex)-1:
		print options
		if regex[i] == '(':
			num_p = 1
			start_i = i
			i += 1
			while True:
				print regex, i
				if regex[i] == ')':
					num_p -= 1
				elif regex[i] == '(':
					num_p += 1

				if num_p == 0:
					break

				i += 1

			sub_opts = parse_regex(regex[start_i+1:i+1])
			new_options = []
			for opti in xrange(len(options[branch_num])):
				curr_opt = options[branch_num][opti]
				for sub_branch_num in xrange(len(sub_opts)):
					for sopt in sub_opts[sub_branch_num]:
						print curr_opt, sopt, sub_opts
						new_options.append(curr_opt + sopt)
			options = new_options
		elif regex[i] == '|':

			i += 1
			while i < len(regex)-1:
				start_i = i
				num_p = 0
				while (regex[i] != '|' or num_p != 0) and i < len(regex)-1:
					if regex[i] == '(':
						num_p += 1
					elif regex[i] == ')':
						num_p -= 1
					i += 1

				if start_i == i:
					sub_opts = ''
				else:
					sub_opts = parse_regex(regex[start_i+1:i])
				options.append(sub_opts)

		elif regex[i] == ')':
			print 'Error: why did we get here?'
			sys.exit()
		else:
			l = len(options[branch_num])
			for j in xrange(l):
				options[branch_num][j] += regex[i]
		i += 1

	return options


options = parse_regex(a)
print options



