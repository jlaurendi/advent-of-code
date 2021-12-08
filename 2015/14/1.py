data = open('input.txt').readlines()

limits = {}
for line in data:
    line = line.split(' ')
    r = line[0]
    s = line[3]
    limit = line[6]
    rest = line[-2]

    limits[r] = {}
    limits[r]['v'] = int(s)
    limits[r]['limit'] = int(limit)
    limits[r]['rest'] = int(rest)


num_secs = 2503
positions = {}
states = {}
points = {}
for i in range(num_secs):

    for r in limits:
        if r not in states:
            states[r] = {}
            states[r]['sec_left'] = limits[r]['limit']
            states[r]['state'] = 'flying'
            positions[r] = 0
            points[r] = 0

        if states[r]['state'] == 'flying':
            positions[r] += limits[r]['v']
            states[r]['sec_left'] -= 1

            if states[r]['sec_left'] == 0:
                states[r]['state'] = 'resting'
                states[r]['sec_left'] = limits[r]['rest']

        elif states[r]['state'] == 'resting':
            states[r]['sec_left'] -= 1

            if states[r]['sec_left'] == 0:
                states[r]['state'] = 'flying'
                states[r]['sec_left'] = limits[r]['limit']

    max_p = 0
    for r in positions:
        if positions[r] > max_p:
            max_p = positions[r]

    for r in positions:
        if positions[r] == max_p:
            points[r] += 1


max_p = 0
for r in points:
    if points[r] > max_p:
        max_p = points[r]
print(max_p)