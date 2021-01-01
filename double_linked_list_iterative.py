class Node(object):
    def __init__(self, d, n = None, p= None):
        self.data = d
        self.next_node = n
        self.prev_node = p
    def get_next (self):
        return self.next_node
    def set_next (self, n):
        self.next_node = n
    def get_prev (self):
        return self.prev_node
    def set_prev (self, p):
        self.prev_node = p
    def get_data (self):
        return self.data
    def set_data (self, d):
        self.data = d
class DoubleLinkedList (object):
    def __init__(self, r=None):
        self.root = r
        self.size = 0
    def get_size (self):
        return self.size
    def add (self, d):
        new_node = Node (d, self.root)
        self.root = new_node
        self.size += 1
    def remove (self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                print("found the right node")
                if this_node.prev_node:
                    print("this node had a previous node")
                    prev_node.set_next(this_node.get_next())
                    print("previous node's next node changes to the current node's next node")
                else:
                    print("this node doesn't have a previous node")
                    self.root = this_node.get_next()
                    print("reassign the root node to be this current node's next node")
                self.size -= 1
                return True
            else:
                this_node.prev_node = this_node
                this_node = this_node.get_next()
        return False
    def find (self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                    this_node = this_node.get_next()
        return None

myList = DoubleLinkedList()
myList.add("Breakfast")
myList.add("Lunch")
myList.add("Dinner")
print(myList.remove("Dinner"))
print(myList.find("Lunch"))
print(myList.find("Dinner"))