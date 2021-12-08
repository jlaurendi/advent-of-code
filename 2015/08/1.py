lines = open('input.txt').readlines()

num_chars_total = 0
num_chars_memory = 0
for line in lines:

    num_chars_total += len(line)
    line = line[1:-1]

    i = 0
    while i < len(line):
        char = line[i]

        if char == "\\":
            next_char = line[i+1]
            if next_char == "\\":
                i += 2
            elif next_char == "x":
                i += 4
            elif next_char == "\"":
                i += 2
        else:
            i += 1
        num_chars_memory += 1



print(num_chars_total - num_chars_memory)
