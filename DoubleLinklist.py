class Node(object):
    def __init__(self,d, n = None , p = None):
        self.data = d
        self.next_node = n
        self.prev_node = p
    #getter setter access change, data, pre, next pointer
    def get_next (self):
        return self.next_node;

    def set_next (self, n):
        self.next_node = n

    def get_prev ( self):
        return self.prev_node

    def set_prev (self, p):
        self.prev_node = p

    def get_data(self):
        return self.data

    def set_data (self, d):
        self.data = d

    def to_string(self):
        return "Node value: " + str(self.data)

    def has_next(self):
        if self.get_next() is None:
            return False
        return True

#Class linked lists
class DoublyLinkedList():

    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def get_size (self):
        return self.size

    def add (self, d ):
        new_node = Node (d, self.root)
        if  (self.root ==  None):
            self.root = new_node
        else:
            self.root = new_node
        self.size += 1


    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.get_data() == d:
                return d
            elif this_node.get_next() == self.root:
                return False
            else:
                this_node = this_node.get_next()

    def print_list(self):
        print ("Print List..........")
        if self.root is None:
            return
        this_node = self.root
        print (this_node.to_string())
        while this_node.has_next():
            this_node = this_node.get_next()
            print (this_node.to_string())

    def getNext(self, next,prev):
        if self.root is None:
            return
        this_node = self.root
        a = this_node.get_data()
        this_node.set_next(next)
        this_node.set_prev(prev)
        print("funtion getdata",a)
        print("get prev ", this_node.get_prev())
        print("get Next ",this_node.get_next())

    def setter(self, next):
        if self.root is None:
            return
        this_node = self.root
        this_node.set_next(next)
        #this_node.set_prev(prev)


def main():
        myList = DoublyLinkedList()
        myList.add("A")
        #myList.setter("B",None)
        myList.getNext("B",None)
        myList.add("B")
        #myList.setter("D")
        myList.getNext("D","E")
        myList.add("C")
        myList.getNext("A",None)
        myList.add("D")
        myList.getNext("H","B")
        myList.add("E")
        myList.getNext("K","C")
        myList.add("F")
        myList.getNext("J","C")
        myList.add("G")
        myList.getNext("I","F")
        print("size=" + str(myList.get_size()))

main()
