json = open('input.txt').readlines()[0]

total = 0
state = 'searching'
curr_number = ''
for char in json:

    if state == 'searching':
        if char == '-' or char.isdigit():
            state = 'number'
            curr_number += char

    elif state == 'number':
        if not char.isdigit():
            total += int(curr_number)
            curr_number = ''
            state = 'searching'
        else:
            curr_number += char

print(total)