import sys, os, copy, math

with open('advent-input.txt') as f:
  a = {i: int(elt) for i, elt in enumerate(f.readlines()[0].split(','))}

def access_memory(a, index):
    if index in a:
        return a[index]
    else:
        return 0

def get_output(a, input_val):
    i = 0
    out = ''
    rel_base = 0
    while i < xrange(len(a)):
        opcode = access_memory(a, i) % 100
        # print a[i]
        op = None
        num_args = 0
        if opcode == 99:
            # print 'break 99'
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
        elif opcode == 5:
            op = 'jit'
            num_args = 3
        elif opcode == 6:
            op = 'jif'
            num_args = 3
        elif opcode == 7:
            op = 'lt'
            num_args = 4
        elif opcode == 8:
            op = 'eq'
            num_args = 4
        elif opcode == 9:
            op = 'adj_rel'
            num_args = 2
        else:
            print 'Unexpected opcode ' + str(opcode)
            sys.exit()

        modes = access_memory(a, i) / 10 / 10
        mode = modes % 10
        if mode == 0:
            pos_a = access_memory(a, i+1)
        elif mode == 1:
            pos_a = i+1
        elif mode == 2:
            pos_a = access_memory(a, i+1) + rel_base
        else:
            print "Error - a"

        val_a = access_memory(a, pos_a)

        modes = modes / 10
        if num_args > 2:
            mode = modes % 10
            if mode == 0:
                pos_b = access_memory(a, i+2)
            elif mode == 1:
                pos_b = i+2
            elif mode == 2:
                pos_b = access_memory(a, i+2) + rel_base
            else:
                print "Error - b"

            val_b = access_memory(a, pos_b)

            if num_args > 3:
                modes = modes / 10
                mode = modes % 10

                if mode == 0:
                    pos_c = access_memory(a, i+3)
                elif mode == 1:
                    pos_c = i+3
                elif mode == 2:
                    pos_c = access_memory(a, i+3)  + rel_base
                else:
                    print "Error - c"

                val_c = access_memory(a, pos_c)

        ip_set = False
        # print op
        # print val_a
        # print val_b
        # print val_c
        if op == 'add':
            a[pos_c] = val_a + val_b
        elif op == 'mul':
            a[pos_c] = val_a * val_b
        elif op == 'save_input':
            a[pos_a] = input_val
        elif op == 'output':
            out += str(val_a)
        elif op == 'jit':
            if val_a != 0:
                i = val_b
                ip_set = True
        elif op == 'jif':
            if val_a == 0:
                i = val_b
                ip_set = True
        elif op == 'lt':
            if val_a < val_b:
                a[pos_c] = 1
            else:
                a[pos_c] = 0
        elif op == 'eq':
            if val_a == val_b:
                a[pos_c] = 1
            else:
                a[pos_c] = 0
        elif op == 'adj_rel':
            rel_base += val_a

        else:
            print "Error " + op

        if not ip_set:
            i += num_args
    return out

print get_output(a, 2)

