#!/bin/python3

import math
import os
import random
import re
import sys
import difflib

def main():

    f =open("Stestcases.txt","r")
    f1 = f.readlines()
    n = int(f1[0])

    count = 0

    for t_itr in f1:
        if t_itr == f1[0]:
            continue
        count = count +1

        print(count,"=",end="")
        #print(t_itr)
        expression = list(t_itr.strip())
        success = "YES"

        if len(expression) % 2 != 0:
            #print(expression)
            #print("KEEPS COMING HERE")
            success = "NO"
            sf = open("Sresult.txt", "a+")
            if count != n:
                f.write(success+"\n")
                print(success)
            else:
                f.write(success)                    
                print(success)
            continue
        if len(expression) == 0:
            success = "YES"
            f = open("Sresult.txt", "a+")
            if count != n:
                f.write(success+"\n")
                print(success)
            else:
                f.write(success)                    
                print(success)
            continue
        stackList = []
        bracket = {"]":"[", ")":"(", "}":"{"}
        success = 'YES'
        for el in expression:
            if el == '[' or el == '(' or el == '{':
                stackList.append(el)
            else:
                if len(stackList) == 0 or bracket[el] != stackList[len(stackList)-1]:
                    success = "NO"
                    break 
                popped = stackList.pop()

        f = open("Sresult.txt", "a+")
        if count != n:
            f.write(success+"\n")
            print(success)
        else:
            f.write(success)                    
            print(success)
    f.close

    with open('Sresult.txt','r') as hosts0:
        with open("Ssol.txt",'r') as hosts1:
            diff = difflib.unified_diff(
                hosts0.readlines(),
                hosts1.readlines(),
                fromfile='hosts0',
                tofile='hosts1',
            )
            for line in diff:
                sys.stdout.write(line)
if __name__ == '__main__':
    main()