#!/bin/python3

import math
import os
import random
import re
import sys
import difflib

class TrieNode():
    def __init__(self):
        self.children = {}
        self.data = []
        self.isCompleteWord = False
        self.words = 0

class Solution():
    def __init__(self):
        self.root = TrieNode()
        
    def add(self,contact):
        curr = self.root
        for i in range(0,len(contact)):
            charFound = True # assume char/prefix found already
            while charFound:
                char = contact[i]
                if char in curr.data:
                    curr.words = curr.words +1
                    # traverse to next tri node
                    curr = curr.children[char]
                    break
                    #i = i + 1
                    #if i <= len(contact)-1:
                    #    char = contact[i]
                    #else:
                    #    i = i-1
                    #    char = contact[i-1]
                    #shouldnt run into problems here b/c a char string pattern
                    #in the middle or end of word that is found within another word
                    # will be on a whole other branch *uniqueness*
                else:
                    #create mapping
                    charFound = False
                    newTrie = TrieNode()
                    curr.children[char] = newTrie
                    curr.data.append(char)
                    curr.words = curr.words +1
                    #print("currchar=",char)
                    #print("currdata=",curr.data)
                    #print("isCompleteWord=",curr.isCompleteWord)
                    #traverse to next trie node
                    curr = curr.children[char]
        curr.isCompleteWord = True
        #print("isCompleteWord=",curr.isCompleteWord)
        return
                    
    def find(self, partial):
        if len(partial) == 0:
            return 0
        curr = self.root
        for i in range(0,len(partial)):            
            char = partial[i]
            if char in curr.data:
                curr = curr.children[char]
                continue
            else:
                return 0

        if curr.isCompleteWord == True:
            return curr.words +1
        return curr.words 
def main():
    
    #n = int(input())
    #
    f =open("testcases.txt","r")
    f1 = f.readlines()
    n = int(f1[0])
    print(n)
    #
    sol = Solution()
    
    #for n_itr in range(n):
    count = 0
    for n_itr in f1:
        count = count +1
        if n_itr ==f1[0]:
            continue
        #opContact = input().split()
        #
        opContact=n_itr.split()
        #
        print(opContact)
        op = opContact[0]

        contact = opContact[1]
        contactQ = list(contact)
        
        if op == "add":
            sol.add(contactQ)
        if op == "find":
            f = open("result.txt", "a+")
            if count != n:
                f.write(str(sol.find(contactQ))+"\n")
                print(sol.find(contactQ))
            else:
                f.write(str(sol.find(contactQ)))
                print(sol.find(contactQ))                
    f.close
    with open('result.txt','r') as hosts0:
        with open("sol.txt",'r') as hosts1:
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
