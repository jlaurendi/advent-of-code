data = open('input.txt').readlines()
# data = """""".readlines()

params = []
for d in data:
    d = d.strip().split(' ')
    d = [i.replace(',','') for i in d]
    # print(d)
    cap = int(d[2])
    dur = int(d[4])
    fla = int(d[6])
    tex = int(d[8])
    # cal = int(d[10])
    params.append([cap,dur,fla,tex])

def calc_score(cookie, params):
    total = 0

    score = [0] * len(params[0])
    for i in range(len(params)):
        for j in range(len(score)):
            score[j] += cookie[i] * params[i][j]

    prod = 1
    for i in range(len(score)):
        if score[i] < 0:
            prod = 0
            break
        prod = prod * score[i]

    return prod

from copy import deepcopy
max_score = 0
cookie = [int(100/len(params[0]))] * len(params[0])
while True:
    prev_max_score = max_score
    for i in range(len(cookie)):
        for j in range(len(cookie)):
            if i == j:
                continue

            while True:
                test_cookie = deepcopy(cookie)
                test_cookie[i] = test_cookie[i] - 1
                test_cookie[j] = test_cookie[j] + 1
                if test_cookie[i] <= 0 or test_cookie[j] >= 100:
                    break

                new_score = calc_score(test_cookie, params)
                if new_score > max_score:
                    cookie = deepcopy(test_cookie)
                    max_score = new_score
                else:
                    break

    if max_score == prev_max_score:
        break
print(max_score)

# print(params)
# print(calc_score([44,56], params))

