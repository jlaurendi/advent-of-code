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

min_0_layer = None
min_0_layer_count = None
for i in xrange(len(layers)):
    layer = layers[i]
    count = 0
    for line in layer:
        for digit in line:
            if digit == 0:
                count += 1

    if min_0_layer is None or count < min_0_layer_count:
        min_0_layer = i
        min_0_layer_count = count

count1 = 0
count2 = 0
print layers[min_0_layer]
for line in layers[min_0_layer]:
    for digit in line:
        if digit == 1:
            count1 += 1
        if digit == 2:
            count2 += 1

print count1 * count2

# 984 -> too low
