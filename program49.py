fh = open('file.txt', 'r+')
print('Content of file: \n{}'.format(fh.read()))
fh.close()
print()
fh = open('file.txt', 'w+')
fh.write('Adding Second Line\nAdding Third Line\nAdding Fourth Line')
fh.close()
fh = open('file.txt', 'r+')
print('New Content of file after writing 3 line into it:\n{}'.format(fh.read()))
fh.close()
print()
fh = open('file.txt', 'a+')
fh.write('Adding Fifth Line\nAdding Sixth Line\nAdding seventh Line\nAdding eighth line\nAdding tenth line')
fh.close()
fh = open('file.txt', 'r+')
print('New Content of file after apending 5 lines into it:\n{}'.format(fh.read()))
fh.close()