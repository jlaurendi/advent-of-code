d = '1113122113'

def transform(s):
    curr_count = 0
    result = ''
    prev_char = None
    for char in s:
        if char != prev_char and curr_count > 0:
            result += str(curr_count) + prev_char
            curr_count = 0

        curr_count += 1
        prev_char = char

    result += str(curr_count) + prev_char
    return result

# print(transform('1'))
# print(transform('11'))
# print(transform('21'))
# print(transform('111221'))

for i in range(50):
    d = transform(d)

print(len(d))