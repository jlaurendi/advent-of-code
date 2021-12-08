import os, copy, sys
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = os.path.join(__location__,'input.txt')

edges = set()
vertices = set()
with open(input_path) as f:
    for ln in f:
        parts = ln.strip().split('contain')
        v = parts[0].replace('bags ', '').strip()
        eparts = parts[1].split(',')
        for epart in eparts:
            vertices.add(v)
            w = epart.replace('bags', '').replace('.', '').strip()
            weight = None
            if w == 'no other':
                w = None
            else:
                num_digits = 0
                for i in range(len(w)):
                    if not w[i].isdigit():
                        break
                    num_digits += 1
                weight = int(w[:num_digits])
                w = w[num_digits:].strip()
            e = (v, w, weight)
            edges.add(e)

for v in vertices:
    print(v)
for e in edges:
    print(e)