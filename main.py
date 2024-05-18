import linked_list
import bst
import heap

def subsetsRecursive(s):
    def recurse(current, index):
        if index == len(s):
            subsets.append(current.copy())
            return
        # Include the current element
        current.append(s[index])
        recurse(current, index + 1)
        # Exclude the current element
        current.pop()
        recurse(current, index + 1)

    subsets = []
    recurse([], 0)
    return subsets

# Example usage
s = [1, 2, 3]
subsets_recursive = subsetsRecursive(s)
print("Recursive Subsets:", subsets_recursive)


def main():
    '''Linked List'''
    my_list = linked_list.LinkedList()

    my_list.add(47)
    my_list.add(3)
    my_list.add(2003)
    my_list.add(4703)
    my_list.add(4747)

    # Checking if a specific element is in the list
    # print(my_list.find(472003))
    # print(my_list.find(47))

    '''myBST'''
    # Create an instance of BinarySearchTree
    myBST = bst.BinarySearchTree()

    # Add nodes to the myBST
    for i in range(100):
        myBST.add(i)



    # Try finding a value
    x = 60
    if myBST.find(x):
        print(f"{x} found")
    else:
        print(f"{x} not found")

    x = 101
    if myBST.find(x):
        print(f"{x} found")
    else:
        print(f"{x} not found")

    # Remove a node
    y = 30
    if myBST.remove(y):
        print(f"{y} was removed.")
    else:
        print(f"{y} was not found")

    # Find the maximum value in the myBST
    z = myBST.findMax()
    print(f"{z}")

    '''Heap'''
    myHeap = heap.Heap()
    myHeap.add(4)
    myHeap.add(7)
    myHeap.add(23)
    myHeap.add(25)
    myHeap.add(47)
    myHeap.removeMax()
    print(myHeap)
    print(myHeap.find(47))
    print(myHeap.find(4))


if __name__ == "__main__":
    main()
    # print(subsetsRecursive([1,2,3,4]))
    