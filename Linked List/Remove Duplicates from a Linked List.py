# Remove Duplicates from Linked List using only one Linked List Node
# LinkedList = 1->2->2->2->3->4->4->5->6
# LinkedList = 1->2->3->4->5->6

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def getHead(self):
        return self.head
        
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
        
    def insertFront(self, data):
        temp = ListNode(data)
        if self.isEmpty():
            self.head = temp
            return self.head
        temp.next = self.head
        self.head = temp
        return self.head
        
    def printList(self):
        if self.isEmpty():
            print("List is empty!")
            return False
        temp = self.head
        while temp.next is not None:
            print(temp.data, end = " -> ")
            temp = temp.next
        print(temp.data, "-> None")
        return True
        
        
class Solution:
    def removeDuplicates(self) -> ListNode:
        curr = self.getHead()
        visitedNodes = set()
        if self.isEmpty():
            return curr
        if curr.next is None:
            return curr
        visitedNodes.add(curr.data)
        while curr:
            if curr.next and curr.next.data not in visitedNodes:
                visitedNodes.add(curr.next.data)
                curr = curr.next
            else:
                curr.next = curr.next.next

            print(visitedNodes)   
            linkedlist.printList()    
        
        
# Solution.removeDuplicates([1,2,2,2,3,4,4,5,6])
linkedlist = LinkedList()
linkedlist.insertFront(6)
linkedlist.insertFront(5)
linkedlist.insertFront(4)
linkedlist.insertFront(4)
linkedlist.insertFront(3)
linkedlist.insertFront(2)
linkedlist.insertFront(2) 
linkedlist.insertFront(2)
linkedlist.insertFront(1)

# linkedlist.printList()
Solution.removeDuplicates(linkedlist)
linkedlist.printList()
    
    