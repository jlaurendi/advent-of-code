import sys, os, copy, math

w = 25
h = 6
layers = []
with open('advent-input.txt') as f:
    a = f.readlines()
    
    index = 0
    new_layer = []
    new_line = []
    for line in a:
        for digit in line.strip():
            new_line.append(int(digit))
            index += 1
            if index % w == 0:
                new_layer.append(new_line)
                new_line = []
            if index % (w * h) == 0:
                layers.append(new_layer)
                new_layer = []

final_layer = copy.deepcopy(layers[0])
num_layers = len(layers)
for i in xrange(w):
    for j in xrange(h):
        for k in xrange(num_layers):
            digit = layers[k][j][i]
            if digit == 0:
                final_layer[j][i] = ' '
                break
            elif digit == 1:
                final_layer[j][i] = '*'
                break

for j in xrange(h):
    line = ''
    for i in xrange(w):
        line += final_layer[j][i]
    print line
