import heapq

class Solution:
    def kthSmallest(self, arr, k):
        n = len(arr)
        
        max_heap = []

        for i in range(k):
            heapq.heappush(max_heap, -arr[i])
            
        for i in range(k,n):
            if arr[i] >= -max_heap[0]:   # max_heap.top()
                continue
            else:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, -arr[i])
                
        top = -max_heap[0]
        return top