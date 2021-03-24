from collections import deque

N = int(input("Please enter the number of operations: "))
Input_Commands = []
d = deque()

for _ in range(N):
    Input_Commands.append(input("please enter commands: ").split())
print(Input_Commands)

for i in range(len(Input_Commands)):
    if Input_Commands[i][0] == "append":
        d.append(Input_Commands[i][1])
    if (Input_Commands[i][0] == "appendleft"):
        d.appendleft(Input_Commands[i][1])
    if (Input_Commands[i][0] == "pop"):
        d.pop()
    if (Input_Commands[i][0] == "popleft"):
        d.popleft()

for i in d:
    print (i,end=" ")