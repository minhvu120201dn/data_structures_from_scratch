from data_structure import DataStructure

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # Initially, a new node's height is set to 1

class AVLTree(DataStructure):
    def __init__(self):
        self.root = None

    def __len__(self) -> int:
        def count_nodes(node: Node) -> int:
            if not node:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)
        
        return count_nodes(self.root)

    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def updateHeight(self, node):
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

    def getBF(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rotateLeft(self, node):
        rightChild = node.right
        rightChildLeft = rightChild.left

        rightChild.left = node
        node.right = rightChildLeft

        self.updateHeight(node)
        self.updateHeight(rightChild)

        return rightChild

    def rotateRight(self, node):
        leftChild = node.left
        leftChildRight = leftChild.right

        leftChild.right = node
        node.left = leftChildRight

        self.updateHeight(node)
        self.updateHeight(leftChild)

        return leftChild

    def balancing(self, node: Node) -> Node:
        balance_factor = self.getBF(node)

        # Left heavy case
        if balance_factor > 1:
            # LR
            if self.getBF(node.left) < 0:
                node.left = self.rotateLeft(node.left)
            # LL
            return self.rotateRight(node)

        # Right heavy case
        if balance_factor < -1:
            # RL
            if self.getBF(node.right) > 0:
                node.right = self.rotateRight(node.right)
            # RR
            return self.rotateLeft(node) 

        return node 


    def add(self, value: int):
        def add_and_update_height(node: Node, value: int) -> Node:
            if not node:
                return Node(value)
            elif value < node.value:
                node.left = add_and_update_height(node.left, value)
            else:
                node.right = add_and_update_height(node.right, value)

            self.updateHeight(node)
            return self.balancing(node)

        self.root = add_and_update_height(self.root, value)

    def remove(self, value: int) -> bool:
        def remove_node(node: Node, value: int) -> Node:
            if not node:
                return None
            elif value < node.value:
                node.left = remove_node(node.left, value)
            elif value > node.value:
                node.right = remove_node(node.right, value)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                temp = self.findMin(node.right)
                node.value = temp.value
                node.right = remove_node(node.right, temp.value)

            self.updateHeight(node)
            return self.balancing(node)

        def node_exists(node: Node, value: int) -> bool:
            if not node:
                return False
            if node.value == value:
                return True
            elif value < node.value:
                return node_exists(node.left, value)
            else:
                return node_exists(node.right, value)

        if node_exists(self.root, value):
            self.root = remove_node(self.root, value)
            return True
        return False

    def find(self, value: int) -> bool:
        def find_value(node: Node, value: int) -> bool:
            if not node:
                return False
            if node.value == value:
                return True
            elif value < node.value:
                return find_value(node.left, value)
            else:
                return find_value(node.right, value)
        
        return find_value(self.root, value)

    def findMin(self, node: Node) -> Node:
        current = node
        while current.left:
            current = current.left
        return current

