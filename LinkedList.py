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
        self.length+=1

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next  
    def pop(self):
        if self.length==0:
            return None
        else:
            temp=self.head
            pre=self.head
            while(temp.next):
                pre=temp
                temp = temp.next
            self.tail=pre
            self.tail.next=None
            print("Lenght of the list ", self.length)
            self.length-=1
            if self.length==0:
                self.head=None
                self.tail=None
            return temp.value
        #return temp
    def prepend(self,value):
        new_node=Node(value)
        if self.head==None: #self.length==0
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1    
        return True    #optional
    
    def pop_first(self):
        if self.length==0:
            return None
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            self.length-=1
            if self.length==0:
                self.tail=None
            return temp  #return temp.value for testing.

    def get(self,value):
        if value<=0 or value>=self.length:
            return None
        else:
            temp=self.head
            for _ in range(value):
                temp=temp.next
            return temp

    def set_value(self,index,value):
        #This is the code that I wrote
        # if index<=0 or index>=self.length:
        #     return None
        # else:
        #     temp=self.head
        #     for _ in range(index):
        #         temp=temp.next
        #     temp.value=value    
        # return temp.value  
        # Below is the code shown in the course
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
 

        



            

my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)
my_linked_list.append(5)
my_linked_list.append(4)
my_linked_list.append(7)
print("The list is now updated.")
#my_linked_list.print_list()
# print("First Sceario")
# print(my_linked_list.pop())
# print("Second Senario")
# print(my_linked_list.pop())
# print("third senario")
# print(my_linked_list.pop())
my_linked_list.print_list()

print("using get command")
print(my_linked_list.get(2))




print("using set_value command")

my_linked_list.set_value(2,54)

my_linked_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""

                                                                                                                    