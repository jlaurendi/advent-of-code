import sys
with open('advent-input.txt') as f:
	a = f.readlines()
	a = [i.strip().split('] ') for i in a]
	new_a = {}
	for i in a:
		time = i[0].strip('[')
		action = i[1]
		new_a[time] = action
		# print time

b = new_a.keys()
b.sort()
mins_asleep = {}
curr_guard = None

for i in b:
	ins = new_a[i]
	if 'Guard' in ins:
		curr_guard = ins.split('Guard #')[1].split(' begins')[0]
		# print ins
		# print curr_guard
	elif 'falls asleep' in ins:
		sleep_start = int(i.split(' ')[1].split(':')[1])
	elif 'wakes' in ins:
		sleep_end = int(i.split(' ')[1].split(':')[1])

		day = i.split(' ')[0].split('1518-')[1]
		# print day
		for minute in range(sleep_start, sleep_end):
			# print curr_guard
			if curr_guard not in mins_asleep:
				mins_asleep[curr_guard] = {}
			if minute not in mins_asleep[curr_guard]:
				mins_asleep[curr_guard][minute] = {}

			mins_asleep[curr_guard][minute][day] = 1


top_guard = None
top_guard_count = 0
for curr_guard in mins_asleep:
	curr_count = 0
	for m in mins_asleep[curr_guard]:
		for n in mins_asleep[curr_guard][m]:
			curr_count += 1
	if curr_count > top_guard_count:
		top_guard_count = curr_count
		top_guard = curr_guard

top_min = None
top_min_count = 0
for m in mins_asleep[top_guard]:
	curr_count = 0
	for n in mins_asleep[top_guard][m]:
		curr_count += 1
	if curr_count > top_min_count:
		top_min_count = curr_count
		top_min = m
print int(top_guard) * int(top_min)
sys.exit()