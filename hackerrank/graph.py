

class Node():
    def __init__(self,id=None):
        self.id = id
        self.next= None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self,id):
        if self.head == None:
            self.head =Node(id)
            self.head = self.tail
        elif self.head == self.tail:
            self.tail= Node(id)
            self.head.next = self.tail
        else:
            self.tail.next = Node(id)
            self.tail = self.tail.next
    def delete(self,val):
        if self. head == None:
            return "Empty: No deletion"
        else:
            curr = self.head
            before = self.head

            while(curr!= None):
                if curr.id == val:
                    if curr == self.head:
                        self.head =self.head.next
                    else:
                        before.next= curr.next

                    curr.next =None
                    print("Deleted Node containing=",val)
                    break
                else:
                    if curr ==self.head:
                        curr = self.head.next
        
                    else:
                        before =curr
                        curr = curr.next
            
class Graph():
    def __init__(self):
        # mapping from nodeid to mem
        self.adjMatrix = []
        self.adjList = {}
        
    def addVertex(self,)
def main():
    pass


if __name__=="__main__":
    main()
