class Node(object):
    def __init__(self, d, n = None):
        self.data = d
        self.next_node = n
    def get_next (self):
        return self.next_node
    def set_next (self, n):
        self.next_node = n
    def get_data (self):
        return self.data
    def set_data (self, d):
        self.data = d
class BinaryTree (object):
    def __init__(self, r=None):
        self.root = r
        self.size = 0
    def get_size (self):
        return self.size
    def add (self, d):
        new_node = Node (d, self.root)
        self.root = new_node
        self.size += 1
    def remove (self, this_node, d):
        #this_node = self.root
        prev_node = None
        if this_node.get_data() == d:
            print("d is equal to: " + str(d))
            if prev_node:
                prev_node.set_next(this_node.get_next())
            else:
                self.root = this_node
            self.size -= 1
            print("d removed")
            return True
        else:
            if this_node.get_next() == None:
                return None
            else:
                return self.remove(this_node.get_next(),d)
    def find (self, this_node, d):
        if this_node.get_data() == d:
            print("d is equal to: " + str(d))
            return d
        else:
            if this_node.get_next() == None:
                return None
            else:
                return self.find(this_node.get_next(),d)

myList = BinaryTree()
myList.add(5)
myList.add(17)
myList.add(23)
#x = myList.find(myList.root,5)
y = myList.remove(myList.root,5)
#print(x)
print(y)
x = myList.find(myList.root,5)
print(x)
#print(myList.root.get_next().get_data())
