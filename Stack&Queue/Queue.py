class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1

    def print_queue(self):
        print("Printing queue with length ",self.length)
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def enqueue(self,value):
        new_node=Node(value)
        if self.length==0:  #if self.first is None
            self.first=new_node
            self.last=new_node
        else:    
            self.last.next=new_node
            self.last = new_node
        self.length+=1



my_queue = Queue(4)
my_queue.print_queue()

print("Testing enqueue")
my_queue.enqueue(3)
my_queue.print_queue()
