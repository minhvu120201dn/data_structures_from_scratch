import linked_list
import bst
import heap
import avl

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
    # myHeap.removeMax()
    print(myHeap)
    print(myHeap.find(47))
    print(myHeap.find(4))

    '''AVL'''
 # Create an instance of the AVL tree
    avl_tree = avl.AVLTree()

    # Insert elements into the AVL tree
    elements_to_add = [10, 20, 5, 4, 15, 25]
    print("Inserting elements:")
    for elem in elements_to_add:
        avl_tree.add(elem)
        print(f"Added {elem}, current length: {len(avl_tree)}")

    # Print the tree height
    print(f"Tree height after insertions: {avl_tree.getHeight(avl_tree.root)}")

    # Check if elements exist in the tree
    print("Checking existence of elements:")
    elements_to_find = [10, 5, 30]
    for elem in elements_to_find:
        found = avl_tree.find(elem)
        print(f"Element {elem} found: {found}")

    # Find the maximum value in the tree
    max_value = avl_tree.findMax()
    print(f"Maximum value in the tree: {max_value}")

    # Remove an element from the tree
    element_to_remove = 20
    removed = avl_tree.remove(element_to_remove)
    print(f"Removed {element_to_remove}: {removed}")

    # Print the tree height after removal
    print(f"Tree height after removal of {element_to_remove}: {avl_tree.getHeight(avl_tree.root)}")

    # Check the length of the tree after removal
    print(f"Current length of the tree: {len(avl_tree)}")

    # Check if the removed element still exists in the tree
    found = avl_tree.find(element_to_remove)
    print(f"Element {element_to_remove} found after removal: {found}")

if __name__ == "__main__":
    main()
    # print(subsetsRecursive([1,2,3,4]))
    