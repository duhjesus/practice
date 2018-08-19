# data struct = stacks
#check that string of brackets, parentheses, and/or braces have a matched pair and balanced.
# matched pair means that there is a closing char on the right of a opening char
# balance means for every char there is one that matches.
def main():
    t = int(input())

    for t_itr in range(t):
        expression = input()
        #print(expression)
        if len(expression) % 2 != 0:
            print("NO")
            continue
        if len(expression) == 0:
            print("YES")
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
        if len(stackList) !=0:
            print("NO")
        else:
            print(success)
                    

# see if set of strings(note) case sensitive contained within 
# set of strings(magazine)
def checkMagazine(magazine, note):
    mag = {}
    n = {}
    for word in magazine:
        if word in mag:
            mag[word] = mag[word] +1
        else:
            mag[word] = 1
    for word in note:
        if word in n:
            n[word] = n[word] +1
        else:
            n[word] = 1
    for key in n:
        if key in mag:
            if n[key] > mag[key]:
                print("No")
                return
        else:
            print("No")
            return
    print("Yes")

# return an integer representing the minimum total 
# characters that must be deleted to make the 
# strings anagrams of each other.
def makeAnagram(a, b):
    sizeAlphabet = 26
    #print(ord(a[0])-ord('a'))
    freqA = []
    freqB = []
    for i in range(0,sizeAlphabet):
        freqA.append(0)
        freqB.append(0)
    for idx,el in enumerate(a):
        charIndex = ord(el) - ord('a')
        freqA[charIndex]= freqA[charIndex] + 1
    for idx,el in enumerate(b):
        charIndex = ord(el) - ord('a')
        freqB[charIndex]= freqB[charIndex] + 1 
    count = 0
    #alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
    for idx, el in enumerate(freqA):
        diff = abs(freqA[idx]- freqB[idx])
        count = count + diff
    return count
# bubble sort
mport math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    swapp = 0
    isSorted =False
    lastUnsorted = len(a)-1
    while(isSorted== False):
        isSorted = True
        for i in range(0,lastUnsorted):
            if a[i] >a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                isSorted = False
                swapp = swapp +1
        lastUnsorted = lastUnsorted - 1
    print("Array is sorted in", swapp, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[len(a)-1])
if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
