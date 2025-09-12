'''
12
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
N = 12

arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, child):
        if self.left is None:
            self.left = child
            return
        if self.right is None:
            self.right = child
            return
        return
    
    def preorder(self):
        if self is not None:
            print(self.value, end=" ")
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
    
    def inorder(self):
        if self is not None:
            if self.left:
                self.left.preorder()
            print(self.value, end=" ")
            if self.right:
                self.right.preorder()
    
    def postorder(self):
        if self is not None:
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
            print(self.value, end=" ")

N = max(arr) + 1

nodes = [Node(i) for i in range(N)]

for i in range(0, len(arr), 2):
    parentnode = arr[i]
    childnode = arr[i + 1]
    nodes[parentnode].insert(nodes[childnode])

nodes[1].preorder()
print()
nodes[1].inorder()
print()
nodes[1].postorder()