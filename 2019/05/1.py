import sys, os, copy, math

with open('advent-input.txt') as f:
  a = [int(elt) for elt in f.readlines()[0].split(',')]

def get_output(a, input_val):
    i = 0
    out = '' 
    while i < xrange(len(a)):
        opcode = a[i] % 100
        op = None
        num_args = 0
        if opcode == 99: 
            break
        elif opcode == 1:
            op = 'add'
            num_args = 4
        elif opcode == 2:
            op = 'mul'
            num_args = 4
        elif opcode == 3:
            op = 'save_input'
            num_args = 2
        elif opcode == 4:
            op = 'output'
            num_args = 2
        else:
            print 'Unexpected opcode ' + str(opcode)
            sys.exit()
        
        modes = a[i] / 10 / 10
        
        pos_a = a[i+1]
        if modes % 10 == 0:
            val_a = a[pos_a]
        else:
            val_a = a[i+1]

        modes = modes / 10
        if num_args > 2:
            pos_b = a[i+2]
            if modes % 10 == 0:
                val_b = a[pos_b]
            else:
                val_b = a[i+2]

            modes = modes / 10
            pos_c = a[i+3]
            if modes % 10 == 0:
                val_c = a[pos_c]
            else:
                val_c = pos_c


        if op == 'add':
            a[pos_c] = val_a + val_b
        elif op == 'mul':
            a[pos_c] = val_a * val_b
        elif op == 'save_input':
            a[pos_a] = input_val
        elif op == 'output':
            out += str(val_a)

        i += num_args
    return out

print get_output(a, 1)
