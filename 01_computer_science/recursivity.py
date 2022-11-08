def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))


print(isPalindrome("AdCDA"))
''' 
# slicing
# http://docs.python.org/2/library/functions.html#slice
str = 'Hello, World'
print(str[:-1])
#'Hello, Worl'
print(str[:])
#'Hello, World'
print(str[1:])
#'ello, World'
print(str[5])
# ','
# object
print(a[:-1])
# a[start:end]
print(a[1:2])
print(a[1:])
print(a[:-1])
print(a[:])
 '''
a = "Hello world"
print (a[0])
# print(a[1:-1])
print (a[-1])
print (a[1:-1])