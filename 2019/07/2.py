import sys, os, copy, math, itertools

with open('input.txt') as f:
    memory = [int(elt) for elt in f.readlines()[0].split(',')]


class Amplifier:
    def __init__(self, memory, phase):
        self.memory = copy.deepcopy(memory)
        self.memory_size = len(self.memory)
        self.curr_ptr = 0
        self.rel_base = 0
        self.state = 'ready'
        self.output = None
        self.phase = phase
        self.phase_set = False

    def access_memory(self, index):
        if index < self.memory_size:
            return self.memory[index]
        else:
            return 0

    def run_one_step(self, input_val):
        if self.state == 'done':
            return self.output

        if self.curr_ptr >= self.memory_size:
            self.state = 'done'
            return self.output

        while self.curr_ptr < self.memory_size:
            opcode = self.access_memory(self.curr_ptr) % 100
            op = None
            num_args = 0

            if opcode == 99:
                self.state = 'done'
                return self.output
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
                print('Unexpected opcode ' + str(opcode))
                sys.exit()


            modes = self.access_memory(self.curr_ptr) // 10 // 10
            mode = modes % 10
            if mode == 0 or op == 'save_input':
                pos_a = self.access_memory(self.curr_ptr+1)
            elif mode == 1:
                pos_a = self.curr_ptr+1
            elif mode == 2:
                pos_a = self.access_memory(self.curr_ptr+1) + self.rel_base
            else:
                print("Error - a")

            val_a = self.access_memory(pos_a)

            modes = modes // 10
            if num_args > 2:
                mode = modes % 10
                if mode == 0:
                    pos_b = self.access_memory(self.curr_ptr+2)
                elif mode == 1:
                    pos_b = self.curr_ptr+2
                elif mode == 2:
                    pos_b = self.access_memory(self.curr_ptr+2) + self.rel_base
                else:
                    print("Error - b")

                val_b = self.access_memory(pos_b)

                if num_args > 3:
                    modes = modes // 10
                    mode = modes % 10

                    if mode == 0:
                        pos_c = self.access_memory(self.curr_ptr+3)
                    elif mode == 1:
                        pos_c = i+3
                    elif mode == 2:
                        pos_c = self.access_memory(self.curr_ptr+3)  + self.rel_base
                    else:
                        print("Error - c")

                    val_c = self.access_memory(pos_c)

            ip_set = False
            if op == 'add':
                self.memory[pos_c] = val_a + val_b
            elif op == 'mul':
                self.memory[pos_c] = val_a * val_b
            elif op == 'save_input':
                if self.phase_set:
                    self.memory[pos_a] = input_val
                else:
                    self.memory[pos_a] = self.phase
                    self.phase_set = True
            elif op == 'output':
                self.output = val_a
                self.curr_ptr += num_args
                return self.output
            elif op == 'jit':
                if val_a != 0:
                    self.curr_ptr = val_b
                    ip_set = True
            elif op == 'jif':
                if val_a == 0:
                    self.curr_ptr = val_b
                    ip_set = True
            elif op == 'lt':
                if val_a < val_b:
                    self.memory[pos_c] = 1
                else:
                    self.memory[pos_c] = 0
            elif op == 'eq':
                if val_a == val_b:
                    self.memory[pos_c] = 1
                else:
                    self.memory[pos_c] = 0
            elif op == 'adj_rel':
                self.rel_base += val_a

            else:
                print("Error " + op)

            if not ip_set:
                self.curr_ptr += num_args
        self.state = 'done'
        return self.output


# Find the max configuration
phase_vals = range(5, 10)
max_amp_out = None
max_phase_vals = None
for curr_phase_vals in itertools.permutations(phase_vals):
    (phase_a, phase_b, phase_c, phase_d, phase_e) = curr_phase_vals

    a = Amplifier(memory, phase_a)
    b = Amplifier(memory, phase_b)
    c = Amplifier(memory, phase_c)
    d = Amplifier(memory, phase_d)
    e = Amplifier(memory, phase_e)

    amp_e_out = 0
    while True:
        amp_a_out = a.run_one_step(amp_e_out)
        amp_b_out = b.run_one_step(amp_a_out)
        amp_c_out = c.run_one_step(amp_b_out)
        amp_d_out = d.run_one_step(amp_c_out)
        amp_e_out = e.run_one_step(amp_d_out)

        # print(amp_a_out, amp_b_out, amp_c_out, amp_d_out, amp_e_out)
        # print(a.state, b.state, c.state, d.state, e.state)
        if e.state == 'done':
            break

    if max_amp_out is None or amp_e_out > max_amp_out:
        max_amp_out = amp_e_out
        max_phase_vals = curr_phase_vals

print(max_amp_out)