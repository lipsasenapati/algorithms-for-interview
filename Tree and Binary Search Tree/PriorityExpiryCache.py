import heapq   #Used for priority queue implementation
import gc   #Used for garbage collection

#Implementation for Item
class Item:
    def __init__(self, key, value, priority, expiryTime):
        self.key = key
        self.value = value
        self.precedence = priority
        self.expiry_time = expiryTime

    def __lt__(self, other):
        return self.expiry_time < other.expiry_time

#Implementation for ListNode
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __lt__(self, other):
        return self.data < other.data


#Implementation of the Doubly Linked List data structure
class DoublyLinkedList:
    def __init__(self):
        self.front = None
        self.end = None
        self.size = 0

    #Add an item to the head of the doubly linked list
    def addFront(self, x):
        if self.size == 0:
            self.front = ListNode(x)
            self.end = self.front
            retVal = self.front
        else:
            newNode = ListNode(x)
            newNode.next = self.front
            self.front.prev = newNode
            self.front = newNode
            retVal = newNode
        self.size += 1
        return retVal

    #Remove an item from the tail of the doubly linked list
    def removeLast(self):
        item = self.end
        self.end = self.end.prev
        self.size -= 1
        return item

    #Remove a specified node from the doubly linked list
    def removeNode(self, node):
        if self.size == 0:
            return

        if self.size == 1:
            self.end = self.front = None
        else:
            prev = node.prev
            next = node.next

            if prev is not None:
                prev.next = next

            if next is not None:
                next.prev = prev

        self.size -= 1
        gc.collect()


#Implementation of the Priority Expiry Cache using a hash table and a doubly linked list
class PriorityExpiryCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.currSize = 0
        self.expiryTimePQ = list()  #takes O(lg (n)) for removing min item from min heap + O(1)) for removing from hash table
        self.precedencePQ = list()  
        self.precedenceToList = {}
        self.keyToItemNode = {}

    def getKeys(self):
        return self.keyToItemNode.keys()

    # evictItem method takes O(lg(n)) for removing from precedence min heap, 
    # O(lg(n)) for removing from expired item
    # O(1) for deleting from hashtable of key to mapped items, and
    # O(1) for removing from doubly linked list 
    def evictItem(self, currentTime):
        if self.currSize == 0:
            return

        self.currSize -= 1
        if self.expiryTimePQ[0].data.expiry_time < currentTime:
            node = heapq.heappop(self.expiryTimePQ)
            item = node.data
            itemList = self.precedenceToList.get(item.precedence)
            itemList.removeNode(node)
            if itemList.size == 0:
                del self.precedenceToList[item.precedence]
            del self.keyToItemNode[item.key]
            self.precedencePQ = list(filter(lambda i: i.data.precedence != item.precedence, self.precedencePQ))
            return

        preference = heapq.heappop(self.precedencePQ).data.precedence

        itemList = self.precedenceToList.get(preference)
        leastPrecedenceLRU = itemList.removeLast()
        del self.keyToItemNode[leastPrecedenceLRU.data.key]
        if leastPrecedenceLRU in self.expiryTimePQ:
            self.expiryTimePQ.remove(leastPrecedenceLRU)

        if itemList.size == 0:
            del self.precedenceToList[preference]

    # get method takes O(1) time complexity
    def get(self, key):
        if key in self.keyToItemNode:
            node = self.keyToItemNode.get(key)
            itemToReturn = node.data
            itemList = self.precedenceToList.get(itemToReturn.precedence)
            itemList.removeNode(node)
            itemList.addFront(itemToReturn)
            return itemToReturn

    # set method takes an overall time complexity of O(lg(n)) where
    # O(lg(n)) is for adding new elements to two min heaps and
    # O(1) for inserting into the key to item hashtable
    def set(self, item, currentTime=0):
        if self.currSize == self.maxSize:
            self.evictItem(currentTime)

        itemList = None
        if item.precedence in self.precedenceToList:
            itemList = self.precedenceToList.get(item.precedence)
        else:
            itemList = DoublyLinkedList()
            self.precedenceToList[item.precedence] = itemList

        node = itemList.addFront(item)
        self.keyToItemNode[item.key] = node
        self.expiryTimePQ.append(node)
        heapq.heapify(self.expiryTimePQ)
        self.precedencePQ.append(node)
        heapq.heapify(self.precedencePQ)
        self.currSize += 1


