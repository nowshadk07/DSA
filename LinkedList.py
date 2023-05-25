class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next        

            

my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)
my_linked_list.print_list()
my_linked_list.append(2)
print("The list is now updated.")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""

                                                                                                                    