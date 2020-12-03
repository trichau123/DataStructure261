import random
"""Python program to create binary tree from random array."""
 
# A Binary Tree Node 
# Utility function to create a new tree node 
class newNode: 
 
    # Constructor to create a newNode 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
                if self.left is None:
                    self.left = newNode(data)
                elif self.left is not None:
                    self.left.insert(data)
                elif self.right is None:
                    self.right = newNode(data)
                elif self.right is not None:
                    self.right.insert(data)
        else:
            self.data = data
            


    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

def ifNodeExists(node, key):
      if ( node == None):
        return False
      if (node.data == key):
        return True
      res1 = ifNodeExists(node.left,key)
      if res1:
        return True

if __name__ == '__main__':
    a = random.sample(range(100), 30)
    print (a)
    root = newNode(a[0]) 
    for i in range(1,30):
      root.insert(a[i])
    print("BINARY TREE: ")
    root.PrintTree()
    key = random.randint(0,100)
    print("RANDOM NUMBER : ", key)
    if (ifNodeExists(root, key)): 
        print("FOUND" )
    else:
        print("NOT FOUND")

  #print graphic
"""    print("BINARY TREE")
    print("                   ",root.data)
    print("             /           \\       ")
    print("           ",root.left.data,"          ",root.right.data)
    print("         /   \\          /   \\")
    print("       ",root.left.left.data,"    ",root.left.right.data,"   ",root.right.left.data,"    ",root.right.right.data," ")
    print("     /    \\       \\           \\  ")

    print("    ",root.left.left.left.data,"    ",root.left.left.right.data,"    ",root.left.right.right.data,"        ", root.right.right.right.data)
    print("                   /")
    print("                ", root.left.right.right.left.data)"""
