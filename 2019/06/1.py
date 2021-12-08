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

q = [('COM', 0)]
total_depth = 0
while len(q) > 0:
    curr_node = q.pop()
    depth = curr_node[1]
    total_depth += depth
    if curr_node[0] not in adj:
        continue
    for node in adj[curr_node[0]]:
        q.append((node, depth + 1))

print total_depth

