heap in pyhton synatx:

import heapq

# Create an empty list that will be treated as a min-heap
heap = []

# Push elements into the heap
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)

# The smallest element is always at index 0
print(heap[0])  # Output: 1

# Pop the smallest element
smallest = heapq.heappop(heap)
print(smallest)  # Output: 1

- in python the heap is **min** (by default). For max heap, negate values: push -val, pop -val