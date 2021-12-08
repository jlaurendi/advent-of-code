lines = open('input.txt').readlines()

num_chars_total = 0
num_chars_encoded = 0
for line in lines:

    num_chars_total += len(line)

    i = 0
    while i < len(line):
        char = line[i]

        if char == "\\":
            num_chars_encoded += 2
        elif char == "\"":
            num_chars_encoded += 2
        else:
            num_chars_encoded += 1
        i += 1

    num_chars_encoded += 2



print(num_chars_encoded - num_chars_total)
