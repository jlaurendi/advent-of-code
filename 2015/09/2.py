lines = open('input.txt').readlines()

graph = {}
for line in lines:
    print(line)
    parts = line.split(' = ')

    locs = parts[0]
    dist = parts[1]

    locs = locs.split(' to ')
    loc1 = locs[0]
    loc2 = locs[1]

    if loc1 not in graph:
        graph[loc1] = {}
    graph[loc1][loc2] = int(dist)

    if loc2 not in graph:
        graph[loc2] = {}
    graph[loc2][loc1] = int(dist)

nodes = graph.keys()
longest_dist = 0
longest_path = None
q = []
for n in nodes:
    q.append({ 'dist': 0, 'path': [ n ] })

while len(q) > 0:
    curr = q.pop(0)
    curr_dist = curr['dist']
    curr_path = curr['path']
    curr_n = curr_path[-1]
    adj_nodes = graph[curr_n].keys()

    for adj_n in adj_nodes:
        if adj_n in curr['path']:
            continue

        if adj_n not in graph[curr_n]:
            continue

        edge_cost = graph[curr_n][adj_n]
        new_path_dist = edge_cost + curr_dist
        if new_path_dist <= longest_dist:
            continue

        if len(curr_path) == len(nodes)-1:
            if new_path_dist > longest_dist:
                longest_dist = new_path_dist
                longest_path = curr_path + [adj_n]
        else:
            q.append({ 'dist': curr_dist + edge_cost, 'path': curr_path + [adj_n] })

print(longest_path)
print(longest_dist)
