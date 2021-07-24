
def findKLargest(lst, k):
    # Write your code here
    for i in range(len(lst)//2,-1,-1):
        minHeap = maxHeapify(lst,i)
    larger = []
    for i in range(k):
        larger.append(minHeap[0])
        removeMin(minHeap)
    return larger

def removeMin(heap):
    if len(heap)>1:
        max = heap[0]
        heap[0] = heap[-1]
        del heap[-1]
        maxHeapify(heap,0)
        return max
    elif len(heap) == 1:
        max = heap[0]
        del heap[0]
        return max
    else:
        return None

def maxHeapify(heap,index):
    left = index * 2 + 1
    right = index * 2 + 2
    largest = index

    if len(heap)>left and heap[largest]<heap[left]:
        largest = left

    if len(heap)>right and heap[largest]<heap[right]:
        largest = right

    if largest != index:
        heap[largest], heap[index] = heap[index], heap[largest]
        maxHeapify(heap, largest)
    return heap


print(findKLargest([9, 4, 7, 1, -2, 6, 5],2))