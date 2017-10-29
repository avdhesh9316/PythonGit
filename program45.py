### Checking a String is palindrome or not

str1 = input('Enter the String : ')
def checkPalindrome(str1):
    l = [i for i in str1]
    return l
l = checkPalindrome(str1)
s = ''
for i in range(len(l)):
    s += l.pop()
if str1 == s:
    print('String is Palindrome')
else:
    print('String is not Palindrome')
