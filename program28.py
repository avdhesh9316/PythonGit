#! /usr/bin/python3
s = 'welcome avdhesh kumar'
vowels = {'a' : 1, 'e' : 0, 'i' : 0, 'o' : 0, 'u' : 0}
count = 0
for i in range(len(s)):
    if s[i] == 'a':
        count += 1
        vowels['a'] += 1
    elif s[i] == 'e':
        count += 1
        vowels['e'] += 1
    elif s[i] == 'i':
        count += 1
        vowels['i'] += 1
    elif s[i] == 'o':
        count += 1
        vowels['o'] += 1
    elif s[i] == 'u':
        count += 1
        vowels['u'] += 1

print('Total vowels : {}'.format(count))
for i in vowels.keys():
    print('{} = {}'.format(i, vowels[i]))
