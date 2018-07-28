#Note:
#in other languages, there's the issue of resizing
#and memory allocation that makes the problem 
#a little more interesting.

#singly-linked list Node
class Node():
    def __init__(self, data= None):
        self.data = data
        self.next = None

#list-based stack
class listStack():
    def __init__(self):
        self.items = []
        self.top = None
    def isEmpty(self):
        return self.top == None
    def peek(self):
        if self.isEmpty():
            #print("EMPTY")
            return None
        return self.items[0]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()

#list-based queue
class listQueue():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def peek(self):
        return self.items[0]
    def add(self,data):
        self.items.append(data)
    def remove(self):
        return self.items.pop(0)

#linkedlist-based queue
class llQueue(Node):
    def __init__(self):    
        self.head = None # remove from head O(1)
        self.tail = None # add to tail O(n)
    def isEmpty(self):
        return self.head == None
        
    def peek(self):
        if self.isEmpty():
            print("queueError: Queue is Empty")
            return None
        return self.head.data
        
    def add(self, data):
        node = Node(data)
        if self.tail != None:
            self.tail.next = node
            
        self.tail = node
        if self.head == None:
            self.head = node

    def remove(self):
        if self.isEmpty():
            print("queueError: Queue is Empty")
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        return data

#linkedlist-based stack
class llStack(Node):
    def __init__(self):
        self.top= None
    def isEmpty(self):
        return self.top == None
    def peek(self):
        if self.isEmpty():
            print("StackError: Stack is Empty")
            return None
        return self.top.data

    def push(self,data):
        node = Node(data)
        node.next = self.top
        self.top = node 
        
    def pop(self):
        if self.top == None:
            #print("StackError: Stack is Empty")
            return None
        popped = self.top.data
        self.top = self.top.next
        return popped

#two stacks-based queue
class MyQueue(llStack):
    def __init__(self):
        self.stackE = llStack()
        self.stackD = llStack()
    def isEmpty(self):
        return self.stackE.isEmpty() and self.stackD.isEmpty()

    def peek(self):
        if self.isEmpty():
            print("EMPTY")
            return None
        if self.stackD.isEmpty():
            while(self.stackE.isEmpty() == False):
                data = self.stackE.pop()
                self.stackD.push(data)
        return self.stackD.peek()

    def pop(self):
        if self.isEmpty():
            print("EMPTY pop")
            return None
        if self.stackD.isEmpty():
            while(self.stackE.isEmpty() == False):
                data = self.stackE.pop()
                self.stackD.push(data)
        return self.stackD.pop()

    def put(self, value):
        self.stackE.push(value)

def main():
    queue = MyQueue()
    t = int(input())
    for _ in range(t):
        values = map(int, input().split())
        values = list(values)
        #print(values[0],"start")
        if values[0] == 1:
            queue.put(values[1])        
        elif values[0] == 2:
            queue.pop()
        else:
            print(queue.peek())
        #print(values[0],"end")
if __name__ == '__main__':
    main()