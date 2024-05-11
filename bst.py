from data_structure import DataStructure

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        # Initialize the root of the BST as None
        self.root = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def add(self, value: int) -> None:
        # Add a value to the BST
        if self.root is None:

             # If tree is empty, set root to new node
            self.root = Node(value) 
        else:

            # Otherwise, use a helper to find the position to insert
            self._add(value, self.root)  

        self.size += 1

    def _add(self, value, node):
        
        # If the value is smaller, keep looking for the nearest empty left position and put the node there
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add(value, node.left)
                
        # Opposite with above
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add(value, node.right)

    def remove(self, value: int) -> bool:
        # Remove a value from the BST
        self.root, deleted = self._remove(self.root, value)
        if deleted:
            self.size -= 1
        return deleted

    def _remove(self, node, value):
        if node is None:
            return node, False
        if value < node.value:
            node.left, deleted = self._remove(node.left, value)
        elif value > node.value:
            node.right, deleted = self._remove(node.right, value)
        else:
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True
            temp = self._findMin(node.right).value
            node.value = temp
            node.right, _ = self._remove(node.right, temp)
            return node, True
        return node, deleted

    def find(self, value: int) -> bool:
        # Find a value in the BST
        return self._find(value, self.root)

    def _find(self, value, node):
        # Helper method to find a value
        if node is None:
            return False
        elif value == node.value:
            return True
        elif value < node.value:
            return self._find(value, node.left)
        else:
            return self._find(value, node.right)

    def findMax(self) -> int:
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value
    
    def _findMin(self, node):
        while node.left is not None:
            node = node.left
        return node