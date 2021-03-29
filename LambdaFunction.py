seq = [1,3,5,9,11]

def double(x):
    return x * 2

doubled = [double(x) for x in seq]
print(doubled)

doublekar = list(map(double,seq))
print(doublekar)

aanidoublekar = list(map(lambda x:x*2,seq))
print(aanidoublekar)