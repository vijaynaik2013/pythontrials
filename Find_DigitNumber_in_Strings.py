s = input()

#easier way
#Solution 1
#print(any(i.isalnum() for i in s))
#print(any(i.isalpha() for i in s))
#print(any(i.isdigit() for i in s))
#print(any(i.islower() for i in s))
#print(any(i.isupper() for i in s))

############################
#Solution 2
def isAlphaNumeric(a):
    return any(i.isalnum() for i in a)

def isAlpha(a):
    return any(i.isalpha() for i in a)

def isDigit(a):
    return any(i.isdigit() for i in a)

def isLower(a):
    return any(i.islower() for i in a)

def isUpper(a):
    return any(i.isupper() for i in a)

print(isAlphaNumeric(s))
print(isAlpha(s))
print(isDigit(s))
print(isLower(s))
print(isUpper(s))

## 3rd way of defining function
def isAlphaNumeric1(a):
    for i in (a):
        if i.isalnum():
            return True
    return False

print(isAlphaNumeric1(s))