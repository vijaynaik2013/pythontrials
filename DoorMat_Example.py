"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

    Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

"""
rows, columns = map(int,input().split())
s1 = ".|."
s2 = "WELCOME"
for i in range(1,rows, 2):
    print((i * s1).center(columns,"-"))
print(s2.center(columns,"-"))
for i in range(rows-2,-1,-2):
    print((i * s1).center(columns, "-"))


#####################################################
print()
print(" Alternative Solution ", ""* 100)
print()
#####################################################

#Alternative Method
for i in range(rows//2):
    print((s1*((i*2)+1)).center(columns,"-"))
print(s2.center(columns,"-"))
for i in range(rows//2-1,-1,-1):
    print((s1*((i*2)+1)).center(columns,"-"))