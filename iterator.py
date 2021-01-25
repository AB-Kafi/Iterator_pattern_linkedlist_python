class Node:

    def __init__(self, data = None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class iterator:

    def __init__(self, headNode):
        self.__current = headNode

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current.next == None:
            raise StopIteration
        self.__current = self.__current.next
        return self.__current


class LinkedList:
    Head = Node()
    Tail = Node()
    counter = 1

    def __init__(self):

       temp = Node(input("Enter a Name : "))
       LinkedList.Head.next = temp
       LinkedList.Tail = temp
    
    def addNode(self):
        temp = Node(input("Enter Next data: "))
        LinkedList.Tail.next = temp
        LinkedList.Tail = temp
        LinkedList.counter += 1

    def __iter__(self):
        return iterator(LinkedList.Head)

if __name__ == "__main__":

    ll = LinkedList()
    ll.addNode()
    ll.addNode()
    print(ll.counter)
    for i in ll:
        print(i)

