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
            self.head.prev=new_node
            self.head=new_node

        self.length+=1 
        return True 


    #This code is from the course. 
    # def pop_first(self):
    #     if self.length==0:
    #         return None
    #     temp=self.head
    #     if self.length==1:
    #         self.head=None
    #         self.tail=None
    #     else:
    #         self.head=self.head.next
    #         self.head.prev=None
    #         temp.next = None
    #     self.length-=1
    #     return temp            
    
    def pop_first(self):
        
        if self.length==0:
            return None
        elif self.length==1:
            temp=self.head
            self.head=None
            self.tail=None
            self.length-=1
            return temp
        else:
            temp=self.head
            self.head=self.head.next
            self.head.prev=None
            temp.next=None
            self.length-=1
            return temp


    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            temp=temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp=temp.prev

        return temp           








my_doubly_linked_list=DoublyLinkedList(12)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(6)
my_doubly_linked_list.append(5)
my_doubly_linked_list.append(54)
my_doubly_linked_list.print_list()

print("Testing POP")
print(my_doubly_linked_list.pop())
my_doubly_linked_list.print_list()

print("Testing prepend")
my_doubly_linked_list.prepend(4)
my_doubly_linked_list.print_list()


print("testing pop first")
print(my_doubly_linked_list.pop_first().value)
my_doubly_linked_list.print_list()

print("testing get")
print(my_doubly_linked_list.get(3))
                                       
                                       

