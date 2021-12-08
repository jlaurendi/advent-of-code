import sys, os, copy
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = os.path.join(__location__,'advent-input.txt')

with open(input_path) as f:
    a = f.readlines()[0]
    a = [int(elt) for elt in a.split(',')]

def get_output(a, noun, verb):
    a[1] = noun
    a[2] = verb
    i = 0
    while i < xrange(len(a)):
        opcode = a[i]
        op = None
        if opcode == 99:
            break
        elif opcode == 1:
            op = 'add'
        elif opcode == 2:
            op = 'mul'
        else:
            print 'Unexpected opcode ' + str(opcode)
            sys.exit()

        pos_a = a[i+1]
        pos_b = a[i+2]
        pos_c = a[i+3]

        if op == 'add':
            a[pos_c] = a[pos_a] + a[pos_b]
        elif op == 'mul':
            a[pos_c] = a[pos_a] * a[pos_b]

        i += 4

    return a[0]

target_output = 19690720
noun = 0
verb = 0
found = False
for noun in xrange(100):
    for verb in xrange(100):
        if get_output(copy.deepcopy(a), noun, verb) == target_output:
            found = True 
            break
    if found:
        break

print 100 * noun + verb
