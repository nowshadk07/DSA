class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self,value) :
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def print_list(self):
        print("Printing the list with length", self.length)
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next   

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:    
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node   
        self.length+=1
        return True
    
    def pop(self):
        
        if self.length==0:
            return None
        temp = self.tail
        if self.length==1:
            self.head =None
            self.tail=None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length-=1
        return temp    

    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node 
        else:
            new_node.next=self.head
            self.prev=new_node
            self.head=new_node

        self.length+=1 
        return True   
            







my_doubly_linked_list=DoublyLinkedList(12)
#my_doubly_linked_list.print_list()
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(34)
my_doubly_linked_list.print_list()

print("Testing POP")
print(my_doubly_linked_list.pop())
my_doubly_linked_list.print_list()

print("Testing prepend")
my_doubly_linked_list.prepend(4)
my_doubly_linked_list.print_list()
                                       
                                       

