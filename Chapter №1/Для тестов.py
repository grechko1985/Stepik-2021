s_1 = input()
count_a = 0
count_b = 0
count_c = 0
i = 0
s = s_1 + '1'
while i < len(s):
    if s[i] == 'a':
        count_a += 1
        if s[i] == s[i + 1]:
            i += 1
        else:
            print('a' + str(count_a), end='')
            i += 1
            count_a = 0
    elif s[i] == 'b':
        count_b += 1
        if s[i] == s[i + 1]:
            i += 1
        else:
            print('b' + str(count_b), end='')
            i += 1
            count_b = 0
    elif s[i] == 'c':
        count_c += 1
        if s[i] == s[i + 1]:
            i += 1
        else:
            print('c' + str(count_c), end='')
            i += 1
            count_c = 0
    else:
        break