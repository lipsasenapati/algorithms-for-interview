def findKSmallest(lst, k):
    # Write your code here
    for i in range(len(lst)//2,-1,-1):
        minHeap = minHeapify(lst,i)
    smaller = []
    for i in range(k):
        smaller.append(minHeap[0])
        removeMin(minHeap)
    return smaller

def removeMin(heap):
    if len(heap)>1:
        min = heap[0]
        heap[0] = heap[-1]
        del heap[-1]
        minHeapify(heap,0)
        return min
    elif len(heap) == 1:
        min = heap[0]
        del heap[0]
        return min
    else:
        return None

def minHeapify(heap,index):
    left = index * 2 + 1
    right = index * 2 + 2
    smallest = index

    if len(heap)>left and heap[smallest]>heap[left]:
        smallest = left

    if len(heap)>right and heap[smallest]>heap[right]:
        smallest = right

    if smallest != index:
        heap[smallest], heap[index] = heap[index], heap[smallest]
        minHeapify(heap, smallest)
    return heap

print(findKSmallest([9, 4, 7, 1, -2, 6, 5],2))