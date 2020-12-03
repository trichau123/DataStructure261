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
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()


if __name__ == '__main__':
    a = random.sample(range(18), 12)
    print (a)
    root = newNode(a[0]) 
    root.left = newNode(a[1]) 
    root.right = newNode(a[2])
    root.left.left = newNode(a[3]) 
    root.right.right = newNode(a[4])
    root.left.right = newNode(a[5])
    root.left.right.right = newNode(a[6]) 
    root.right.right.right = newNode(a[7]) 
    root.left.left.right = newNode(a[8]) 
    root.left.right.right.left = newNode(a[9])
    root.left.left.left = newNode(a[10]) 
    root.right.left = newNode(a[11])
  #print graphic
    print("BINARY TREE")
    print("                   ",root.data)
    print("             /           \\       ")
    print("           ",root.left.data,"          ",root.right.data)
    print("         /   \\          /   \\")
    print("       ",root.left.left.data,"    ",root.left.right.data,"   ",root.right.left.data,"    ",root.right.right.data," ")
    print("     /    \\       \\           \\  ")

    print("    ",root.left.left.left.data,"    ",root.left.left.right.data,"    ",root.left.right.right.data,"        ", root.right.right.right.data)
    print("                   /")
    print("                ", root.left.right.right.left.data)







