class Node(object): # this is a definition of a class 'Node'
    def __init__(self, d, n = None): # Initializes the 'Node' object with parameters of data & next node
        self.data = d # setting 'data' attribute to the 'd' parameter
        self.next_node = n # setting 'next_node' attribute to the 'n' parameter
    def get_next (self): # retrieves the next node
        return self.next_node # returns the next node being pointed to
    def set_next (self, n):# assigns the next node
        self.next_node = n # setting 'next_node' attribute to the 'n' parameter
    def get_data (self): # retrieves the data of this node
        return self.data # returns the data of this node
    def set_data (self, d): # assigns the data of this node
        self.data = d # defining 'data' attribute to the 'd' parameter
class LinkedList (object): # this is a definition of a class 'LinkedList'
    def __init__(self, r=None): # Initializes the 'LinkedList' object with parameter of root
        self.root = r
        self.size = 0
    def get_size (self): # retrieves the length of the list
        return self.size
    def add (self, d): # creates new node and pushes it to the list
        new_node = Node (d, self.root) # initializing a 'new_node' with 'd' as the data and root as the next_node
        self.root = new_node
        self.size += 1 # increments the length of the list
    def remove (self, d): # removes node based on the data passed in from the parameter
        this_node = self.root
        prev_node = None
        while this_node: # as long as there's a node...
            if this_node.get_data() == d: # checks to see if the node's data matches the 'd' parameter
                if prev_node: # as long as there's a prev_node...
                    print(prev_node.get_data()) # displays the prev_node's data
                    prev_node.set_next(this_node.get_next()) # assigns the prev_node's next_node pointer to the node that follows this one
                else: # node's data does not match the 'd' parameter...
                    self.root = this_node.get_next() # assigns the root to the node that follows this one
                self.size -= 1 # decrements the length of the list
                return True # the node was successfully removed
            else:
                prev_node = this_node # assigns this_node to now be the prev_node
                this_node = this_node.get_next() # assigns the next_node to now be this_node
        return False # data wasn't found; no node removed
    def find (self, d): # finds node based on the data passed in from the parameter
        this_node = self.root
        while this_node: # as long as there's a node...
            if this_node.get_data() == d: # checks to see if the node's data matches the 'd' parameter
                return d # displays the data
            else: # node's data does not match the 'd' parameter...
                    this_node = this_node.get_next() # assigns the next_node to now be this_node
        return None # data wasn't found; no node found

myList = LinkedList() # initalizing a new list called 'myList'
myList.add("Breakfast") # adding "Breakfast" to myList
myList.add("Lunch")
myList.add("Dinner")
myList.remove("Dinner") # removing "Dinner" from myList
print(myList.remove("Dinner")) # displaying the result of removing "Dinner" from myList
print(myList.find("Lunch")) # displaying the result of finding "Lunch" from myList
print(myList.find("Dinner"))