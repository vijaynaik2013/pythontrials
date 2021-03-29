#x and y are variables which are declared in lambda function
# and then addition executed for these variable
#LAMBDA usage as below
addusingLambda = lambda x,y: x+y
print(addusingLambda(2,3))
########################################################################

seq = [1,3,5,9,11]

def double(x):
    return x * 2

doubled = [double(x) for x in seq]
print(doubled)

doublekar = list(map(double,seq))
print(doublekar)

aanidoublekar = list(map(lambda x:x*2,seq))
print(aanidoublekar)