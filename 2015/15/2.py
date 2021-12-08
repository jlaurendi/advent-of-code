data = open('input.txt').readlines()
# data = """""".readlines()

params = []
cals = []
for d in data:
    d = d.strip().split(' ')
    d = [i.replace(',','') for i in d]
    # print(d)
    cap = int(d[2])
    dur = int(d[4])
    fla = int(d[6])
    tex = int(d[8])
    cal = int(d[10])
    params.append([cap,dur,fla,tex])
    cals.append(cal)

def calc_score(cookie, params):
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

def calc_cals(cookie, cals):
    total = 0
    for i in range(len(cookie)):
        total += cookie[i] * cals[i]
    return total

from copy import deepcopy
max_score = -10
cookie = [int(100/len(params[0]))] * len(params[0])
prev_cookie = deepcopy(cookie)
q = [cookie]

for i in range(100):
    for j in range(100):
        if i + j > 100:
            break

        for k in range(100):
            if i + j + k > 100:
                break

            l = 100 - i - j - k
            cookie = [i, j, k, l]
            if calc_cals(cookie, cals) == 500:
                new_score = calc_score(cookie, params)
                if new_score > max_score:
                    max_score = new_score


# while len(q) > 0:
#     c = q.pop(0)



#     print(max_score)
#     prev_max_score = max_score
#     for i in range(len(cookie)):
#         for j in range(len(cookie)):
#             if i == j:
#                 continue

#             test_cookie = deepcopy(cookie)
#             prev_score = calc_score(test_cookie, params)
#             while True:
#                 # print(test_cookie)
#                 test_cookie[i] = test_cookie[i] - 1
#                 test_cookie[j] = test_cookie[j] + 1
#                 if test_cookie[i] <= 0 or test_cookie[j] >= 100:
#                     break

#                 new_score = calc_score(test_cookie, params)
#                 if new_score > prev_score:
#                     prev_score = new_score
#                     cookie = deepcopy(test_cookie)
#                     if calc_cals(cookie, cals) == 500:
#                         max_score = new_score


print(max_score)

# print(params)

# 9375000 - too low
# 10005000 - too low
# 11171160
