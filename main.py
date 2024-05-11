import linked_list
import bst

def main():
    '''Linked List'''
    my_list = linked_list.LinkedList()

    my_list.add(47)
    my_list.add(3)
    my_list.add(2003)
    my_list.add(4703)
    my_list.add(4747)

    # Checking if a specific element is in the list
    print(my_list.find(472003))
    print(my_list.find(47))

    '''myBST'''
    # Create an instance of BinarySearchTree
    myBST = bst.BinarySearchTree()

    # Add nodes to the myBST
    myBST.add(50)
    myBST.add(30)
    myBST.add(70)
    myBST.add(20)
    myBST.add(40)
    myBST.add(60)
    myBST.add(80)


    # Try finding a value
    x = 60
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

if __name__ == "__main__":
    main()