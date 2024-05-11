import linked_list

def main():
    my_list = linked_list.LinkedList()

    my_list.add(47)
    my_list.add(3)
    my_list.add(2003)
    my_list.add(4703)
    my_list.add(4747)

    # Checking if a specific element is in the list
    print(my_list.find(472003))
    print(my_list.find(47))

    # Removing an element from the list
    if my_list.remove(30):
        print("30 removed from the list.")
    else:
        print("30 was not found in the list.")

    # Checking if the element still exists after removal
    print("Is 30 in the list after removal?", my_list.find(30))

    # Finding the maximum value in the list
    print("The maximum value in the list is:", my_list.findMax())

    # Printing the current length of the list after removal
    print("Current length of the list:", len(my_list))

    # Adding more elements to the list
    my_list.add(60)
    my_list.add(70)

    # Finding the new maximum value in the list
    print("New maximum value in the list:", my_list.findMax())

    # Printing the current length of the list after adding more elements
    print("Updated length of the list:", len(my_list))


if __name__ == "__main__":
    main()