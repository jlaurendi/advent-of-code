import sys, copy
with open('advent-input.txt') as f:
	a = f.readlines()[0]

state = "####..##.##..##..#..###..#....#.######..###########.#...#.##..####.###.#.###.###..#.####..#.#..##..#"
state_dict = {}
for i in range(len(state)):
	state_dict[i] = state[i]
print state_dict
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

num_gens = 20
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


print cnt
