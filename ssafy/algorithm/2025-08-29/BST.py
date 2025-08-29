class Node():
    def __init__(self, t):
        self.left = None
        self.right = None
        self.value = t
    
    def search(self, t):
        if t == self.value:
            return print("find!")
        elif self.value is None:
            return print("not exist!!")
        elif t < self.value:
            self.search(self.left)
        elif t > self.value:
            self.search(self.right)

    def insert(self, t):
        pass

    def delete(self, t):
        pass

    def find(self, t):
        pass

head = Node()