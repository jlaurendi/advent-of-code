json = open('input.txt').readlines()[0]
# j = json
# json = '[1,2,3]'
# json = '[1,{"c":"red","b":2},3]'
# json = '[1,2,3,{"d":"red","g":2,e":[1,2,3,4],"f":{"d":1}},{"d":[1,2,3], "e":{1,2,3,"g":"red",{1,2,3}}}]'
# json = '[1,"red",5]'

# total = 0
# state = 'searching'
# curr_number = ''
# for char in json:
#     if state == 'searching':
#         if char == '-' or char.isdigit():
#             state = 'number'
#             curr_number += char

#     elif state == 'number':
#         if not char.isdigit():
#             total += int(curr_number)
#             curr_number = ''
#             state = 'searching'
#         else:
#             curr_number += char
# print(total)

from sys import exit


tree = {}
curr_node_num = 0
next_node_num = 0
q = []
i = 0
total = 0
top_level_nodes = []
while i < len(json):
    char = json[i]

    if char == "{":
        next_node_num += 1
        if len(q) == 0:
            top_level_nodes.append(next_node_num)
        q.append(next_node_num)
        tree[next_node_num] = { 'red': False, 'count': 0 }
        i += 1
        curr_node_num = next_node_num

    elif char == "}":
        i += 1
        next_node_num = q.pop()

        if len(q) != 0:

            if not tree[curr_node_num]['red']:
                # print(tree)
                # print(q)
                # print(closed_node)
                tree[q[-1]]['count'] += tree[curr_node_num]['count']

            curr_node_num = q[-1]


    elif char == '-' or char.isdigit():
        curr_number = ''
        curr_number += char
        i += 1
        char = json[i]
        while char.isdigit():
            curr_number += char
            i += 1
            char = json[i]
        if len(q) == 0:
            total += int(curr_number)
        else:
            tree[curr_node_num]['count'] += int(curr_number)

    elif char == ":":
        i += 1
        char = json[i]
        if char == "\"":
            if json[i+1:i+5] == "red\"":
                tree[curr_node_num]['red'] = True
                i += 5
            else:
                i += 1
    else:
        i += 1

# print(tree)

for tln in top_level_nodes:
    if not tree[tln]['red']:
        total += tree[tln]['count']

print (top_level_nodes)
# print(tree)
print(total)

# Guesses
# 142168 too high
# 76957 too low
# 53931 too low
