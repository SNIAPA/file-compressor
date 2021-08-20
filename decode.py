#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

def main(s:str,l:str) ->str:
    tree = l.split('0x')[1:]
    tree= [chr(int(x,16)) for x in tree]

    row = 1
    offset = 0
    i = 0
    while i < len(tree):
        if (tree[i] != '\x00') and ( tree[i] !=''):
            tree = tree[:(2**(row+1))-2 + (offset**2)] + ['',''] + tree[(2**(row+1))-2 + (offset**2):]
        if (2**row)-1  <= offset:
            offset = 0
            row+=1
            i+=1
            continue

        offset+=1
        i+=1
    


    ans = ''
    i = 0
    counter = 0
    for x in s:
        index = (2**(i+1))-2 + ((counter)*2) + int(x)
        if tree[index] == '\x00':
            i+=1
            counter = (counter*2) + int(x)
            continue
        i = 0
        counter = 0
        ans+=tree[index]
    return(ans)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(main(input('Input encoded string: '),input("input node list: ")))
    else:    
        print(main(sys.argv[1],sys.argv[2]))