import sys, os, copy, math

edges = {}
nodes = {}
adj = {}
with open('advent-input.txt') as f:
    a = f.readlines()
    for elt in a:
        sp = elt.strip().split(')')
        node1 = sp[0]
        node2 = sp[1]
        if node1 not in adj:
            adj[node1] = {}
        adj[node1][node2] = 1

        if node2 not in adj:
            adj[node2] = {}
        adj[node2][node1] = 1

q = [('YOU', 0)]
visited = set()
total_depth = 0
while len(q) > 0:
    curr_node = q.pop(0)
    depth = curr_node[1]
    if curr_node[0] not in adj:
        continue
    for node in adj[curr_node[0]]:
        if node == 'SAN':
            print depth-1
            sys.exit()
        if node in visited:
            continue
        visited.add(node)
        q.append((node, depth + 1))

