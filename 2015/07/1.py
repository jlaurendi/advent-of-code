from sys import exit
import copy
lines = open('input.txt').readlines()

signals = {}
while len(lines) > 0:
    # print(len(lines))
    new_lines = []
    for i in range(len(lines)):
        line = lines[i]
        line = line.split(' -> ')
        inst = line[0]
        wire = line[1].strip()

        inst_parts = inst.split(' ')
        num_parts = len(inst_parts)

        if num_parts == 1:
            w1 = inst_parts[0]
            if w1.isdigit():
                signals[wire] = int(w1)
            else:
                if w1 not in signals.keys():
                    new_lines.append(lines[i])
                    continue
                signals[wire] = signals[w1]

        elif num_parts == 2:
            if inst_parts[0] == 'NOT':
                w1 = inst_parts[1]
                if w1 not in signals.keys():
                    new_lines.append(lines[i])
                    continue

                signals[wire] = ~signals[w1] % 2**16
            else:
                print("ERROR in not")
                exit()

        elif num_parts == 3:
            w1 = inst_parts[0]
            w2 = inst_parts[2]
            if inst_parts[1] == 'AND':
                if w1.isdigit():
                    if w2 not in signals.keys():
                        new_lines.append(lines[i])
                        continue
                    signals[wire] = int(w1) & signals[w2]
                else:
                    if w1 not in signals.keys() or w2 not in signals.keys():
                        new_lines.append(lines[i])
                        continue
                    signals[wire] = signals[w1] & signals[w2]
            elif inst_parts[1] == 'OR':
                if w1 not in signals.keys() or w2 not in signals.keys():
                    new_lines.append(lines[i])
                    continue

                signals[wire] =  signals[w1] | signals[w2]
            elif inst_parts[1] == 'LSHIFT':
                if w1 not in signals.keys():
                    new_lines.append(lines[i])
                    continue

                signals[wire] = signals[w1] << int(w2)
            elif inst_parts[1] == 'RSHIFT':
                if w1 not in signals.keys():
                    new_lines.append(lines[i])
                    continue

                signals[wire] = signals[w1] >> int(w2)
            else:
                print("ERROR in num parts = 3")
                exit()
        else:
            print("ERROR")
            exit()

    lines = copy.deepcopy(new_lines)
    # exit()
    # if len(lines) == 287:
    #     for l in lines:
    #         print(l)
    #     print(signals)
    #     exit()


# print(signals)
print(signals['a'])