#!/bin/python3

import math
import os
import random
import re
import sys
# function: helper function 
#           merges left and right half arrays in sorted order
# input:nums= array to be sorted
#       temp= place holder array, hard to do inplace sorting
#       leftStart = start index of the left half array
#       rightEnd =  end index of the right half array
# ouput: none
# effect: sorts portion of nums array
def mergeHalves(nums, temp, leftStart,rightEnd):
    leftEnd = leftStart+ (rightEnd-leftStart)//2 #middle 
    rightStart = leftEnd +1 # middle +1
    size = rightEnd -leftStart +1

    left = leftStart
    right = rightStart
    index = leftStart
    cnt = 0
    #comparing elements of the two halves 
    #smaller element of the two taken and copied into temp array
    #then the array's(that the smaller element was in) ptr is incremented
    #compared again until you reach the end of one of the arrays first

    while(left <= leftEnd and right<=rightEnd):
    
        if nums[left] <=nums[right]:
            temp[index]=nums[left]
            left =left +1

        else:
            temp[index] = nums[right]
            right = right +1
            cnt = cnt + leftEnd+1 -left
        index = index +1
    # recall python array slices go from left index : to right index (not inclusive on the right end)
    # only one or the other of the halves will have remaining elements so only one of the two following lines
    # will have an effect
    # copying remaining elements of left half and right half
    temp[index:index + leftEnd-left+1]=nums[left:left +leftEnd-left+1]
    temp[index:index + rightEnd-right+1]=nums[right: right +rightEnd-right+1]
    nums[leftStart:leftStart+size]=temp[leftStart:leftStart+size]
    #print("result:",nums)
    return cnt
def mergesort(nums, temp, leftStart, rightEnd):
    if leftStart >= rightEnd:
        return 0

    middle = leftStart+ (rightEnd-leftStart)//2 #written like this b/c (leftstart+rightend )/2 <-overflows
    cntl = mergesort(nums,temp,leftStart,middle)
    cntr = mergesort(nums,temp,middle+1,rightEnd)
    cntm = mergeHalves(nums,temp, leftStart,rightEnd)
    return cntl+cntr+cntm

# Complete the countInversions function below.
def countInversions(arr):
    temp = list(0 for i in range(0,len(arr)))
    theCnt =mergesort(arr,temp,0,len(arr)-1)
    return theCnt
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))
        success = True
        for i in range(0,len(arr)-1-1):
            if arr[i]<= arr[i+1]:
                continue
            else:
                success =False
                break
        if success == True:
            result = 0
        else:
            result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
