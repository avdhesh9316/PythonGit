
pattern = 'Treasure'
count = 0
d = {'file1.txt' : 0, 'file2.txt' : 0, 'file3.txt' : 0, 'file4.txt' : 0}
def countPattern(f, v, count, pattern):
    fh = open(f, 'r+')
    if fh.read().__contains__(pattern):
        fh.seek(0)
        v = fh.read().count(pattern)
    if v > 0:
        count += 1
    print('{} has {} patterns'.format(f,v))
    return count
    fh.close()

for k, v in d.items():
    count = countPattern(k, v, count, pattern)

print('The Number of file with the given pattern is : {}'.format(count))
