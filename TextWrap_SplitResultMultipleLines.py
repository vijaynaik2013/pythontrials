"""
You are given a string  and width .
Your task is to wrap the string into a paragraph of width .

Input Format
The first line contains a string and second line contains the width.
Input String 1 : ABCDEFGHIJKLIMNOQRSTUVWXYZ
Input String 2 : 4
"""

import textwrap

def wrap(string,max_width):
    a = textwrap.wrap(string,width=max_width)
   # return ('\n'.join(map(str, a)))
    return ('\n'.join(a))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
  #  print(*result,sep='\n')
