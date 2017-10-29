def binarySearch(l, a):
    for i in l:
        if i == a:
            return True
        else:
            return False
l = [14, 52, 63, 0, 897, 1000, 235, 5]
a = int(input('Enter the number you want to search in the list : '))
if binarySearch(l, a):
    print('Element present in the list')
else:
    print('Element not present in the list')
