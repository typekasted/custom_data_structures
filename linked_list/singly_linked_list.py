# Node class
unique_id_list = []

class Node:
    def __init__(self, element, unique_id) -> None:
        self.element = element
        self.next = None
        if unique_id not in unique_id_list:
            self.unique_id = unique_id
            unique_id_list.append(self.unique_id)
        else:
            raise ValueError(f"Unique Id \'{unique_id}\' already exists. Error while inserting (element : \'{self.element}\', unique_id: \'{unique_id}\')")

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_front(self, new_element, unique_id):
        """Add a node at the front"""
        # create a node
        new_node = Node(new_element, unique_id)
        # attach next to current head
        new_node.next = self.head
        # change the head to point to new node
        self.head = new_node

    def is_node_present(self, unique_id):
        "linear search"
        temp = self.head
        while temp:
            if temp.unique_id == unique_id:
                return True
            temp = temp.next
        return False
    
    def insert_after(self, search_unique_id, new_element, unique_id):
        # search for previous node
        if self.is_node_present(search_unique_id): 
            # if prev_node is present, find the node from unique_id
            temp = self.head
            while temp.unique_id != search_unique_id:
                temp = temp.next
            # pushing the new node after previous node
            new_node = Node(new_element, unique_id)
            new_node.next = temp.next
            temp.next = new_node
        else:
            raise ValueError(f"The prev_node provided does not exist.")

    def print_elements(self):
        temp = self.head
        count = 0
        print(f"Head: {temp}")
        while temp:
            count += 1
            print(f"(node_count: {count}, node_id: {hex(id(temp))}, element: {temp.element}, next: {temp.next}, unique_id: {temp.unique_id})")
            temp = temp.next
        print("-----------------------")

    def size(self):
        temp = self.head # Initialise temp
        count = 0 # Initialise count
        # Loop while end of linked list is not reached
        while (temp):
            count += 1
            temp = temp.next
        return count

if __name__ == "__main__":

    obj1 = SinglyLinkedList()

    print(f"Initial size: {obj1.size()}")
    obj1.print_elements()

    obj1.insert_front(10, "anish1@gmail.com")
    print(f"Size after inserting: {obj1.size()}")
    obj1.print_elements()

    obj1.insert_front(20, "anish2@gmail.com")
    print(f"Size: {obj1.size()}")
    obj1.print_elements()

    # Will throw error
    # obj1.insert_after("anish3@gmail.com", 15, "anish2@gmail.com")
    
    # obj1.print_elements()

    obj1.insert_after("anish2@gmail.com", 15, "anish3@gmail.com")
    print(f"Size: {obj1.size()}")
    obj1.print_elements()

# OUTPUT:

# anish@Anish ~ % /opt/homebrew/opt/python@3.10/bin/python3 /Users/anish/Desktop/data_science/data_struct/custom_data_structures/linked_list/singly_
# linked_list.py
# Initial size: 0
# Head: None
# -----------------------
# Size after inserting: 1
# Head: <__main__.Node object at 0x1031b7df0>
# (node_count: 1, node_id: 0x1031b7df0, element: 10, next: None, unique_id: anish1@gmail.com)
# -----------------------
# Size: 2
# Head: <__main__.Node object at 0x1031b7d90>
# (node_count: 1, node_id: 0x1031b7d90, element: 20, next: <__main__.Node object at 0x1031b7df0>, unique_id: anish2@gmail.com)
# (node_count: 2, node_id: 0x1031b7df0, element: 10, next: None, unique_id: anish1@gmail.com)
# -----------------------
# Size: 3
# Head: <__main__.Node object at 0x1031b7d90>
# (node_count: 1, node_id: 0x1031b7d90, element: 20, next: <__main__.Node object at 0x1031b7d30>, unique_id: anish2@gmail.com)
# (node_count: 2, node_id: 0x1031b7d30, element: 15, next: <__main__.Node object at 0x1031b7df0>, unique_id: anish3@gmail.com)
# (node_count: 3, node_id: 0x1031b7df0, element: 10, next: None, unique_id: anish1@gmail.com)
# -----------------------