class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def find_middle_node(self):
        fast=self.head
        slow=self.head
        while True:
            slow=slow.next
            #print("Value and next of slow ", slow.value, slow.next.value)
            fast=fast.next.next
           #print("Value and next of fast ", fast.value, fast.next)
            if fast.next is None or fast is None:
                #print("breaking on ", slow.value, fast.value)
                
                break
            
        return slow
                    
            



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""