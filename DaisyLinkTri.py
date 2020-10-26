import random
c = ""
class Node:
  #constructor
  def __init__(self, data, next = None):
    self.data = data
    self.next = next
#A linked list class with a single head Node
class linkedList:
  def __init__(self):
    self.head = None
  #insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
#print method for the linked list
 
  def printLL(self):
    c = ""
    current = self.head
    while(current):
      c += str(current.data)
      current = current.next
    return c
con = "y"
while(con == "y" or con == "Y"):     
  #createing a single Node
  LL = linkedList()
  a = random.randint(0,14)
  #pick a random position
  for i in range(14):
    if (i <a):#if i greater than random num print 0
      LL.insert(1)y
    else:
      LL.insert(0)

  def print_frame(n, m, c):
       print(c[0]," -->",c[1],"-->",c[2],"-->",c[3],"-->",c[4])
       print("^",22*" ","|")
       print("|",22*" ","v")
       print(c[13],22*" ",c[5])
       print("^",22*" ","|")
       print("|",22*" ","v")
       print(c[12],22*" ",c[6])
       print("^",22*" ","|")
       print("|",22*" ","v")
       print(c[11]," <--",c[10],"<--",c[9],"<--",c[8],"<--",c[7])
  c = LL.printLL()
  print_frame(4, 5, c)
  con = input("Do you want to continue y Y : ")
