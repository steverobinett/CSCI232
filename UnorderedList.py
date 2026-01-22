class Node:
    """A node of a linked list"""

    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        """Get node data"""
        return self._data

    def set_data(self, node_data):
        """Set node data"""
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        """Get next node"""
        return self._next

    def set_next(self, node_next):
        """Set next node"""
        self._next = node_next

    next = property(get_next, set_next)

    def __str__(self):
        """String"""
        return str(self._data)


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    # this implementation will always add new item to front of list
    def add(self, item):

        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next

        return count

    def search(self, item):
        current = self.head
        if current is not None:
            if current.data == item:
                return True
        current = current.next

        return False

    def remove(self, item):
        current = self.head

        previous = None

        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next

        if current is None:
            raise ValueError(f"{item} is not in the list")
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    # implement the following methods for the assignment

    def append(self, item):
        pass

    def insert(self, pos, item):
        pass

    def index(self, item):
        pass

    def pop(self, pos):
        pass
    
    def __str__(self):
        return "Not implmented yet"
       

#test code
def main():
    myList = UnorderedList()

    print("Starting list")
    
    # build your list here
    
    

    # test the methods here

    print("Ending list:")
    


main()
