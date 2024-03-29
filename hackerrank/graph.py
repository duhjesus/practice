# dfs at the very bottom with adj list implementation
# bfs below w/ adj matrix implementation
class Graph():
    def __init__(self, n):
        self.n = n
        self.nodelookup = {} # key=id,val=[boolean visited, distance from node v]
        row = [0 for i in range(0,n)]
        self.adjMatrix = [ row.copy() for j in range(0,n)]     
    def connect(self, u, v):
        self.adjMatrix[u][v] = 1
        self.adjMatrix[v][u] = 1

    def find_all_distances(self,s): #starting node
        # for row in self.adjMatrix:
        #     print(row)
        for i in range(0,self.n):
            self.nodelookup[i] = [False,-1]
        queue = []
        root = s
        queue.append(s)
        self.nodelookup[root][1] = 0
        while len(queue) != 0:
            v = queue.pop(0)
            for  i in range(0,self.n): # neighbors of v
                if i ==v:
                    continue #skip
                if self.adjMatrix[v][i] == 1:
                    if self.nodelookup[i][0] == False:
                        queue.append(i)
                        self.nodelookup[i][0] = True
                        self.nodelookup[i][1] = self.nodelookup[v][1]+6
                        #adds the edge weight of grandparent ->parent to 
                        # edge weight of parent->child (self.nodelookup[i][1])
        for i in range(0,self.n):
            if i ==root:
                continue
            if i == self.n-1:
                print(self.nodelookup[i][1])
            else:                
                print(self.nodelookup[i][1], end=' ')

            
                        
def main():
    t = int(input())
    for i in range(t):
        n,m = [int(value) for value in input().split()]
        graph = Graph(n)
        for i in range(m):
            x,y = [int(x) for x in input().split()]
            #print(x,y)
            graph.connect(x-1,y-1) 
        s = int(input())
        s = s-1
        graph.find_all_distances(s)
        #print("done with test")
if __name__ == "__main__":
    main()
###############################
# below  dfs and adj list
#
class Node():
    def __init__(self,id=None):
        self.id = id
        self.next= None

class LinkedList():
    def __init__(self,head):
        self.head = head
        self.tail = head
    def add(self,nodeToAdd):
        if self.head == None:
            self.head =nodeToAdd
            self.head = self.tail
        elif self.head == self.tail:
            self.tail= nodeToAdd
            self.head.next = self.tail
        else:
            self.tail.next = nodeToAdd
            self.tail = self.tail.next
    # def insert(self,id):
    #     if self.head == None:
    #         self.head =Node(id)
    #         self.head = self.tail
    #     elif self.head == self.tail:
    #         self.tail= Node(id)
    #         self.head.next = self.tail
    #     else:
    #         self.tail.next = Node(id)
    #         self.tail = self.tail.next
    def delete(self,val):
        if self. head == None:
            print("Empty: No deletion")
            return
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
                    print("Deleted Node id=",val)
                    break
                else:
                    if curr ==self.head:
                        curr = self.head.next
        
                    else:
                        before =curr
                        curr = curr.next

#!
#ctrl +/ results in entire code block being edited out
#!

class Vertex():
    def __init__(self,index):
        self.id = index
        self.next= None
        self.visited = False
class Graph():
    def __init__(self):
        self.adjList = []#aadjacence list rray of linkedlists where head is
                         #vertex and all nodes in list are neighbors
        self.nodelookup = {} # easily access node's idx in the adjlist
                             # key = node's id, val = idx in adjlist
    #create's the graph structure by
    #finding actual nodes of graph in the grid
    #and by generating an adjlist
    #
    def create(self, grid, n , m):
        for i in range(0,n):
            for j in range(0,m):
                if grid[i][j] == 0:
                    continue
                index = i*m+j
                curr = Vertex(index)
                templl = LinkedList(curr)
                self.nodelookup[index] = len(self.adjList)
                x = []
                x.append([i-1,j-1])
                x.append([i-1,j])
                x.append([i-1,j+1])
                x.append([i,j-1])
                x.append([i,j+1])
                x.append([i+1,j-1])
                x.append([i+1,j])
                x.append([i+1,j+1])
                for position in x:
                    if position[0] <0 or position[0]>=n:
                        continue                        
                    elif position[1] <0 or position[1]>=m:
                        continue 
                    elif grid[position[0]][position[1]] == 0:
                        continue 
                    else:
                        idx = position[0]*m+position[1]
                        neighbor = Vertex(idx)
                        templl.add(neighbor)
                self.adjList.append(templl)

    def dfsCount(self):
        if len(self.adjList) == 0:
            return 0
        maxx = 0
        adjIndex = 0
        while adjIndex < len(self.adjList): # goes thru all the disconnected regions
            cnt = 0
            stack = []
            curr = self.adjList[adjIndex].head            
            if curr.visited == False: 
                stack.append(curr)                
                while len(stack) != 0: # goes thru all the connected cells w/in one region
                    v = stack.pop()                    
                    if v.visited == False:
                        v.visited = True
                        cnt = cnt + 1 # keeps track of current region's 
                                      # current amt of found vertices
                        vhead = v.next                      
                        while( vhead != None):
                            nodeIndex =self.nodelookup[vhead.id] # lookup node's idx in the list
                            stack.append(self.adjList[nodeIndex].head)
                            vhead = vhead.next                        

            adjIndex = adjIndex + 1
            if maxx < cnt:
                maxx = cnt
        return maxx

def main():
    g = Graph()
    g.create(grid, n, m)
    cnt = g.dfsCount()
    print(cnt)

if __name__=="__main__":
    main()
