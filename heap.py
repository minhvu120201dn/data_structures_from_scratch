from data_structure import DataStructure

class Heap(DataStructure):

    def __init__(self):
        self.arr = []

    def __len__(self) -> int:
        return len(self.arr)

    def parent(i:int) -> int:
        return (i-1) // 2
    
    def getValue(self, i:int) -> int:
        return self.arr[i]

    def leftChild(self, i:int) -> int:
        return (2*i) + 1
    
    def rightChild(self, i:int) -> int:
        return (2*i) + 2


    def add(self, value:int) -> None:
        self.arr.append(value)

        i = len(self.arr) - 1
        
        while i > 0:
            parent = Heap.parent(i)

            if self.getValue(i) > self.getValue(parent):
                self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
                i = parent
            else: 
                break
        return

    def remove(self, value:int) -> bool:
        pass


    def removeMax(self) -> int:
        if len(self.arr) == 0:
            return

        if len(self.arr) == 1:
            return self.arr.pop()

        # Save the root value to return later
        root = self.arr[0]

        # Move the last element to the root
        self.arr[0] = self.arr.pop()

        i = 0
        while True:
            left = self.leftChild(i)
            right = self.rightChild(i)

            # Assume the current node is the largest
            largest = i  

            # Check if the left child exists and is greater than the current largest
            if left < len(self.arr) and self.arr[left] > self.arr[largest]:
                largest = left

            # Check if the right child exists and is greater than the current largest
            if right < len(self.arr) and self.arr[right] > self.arr[largest]:
                largest = right

            # If the largest is not the current node, swap them
            if largest != i:
                self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
                i = largest
            else:
                # If no swaps were made, the heap is in a valid state
                break

        return root

    def find(self, value:int) -> bool:
        for item in self.arr:
            if item == value:
                return True
        return False

    def findMax(self) -> int:
        return self.arr[0]
    
    def __str__(self):
        return str(self.arr)