from data_structure import DataStructure



class LinkedList:
    class Node:

        # Initialize the node with a value, and its next node, the default is none
        def __init__(self, value=None):
            self.value = value
            self.next = None
    
    def __init__(self):

        # Initialize a single Linked List, with the default size is 0, it will increase whenever there is a new node
        self.head = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def add(self, value: int) -> None:
        # Create new node with head = None
        newNode = LinkedList.Node(value)

        # If this node is the first node
        if not self.head:
            self.head = newNode
        
        # If this node is not the first node, then find the lastest node using the while.
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode

        # Increase Linked List size
        self.size += 1

    def remove(self, value: int) -> bool:
        current = self.head
        previous = None
        while current:
            if current.value == value:
                
                # If previous is not none, meaning this node is note the first node
                if previous:
                    previous.next = current.next
                else:
                # If the node is the head
                    self.head = current.next
                self.size -= 1
                return True
            
            # If it do not match the value, then just move on
            previous = current
            current = current.next
        return False

    def find(self, value: int) -> bool:
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def findMax(self) -> int:
        max_value = self.head.value
        current = self.head.next
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value
