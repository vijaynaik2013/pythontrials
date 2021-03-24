#width = 20
#print('HackerRank'.ljust(width,'-'))
#print('HackerRank'.center(width,'-'))
#print('HackerRank'.rjust(width,'-'))
import textwrap

s = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
a = [textwrap.wrap(s, width=4)]
for i in a:
    print (*i, sep='\n')

b = [textwrap.fill(s,width=4)]
for line in b:
    print(line)