from data_structure import DataStructure

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

class AVLTree(DataStructure):
    def __init__(self):
        self.root = None

    def __len__(self) -> int:
        #TODO
        pass

    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def updateHeight(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def getBF(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def balancing(self, node) -> Node:
        bf = self.getBF(node)

        if bf == 2:
            pass
            # LL
            if node.left.right == None:
                temp = node
                node = node.left
                node.left.right = temp
            # LR
            
        elif bf == -2:
            # RR
            if node.right.left == None:
                temp = node
                node = node.right
                node.right.left = temp
            # RL
            else:
                tempLeft = node.right.left.left
                tempRight = node.right.left.right
                temp1 = node
                temp2 = node.right
                node = node.right.left
                node.left = temp1
                node.right = temp2
                node.left.right = tempLeft
                node.right.left = tempRight


    def add(self, value:int):
        def add_and_update_height(node:Node, value:int) -> Node:
            if node == None:
                return Node(value)
            elif value < node.value:
                node.left = add_and_update_height(node.left)
            else:
                node.right = add_and_update_height(node.right)
            self.balancing(node)
            self.updateHeight(node)
        add_and_update_height(self.root, value)





    def remove(self, value:int) -> bool:
        #TODO
        pass

    def find(self, value:int) -> bool:
        #TODO
        pass

    def findMax(self) -> int:
        #TODO
        pass