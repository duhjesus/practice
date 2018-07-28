#!/bin/python3

import math
import os
import random
import re
import sys
from array import array


class minHeap():
    def __init__(self):
        #self.capacity = 10
        #self.size = 0
        self.items = []
        self.size = len(self.items)
    def getLeftChildIndex(self,parentIndex):
        return parentIndex*2 +1
    def getRightChildIndex(self,parentIndex):
        return parentIndex*2 +2
    def getParentIndex(self,childIndex):
        return math.ceil(childIndex/2) -1
    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index) <len(self.items)
    def hasRightChild(self,index):
        return self.getRightChildIndex(index) <len(self.items)
    def hasParent(self,index):
        return self.getParentIndex(index) >= 0
    def leftChild(self,index):
        return self.items[self.getLeftChildIndex(index)]
    def rightChild(self,index):
        return self.items[self.getRightChildIndex(index)]
    def swap(self,indexOne, indexTwo):
        temp = self.items[indexOne]
        self.items[indexOne] = self.items[indexTwo]
        self.items[indexTwo] = temp
    #for languages using arrays instead of lists or vectors
    #def ensureExtraCapacity():
    #   if size== cpacity:
    #   copy array contents over to an array 2x the size
    #   and double the capcity
    def peek(self):
        if len(self.items)== 0:
            print("EMPTY HEAP")
            return None
        return self.items[0]
    
    #extracts minimum element
    def poll(self):
        if len(self.items) == 0:
            #print("EMPTY HEAP")
            return None
        el = self.items[0]
        #put last el in first spot(part of algorithm)
        self.items[0]= self.items[self.size-1]
        #delete last element in array
        self.items.pop()
        self.heapifyDown()
        #print("after heapifydown=", self.items)
        return el

    def add(self,item):
        #self.ensureExtraCapacity()
        self.items.append(item)
        self.heapifyUp()
        #print("after heapifyUp=",self.items)

    def heapifyUp(self):
        index = len(self.items)-1
        while self.hasParent(index) and self.items[self.getParentIndex(index)] > self.items[index]:
            self.swap(index,self.getParentIndex(index))
            index = self.getParentIndex(index)

    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            smallerChildIndex = self.getLeftChildIndex(index)
            #trying to go down to the smallest child
            if self.hasRightChild(index) and self.items[self.getRightChildIndex(index)] <self.items[self.getLeftChildIndex(index)]:
                smallerChildIndex = self.getRightChildIndex(index)
            if self.items[index] <self.items[smallerChildIndex]:
                break #done
            else:#keep going down the heap
                self.swap(smallerChildIndex,index)
                
            index= smallerChildIndex
    #
    # input: unsorted list, uninitialized heap to be declared in main
    # output: returns sorted list
    # ascending order using minheap
    def heapsort(self,alist, heap):
        print("list before sorting", alist)
        for el in alist:
            heap.add(el)
        copyItems=heap.items.copy() # heap gets its data deleted after a sort
        output = []
        while True:
            out = heap.poll()
            if out == None:
                break
            output.append(out)
        heap.items= copyItems.copy()
        print("the output = ",output)
        return output
