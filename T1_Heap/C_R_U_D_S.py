########################################
#         HEAP - C.R.U.D.S             #
#    (Min Heap & Max Heap dono)        #
########################################

# Heap kya hai?
# -> Complete Binary Tree hai jisme:
#    Min Heap: parent CHOTA hota hai children se
#    Max Heap: parent BADA hota hai children se
#
# Array representation:
#    parent index = (i - 1) // 2
#    left child   = 2 * i + 1
#    right child  = 2 * i + 2


# ============================================
#   METHOD 1: MANUAL IMPLEMENTATION (scratch)
#   -- yeh samajhna zaroori hai internals ke liye
# ============================================

class MinHeap:

  def __init__(self):
    self.heap = []
    self.n = 0       # size track karne ke liye (like LinkedList)

  def __len__(self):
    return self.n

  # ---------- HELPER FUNCTIONS ----------

  def _parent(self, i):
    return (i - 1) // 2

  def _left(self, i):
    return 2 * i + 1

  def _right(self, i):
    return 2 * i + 2

  def _swap(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

  # Heapify UP -> naya element neeche se upar jaata hai (insert ke baad)
  def _heapify_up(self, i):
    while i > 0 and self.heap[i] < self.heap[self._parent(i)]:
      self._swap(i, self._parent(i))
      i = self._parent(i)

  # Heapify DOWN -> root se neeche jaata hai (delete ke baad)
  def _heapify_down(self, i):
    smallest = i
    left = self._left(i)
    right = self._right(i)

    if left < self.n and self.heap[left] < self.heap[smallest]:
      smallest = left

    if right < self.n and self.heap[right] < self.heap[smallest]:
      smallest = right

    if smallest != i:
      self._swap(i, smallest)
      self._heapify_down(smallest)   # recursion


  #### CREATE / INSERT
  # O(log n)
  def insert(self, value):
    self.heap.append(value)
    self.n += 1
    self._heapify_up(self.n - 1)     # naya element last me add hua, usko sahi jagah le jao

  #### READ / PEEK
  # O(1) -> root element (min element) dekho bina nikale
  def peek(self):
    if self.n == 0:
      return 'Heap is empty'
    return self.heap[0]

  #### DELETE (extract min -- root ko nikalo)
  # O(log n)
  def extract_min(self):
    if self.n == 0:
      return 'Heap is empty'

    if self.n == 1:
      self.n -= 1
      return self.heap.pop()

    root = self.heap[0]
    # last element ko root pe daalo, phir heapify down
    self.heap[0] = self.heap.pop()
    self.n -= 1
    self._heapify_down(0)
    return root

  #### DELETE arbitrary value
  # O(n) search + O(log n) heapify
  def remove(self, target):
    # pehle dhundho
    idx = -1
    for i in range(self.n):
      if self.heap[i] == target:
        idx = i
        break

    if idx == -1:
      return f'{target} not found'

    # last element se replace karo
    self.heap[idx] = self.heap[-1]
    self.heap.pop()
    self.n -= 1

    # agar kuch bacha hai toh fix karo
    if idx < self.n:
      self._heapify_down(idx)
      self._heapify_up(idx)

  #### UPDATE (kisi value ko change karo)
  # O(n) search + O(log n) heapify
  def update(self, old_val, new_val):
    idx = -1
    for i in range(self.n):
      if self.heap[i] == old_val:
        idx = i
        break

    if idx == -1:
      return f'{old_val} not found'

    self.heap[idx] = new_val

    # Dono direction me fix karo
    # agar new_val chota hua -> upar jaayega
    # agar new_val bada hua  -> neeche jaayega
    self._heapify_up(idx)
    self._heapify_down(idx)

  #### SEARCH (heap me element hai ya nahi)
  # O(n) -> heap me binary search nahi chalta!
  def search(self, target):
    for i in range(self.n):
      if self.heap[i] == target:
        return i      # index return
    return -1         # nahi mila

  #### TRAVERSE (print the heap array)
  def traverse(self):
    print(self.heap)

  #### BUILD HEAP from a list
  # O(n) -> har non-leaf node pe heapify down
  def build_heap(self, arr):
    self.heap = arr[:]         # copy banao
    self.n = len(arr)

    # last non-leaf node se start karo (bottom-up)
    for i in range(self.n // 2 - 1, -1, -1):
      self._heapify_down(i)

  #### CLEAR
  def clear(self):
    self.heap = []
    self.n = 0

  #### SIZE CHECK
  def is_empty(self):
    return self.n == 0



# ============================================
#   METHOD 2: PYTHON heapq MODULE (shortcut)
#   -- LeetCode me yeh use karoge mostly
# ============================================

import heapq

class HeapqDemo:

  # ---------- MIN HEAP (default in Python) ----------

  @staticmethod
  def min_heap_demo():
    print("=== MIN HEAP (heapq) ===")

    heap = []

    # INSERT -> heapq.heappush()
    heapq.heappush(heap, 40)
    heapq.heappush(heap, 10)
    heapq.heappush(heap, 30)
    heapq.heappush(heap, 20)
    print("After inserts:", heap)        # [10, 20, 30, 40]

    # PEEK -> heap[0]  (smallest element)
    print("Peek (min):", heap[0])        # 10

    # DELETE MIN -> heapq.heappop()
    smallest = heapq.heappop(heap)
    print("Popped:", smallest)           # 10
    print("After pop:", heap)            # [20, 40, 30]

    # BUILD HEAP from list -> heapq.heapify()
    arr = [5, 3, 8, 1, 2]
    heapq.heapify(arr)
    print("Heapified:", arr)             # [1, 2, 8, 5, 3]

    # PUSH + POP in one step (efficient) -> heapq.heappushpop()
    result = heapq.heappushpop(arr, 4)   # push 4, then pop smallest
    print("Pushpop result:", result)     # 1
    print("After pushpop:", arr)

    # REPLACE (pop first, then push) -> heapq.heapreplace()
    result = heapq.heapreplace(arr, 0)   # pop smallest, then push 0
    print("Replace result:", result)
    print("After replace:", arr)

    # N SMALLEST / N LARGEST
    data = [10, 3, 7, 1, 9, 5, 2]
    print("3 smallest:", heapq.nsmallest(3, data))  # [1, 2, 3]
    print("3 largest:", heapq.nlargest(3, data))    # [10, 9, 7]

    print()

  # ---------- MAX HEAP (trick: negate values!) ----------
  # Python me Max Heap nahi hai directly,
  # toh -1 se multiply karo push/pop ke time

  @staticmethod
  def max_heap_demo():
    print("=== MAX HEAP (negate trick) ===")

    max_heap = []

    # INSERT -> push with negation
    heapq.heappush(max_heap, -40)
    heapq.heappush(max_heap, -10)
    heapq.heappush(max_heap, -30)
    heapq.heappush(max_heap, -20)
    print("Internal:", max_heap)                        # [-40, -20, -30, -10]

    # PEEK -> negate back
    print("Peek (max):", -max_heap[0])                  # 40

    # POP -> negate back
    largest = -heapq.heappop(max_heap)
    print("Popped (max):", largest)                      # 40
    print("After pop:", [-x for x in max_heap])          # [30, 20, 10]

    print()



# ============================================
#          DEMO / TESTING SECTION
#   (LinkedList jaisa bottom me run karenge)
# ============================================

if __name__ == '__main__':

  print("="*50)
  print("  MANUAL MIN HEAP DEMO")
  print("="*50)

  h = MinHeap()

  # INSERT
  h.insert(40)
  h.insert(10)
  h.insert(30)
  h.insert(20)
  h.insert(5)

  print("After inserts:")
  h.traverse()               # [5, 10, 30, 40, 20]

  # PEEK
  print("Peek (min):", h.peek())    # 5

  # SEARCH
  print("Search 30:", h.search(30))   # index milega
  print("Search 99:", h.search(99))   # -1

  # EXTRACT MIN
  print("Extract min:", h.extract_min())  # 5
  h.traverse()

  # UPDATE
  h.update(40, 2)     # 40 ko 2 bana do
  print("After update 40->2:")
  h.traverse()

  # REMOVE
  h.remove(30)
  print("After removing 30:")
  h.traverse()

  # BUILD HEAP
  h2 = MinHeap()
  h2.build_heap([9, 4, 7, 1, 3, 6])
  print("\nBuild heap from [9,4,7,1,3,6]:")
  h2.traverse()

  # SIZE & CLEAR
  print("Size:", len(h2))
  h2.clear()
  print("After clear, empty?:", h2.is_empty())


  print("\n" + "="*50)
  print("  PYTHON heapq MODULE DEMO")
  print("="*50)

  HeapqDemo.min_heap_demo()
  HeapqDemo.max_heap_demo()


  print("\n" + "="*50)
  print("  QUICK CHEATSHEET")
  print("="*50)
  print("""
  heapq FUNCTIONS:
  +------------------------------+------------+
  | Operation                    | Time       |
  +------------------------------+------------+
  | heapq.heappush(heap, val)    | O(log n)   |
  | heapq.heappop(heap)          | O(log n)   |
  | heap[0]  (peek)              | O(1)       |
  | heapq.heapify(list)          | O(n)       |
  | heapq.heappushpop(heap, val) | O(log n)   |
  | heapq.heapreplace(heap, val) | O(log n)   |
  | heapq.nsmallest(k, iterable) | O(n log k) |
  | heapq.nlargest(k, iterable)  | O(n log k) |
  +------------------------------+------------+

  MAX HEAP TRICK:
    push: heapq.heappush(heap, -val)
    pop:  -heapq.heappop(heap)
    peek: -heap[0]
  """)