#Executing PriorityExpiryCache
priorityExp = PriorityExpiryCache(5)
priorityExp.set(Item("A", "1", 5, 100))
priorityExp.set(Item("B", "2", 15, 3))
priorityExp.set(Item("C", "3", 5, 10))
priorityExp.set(Item("D", "4", 1, 15))
priorityExp.set(Item("E", "5", 5, 150))

priorityExp.get("C")
print(priorityExp.getKeys())
print("space for 5 keys, all 5 items are included. \n\n")

# Current time = 0
priorityExp.evictItem(5)
print(priorityExp.getKeys())
print("\"B\" is removed because it is expired.  e3 < e5 \n\n")
# time.sleep(5)

# Current time = 5
priorityExp.evictItem(5)
print(priorityExp.getKeys())
print("\"D\" is removed because it the lowest priority. \n D's expire time is irrelevant.\n\n")

priorityExp.evictItem(5)
print(priorityExp.getKeys())
print("\"A\" is removed because it is least recently used. \n A's expire time is irrelevant.\n\n")

priorityExp.evictItem(5)
print(priorityExp.getKeys())
print("\"E\" is removed because C is more recently used (due to the Get(\"C\") event).\n\n")


# 
# Your previous Go content is preserved below:
# 
# package cache
# 
# import (
#   "time"
# )
# 
# /*
# You can use any language.
# 
# Your task is to implement a PriorityExpiryCache cache with a max capacity.  Specifically please fill out the data structures on the PriorityExpiryCache object and implement the entry eviction method.
# 
# 
# It should support these operations:
#   Get: Get the value of the key if the key exists in the cache and is not expired.
#   Set: Update or insert the value of the key with a priority value and expiretime.
#     Set should never ever allow more items than maxItems to be in the cache.
#     When evicting we need to evict the lowest priority item(s) which are least recently used.
# 
# Example:
# p5 => priority 5
# e10 => expires at 10 seconds since epoch
# 
# c = NewCache(5)
# c.Set("A", value=1, priority=5,  expireTime=100)
# c.Set("B", value=2, priority=15, expireTime=3)
# c.Set("C", value=3, priority=5,  expireTime=10)
# c.Set("D", value=4, priority=1,  expireTime=15)
# c.Set("E", value=5, priority=5,  expireTime=150)
# c.Get("C")
# 
# 
# // Current time = 0
# c.SetMaxItems(5)
# c.Keys() = ["A", "B", "C", "D", "E"]
# // space for 5 keys, all 5 items are included
# 
# time.Sleep(5)
# 
# // Current time = 5
# c.SetMaxItems(4)
# c.Keys() = ["A", "C", "D", "E"]
# // "B" is removed because it is expired.  e3 < e5
# 
# c.SetMaxItems(3)
# c.Keys() = ["A", "C", "E"]
# // "D" is removed because it the lowest priority
# // D's expire time is irrelevant.
# 
# c.SetMaxItems(2)
# c.Keys() = ["C", "E"]
# // "A" is removed because it is least recently used."
# // A's expire time is irrelevant.
# 
# c.SetMaxItems(1)
# c.Keys() = ["C"]
# // "E" is removed because C is more recently used (due to the Get("C") event).
# 
# */
# 
# type PriorityExpiryCache struct {
#   maxItems int
#   // TODO(interviewee): implement this
# }
# 
# func NewCache(maxItems int) *PriorityExpiryCache {
#   return &PriorityExpiryCache{
#     maxItems: maxItems,
#   }
# }
# 
# func (c *PriorityExpiryCache) Get(key string) interface{} {
#   
# 
#   return nil
# }
# 
# func (c *PriorityExpiryCache) Set(key string, value interface{}, priority int, expire time.Time) {
#   
# 
#   c.evictItems()
# }
# 
# func (c *PriorityExpiryCache) SetMaxItems(maxItems int) {
#   c.maxItems = maxItems
# 
#   c.evictItems()
# }
# 
# // evictItems will evict items from the cache to make room for new ones.
# func (c *PriorityExpiryCache) evictItems() {
#   // TODO(interviewee): implement this
# }
