import sys, copy

num_gens = 50000000000

print 11304+(num_gens-125)*88
sys.exit()



with open('advent-input.txt') as f:
	a = f.readlines()[0]

state = "####..##.##..##..#..###..#....#.######..###########.#...#.##..####.###.#.###.###..#.####..#.#..##..#"
state_dict = {}
for i in range(len(state)):
	state_dict[i] = state[i]
rules = {
'.#.##': '.',
'...##': '#',
'..#..': '.',
'#.#..': '.',
'...#.': '.',
'.#...': '#',
'.....': '.',
'#....': '.',
'#...#': '#',
'###.#': '.',
'..###': '#',
'###..': '.',
'##.##': '.',
'##.#.': '#',
'..#.#': '#',
'.###.': '.',
'.#.#.': '.',
'.##..': '#',
'.####': '.',
'##...': '.',
'#####': '.',
'..##.': '.',
'#.##.': '.',
'.#..#': '#',
'##..#': '.',
'#.#.#': '#',
'#.###': '.',
'....#': '.',
'#..#.': '#',
'#..##': '.',
'####.': '#',
'.##.#': '#'
}

last = 0
total = 0
for g in xrange(num_gens):
	state_dict[int(min(state_dict.keys()))-1] = '.'
	state_dict[int(min(state_dict.keys()))-1] = '.'
	state_dict[int(max(state_dict.keys()))+1] = '.'
	state_dict[int(max(state_dict.keys()))+1] = '.'
	next_state = copy.deepcopy(state_dict)
	for i in state_dict.keys():

		s = ''
		for offset in [-2,-1,0,1,2]:
			if (i+offset) not in state_dict:
				s += '.'
			else:
				s += state_dict[i+offset]

		if rules[s] == '#':
			next_state[i] = '#'
		else:
			next_state[i] = '.'
	state_dict = next_state

	cnt = 0
	for i in state_dict:
		if state_dict[i] == '#':
			cnt += i

	print g, cnt, cnt-last
	# if (cnt-last) == 88:
	# 	cnt += 88*(num_gens-(g+1))
	# 	print cnt, num_gens, g, total
	# 	break
	last = cnt
print cnt
# print 7521+
# print 126408+88*(num_gens-)

# 4400000384534
# 4400000384446
# 4400000384358
# 4400000000129
# 4400000000304