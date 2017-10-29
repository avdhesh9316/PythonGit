from sys import stdout

List = [10,20,30,40,50,60,70]

List.append(80)

List.insert(4, 100)

#print(len(List))

print("List : ")
for i in range(len(List)):
    stdout.write(' {}'.format(List[i]))

## Bubble Sorted

for i in range(len(List) - 1):
    for j in range(i+1, len(List)):
        if List[i] >= List[j]:
            List[i],List[j] = List[j],List[i]

print("\nSorted list in Ascending Order : ")
for i in range(len(List)):
    stdout.write(' {}'.format(List[i]))


s = 0
e = len(List) - 1
while s <= e:
    List[s], List[e] = List[e], List[s]
    s += 1
    e -= 1

print("\nSorted list in Descending Order : ")
for i in range(len(List)):
    stdout.write(' {}'.format(List[i]))
