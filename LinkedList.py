class Node:
    def __init__(self , data ):
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = None
    def append(self , data):
        new_node = Node(data)
        temp = self.head
        if(self.head == None):
            self.head = new_node
        else:
            while(temp is not None):
                temp = temp.next 
            temp.next = new_node
    def printll(self):
        temp = self.head
        while(temp is not None):
            print(temp.data , end = " ---> ")
            temp = temp.next
        print("None")


if __name__ == "__main__":
    l1 = LinkedList()
    l1.append(10)
    l1.printll()