def split_and_join(line):
    a = line.split()
    b = '-'.join(a)
    print(b)

line = input()
split_and_join(line)