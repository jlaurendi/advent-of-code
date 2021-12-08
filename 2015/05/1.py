
def is_nice(s):
    num_vowels = 0
    one_letter_twice = False
    trigger_words = { 'ab': 1, 'cd': 1, 'pq': 1, 'xy': 1 }

    prev_char = ''
    for i in range(len(s)):
        char = s[i]

        if char in ['a', 'e', 'i', 'o', 'u']:
            num_vowels += 1

        if char == prev_char:
            one_letter_twice = True

        if prev_char + char in trigger_words:
            return False

        prev_char = char

    return num_vowels >= 3 and one_letter_twice

# print(is_nice('ugknbfddgicrmopn'))
# print(is_nice('aaa'))
# print(is_nice('jchzalrnumimnmhp'))
# print(is_nice('haegwjzuvuyypxyu'))
# print(is_nice('dvszwmarrgswjxmb'))


lines = open('input.txt').readlines()

num_nice = 0
for ln in lines:
    if is_nice(ln):
        num_nice += 1
print(num_nice)