##########
class maxHeap():
    def __init__(self):
        #self.capacity = 10
        #self.size = 0
        self.items = []
        self.size = len(self.items)
    def getLeftChildIndex(self,parentIndex):
        return parentIndex*2 +1
    def getRightChildIndex(self,parentIndex):
        return parentIndex*2 +2
    def getParentIndex(self,childIndex):
        return math.ceil(childIndex/2) -1
    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index) <len(self.items)
    def hasRightChild(self,index):
        return self.getRightChildIndex(index) <len(self.items)
    def hasParent(self,index):
        return self.getParentIndex(index) >= 0
    def leftChild(self,index):
        return self.items[self.getLeftChildIndex(index)]
    def rightChild(self,index):
        return self.items[self.getRightChildIndex(index)]
    def swap(self,indexOne, indexTwo):
        temp = self.items[indexOne]
        self.items[indexOne] = self.items[indexTwo]
        self.items[indexTwo] = temp
    #for languages using arrays instead of lists or vectors
    #def ensureExtraCapacity():
    #   if size== cpacity:
    #   copy array contents over to an array 2x the size
    #   and double the capcity
    def peek(self):
        if len(self.items)== 0:
            print("EMPTY HEAP")
            return None
        return self.items[0]
    
    #extracts max element
    def poll(self):
        if len(self.items) == 0:
            print("EMPTY HEAP")
            return None
        el = self.items[0]
        #put last el in first spot(part of algorithm)
        self.items[0]= self.items[self.size-1]
        #delete last element in array
        self.items.pop()
        self.heapifyDown()
        #print("after heapifydown=", self.items)
        return el

    def add(self,item):
        #self.ensureExtraCapacity()
        self.items.append(item)
        self.heapifyUp()
        #print("after heapifyUp=",self.items)

    def heapifyUp(self):
        index = len(self.items)-1
        while self.hasParent(index) and self.items[self.getParentIndex(index)] < self.items[index]:
            self.swap(index,self.getParentIndex(index))
            index = self.getParentIndex(index)

    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            smallerChildIndex = self.getLeftChildIndex(index)
            #trying to go down to the largest child
            if self.hasRightChild(index) and self.items[self.getRightChildIndex(index)] >self.items[self.getLeftChildIndex(index)]:
                smallerChildIndex = self.getRightChildIndex(index)
            if self.items[index] >self.items[smallerChildIndex]:
                break #done
            else:#keep going down the heap
                self.swap(smallerChildIndex,index)
                
            index= smallerChildIndex
    #
    # input: unsorted list, uninitialized heap to be declared in main
    # output: returns sorted list
    # descending order using minheap
    def heapsort(self,alist, heap):
        print("list before sorting", alist)
        for el in alist:
            heap.add(el)
        copyItems=heap.items.copy() # heap gets its data deleted after a sort
        output = []
        while True:
            out = heap.poll()
            if out == None:
                break
            output.append(out)
        heap.items= copyItems.copy()
        print("the output = ",output)
        
def main():
    minHeap1 = minHeap()
    maxHeap1 = maxHeap()
    
    
    #alist = [25,67,56,32,12,96,82,44]
    #alistSorted= heap.heapsort(alist,heap)

    n = int(input())
    
    a = []
    size = 0
    for _ in range(n):
        size = size +1
        a_item = int(input())
        a.append(a_item)
        if size <2:
            print(a_item*1.0)
            continue
            
        #Step 0: add the smaller of the first 
        #two values to init the minHeap and
        #the maxHeap
        if size ==2:
            if a[0] < a[1]:
                minHeap1.add(a[1])
                maxHeap1.add(a[0])
            else:
                minHeap1.add(a[0])
                maxHeap1.add(a[1])
            print((a[0] +a[1])/2 *1.0)
            continue
        #Step 1: Add next item to one of the heaps
        #if next item is smaller than maxHeap root add it to maxHeap,
        #else add it to minHeap
        if maxHeap1.items[0] > a_item:
            maxHeap1.add(a_item)
        else:
            minHeap1.add(a_item)
        #Step 2: Balance the heaps (after this step heaps will be either balanced or
        #one of them will contain 1 more item)
        #if number of elements in one of the heaps is greater than the other by
        #more than 1, remove the root element from the one containing more elements and
        #add to the other one
        minHeapLen =len(minHeap1.items)
        maxHeapLen =len(maxHeap1.items)
        if abs(maxHeapLen - minHeapLen) > 1:
            if minHeapLen > maxHeapLen:
                val = minHeap1.poll()
                maxHeap1.add(val)
            else:
                val = maxHeap1.poll()
                minHeap1.add(val)
        #step 3: if equal( even amount) of elements in minHeap and MaxHeap
        #then add the roots of the min heap and max heap and divide by 2
        #B/C we added the values > median to the min heap so that
        #the min heap's root is the smallest value of the larger numbers
        #values < median were added to the max heap so that the maxHeap root
        #is the value of the largest value of the smaller numbers
        #i.e. example [3,5,1,2,6,4] -> minHeap w/ root 4
        #-> maxHeap w/ root 3 --> so (3+4)/2 = median
        # 1 skipped b/c 1 element
        #the two heaps
        # min=5 max=3 ->min=5 max=3,1 ->min=5 max=3,1,2 ->min=3,5 max=2,1
        # min=3,5,6  max=2,1 ->min=3,4,5,6 max=2,1 ->min=4,5,6 max=3,2,1
        
        # find the lengths again b/c we may had to balance the heaps
        minHeapLen =len(minHeap1.items)
        maxHeapLen =len(maxHeap1.items)
        if minHeapLen == maxHeapLen:
            print((minHeap1.peek()+maxHeap1.peek())/2 *1.0)
        else:
            if minHeapLen >maxHeapLen:
                print(minHeap1.peek()*1.0)
            else:
                print(maxHeap1.peek()*1.0)
        #print("minheap=",minHeap1.items)
        #print("maxheap=",maxHeap1.items)
if __name__ == '__main__':
    main()