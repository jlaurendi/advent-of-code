import sys
with open('advent-input.txt') as f:
    a = f.readlines()
    a = [i.strip() for i in a]

# checksum = 0
# two_cnt = 0
# three_cnt = 0
# for elt in a:
# 	char_cnt = {}
# 	for char in elt:
# 		if char not in char_cnt:
# 			char_cnt[char] = 0
# 		char_cnt[char] += 1

# 	two_found = False
# 	three_found = False
# 	for char in char_cnt:

# 		cnt = char_cnt[char]

# 		if cnt == 2:
# 			two_found = True
# 		elif cnt == 3:
# 			three_found = True

# 	if two_found:
# 		two_cnt += 1
# 	if three_found:
# 		three_cnt += 1

# checksum = two_cnt * three_cnt
# print(checksum)

for elt1 in a:
	for elt2 in a:
		diffs = 0
		correct = True
		for i in range(len(elt1)):
			if elt1[i] != elt2[i]:
				diffs += 1
			if diffs > 1:
				correct = False
				break
		if diffs == 1:
			ans = ''
			for i in xrange(len(elt1)):
				if elt1[i] == elt2[i]:
					ans += elt1[i]
			print elt1, elt2
			print ans
			sys.exit()



