lines = open('input.txt').readlines()

signals = {}
for line in lines:
    line = line.split(' -> ')
    inst = line[0]
    wire = line[1]

    print(inst)
    print(wire)


print(signals['a'])