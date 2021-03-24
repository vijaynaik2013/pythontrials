N = int(input("please enter the number of commands:"))
prompt_command = []
convert_command = []

for _ in range(N):
    a = input("please enter the command: ").split()
    prompt_command.append(a)

for i in range(len(prompt_command)):
    if prompt_command[i][0]=="insert":
        convert_command.insert(int(prompt_command[i][1]),int(prompt_command[i][2]))
        print(convert_command)
    elif prompt_command[i][0]== "print":
        print(convert_command)
    elif prompt_command[i][0]== "remove":
        convert_command.remove(int(prompt_command[i][1]))
    elif prompt_command[i][0] == "append":
        convert_command.append(int(prompt_command[i][1]))
    elif prompt_command[i][0] == "sort":
        convert_command.sort()
    elif prompt_command[i][0] == "pop":
        convert_command.pop()
    elif prompt_command[i][0] == "reverse":
        convert_command.reverse()




