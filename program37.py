from sys import stdout
d1 = {'student1': 90, 'student2': 50, 'student3': 10}
d2 = {'student1': 55, 'student2': 11, 'student3': 5}
d3 = {'student1': 85, 'student2': 91, 'student3': 6}

def biggest(d, m):
    for i in d.values():
        if i >= m:
            m = i
    return m

max1 = max2 = max3 = 0
max1 = biggest(d1, max1)
max2 = biggest(d1, max2)
max3 = biggest(d1, max3)

if max1 > max2 and max1 > max3:
    print('Dict 1 is the largest')
elif max2 > max1 and max2 > max3:
    print('Dict 2 is the largest')
else:
    print('Dict 3 is the largest')


d2['student4'] = 52
d3['student4'] = 49

print('Length of dict 1 : {} and Length of dict2 : {} and Length of dict3 : {}'.format(len(d1), len(d2), len(d3)))

def dictToStr(d):
    for i in d:
        global str1
        str1 = '{} {} : {} '.format(str1,i, d[i])

str1 = ''
dictToStr(d1)
dictToStr(d2)
dictToStr(d3)

print(str1)
