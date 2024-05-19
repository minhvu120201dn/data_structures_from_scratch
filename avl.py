from data_structure import DataStructure

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

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

    def add(self, value:int) -> None:
        #TODO
        pass

    def remove(self, value:int) -> bool:
        #TODO
        pass

    def find(self, value:int) -> bool:
        #TODO
        pass

    def findMax(self) -> int:
        #TODO
        pass