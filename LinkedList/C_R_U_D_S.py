class Node:
  def __init__(self, value): # value or data anything is fine
    self.value = value
    self.next = None



class LinkedList:

  # emplty linkedlist
  def __init__(self):
    self.head = None
    self.n = 0

  def __len__(self):
    return self.n

  def insert_head(self, value):

    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node

    self.n += 1

  # Traverse
  def traverse(self):
    curr = self.head
    while curr != None:   # or while curr: ->also works
      print(curr.value)
      curr = curr.next

  # # Traverse (PRINT.. ->)
  def traversePrint(self):
    curr = self.head

    res = ''
    while curr != None:
      res += str(curr.value) + '->'
      curr = curr.next

    return res[:-2]

  ## Insert TAIL
  def append(self, value):

    tail = Node(value)

    # if lsit is empty
    if self.head == None:
      self.head = tail
      self.n += 1
      return

    curr = self.head
    while curr.next != None:
      curr = curr.next

    # u r at the last node
    curr.next = tail
    self.n += 1

  def insert_after(self, after, value):
    new_node = Node(value)

    curr = self.head

    while curr != None:
      if curr.value == after:
        break
      curr = curr.next

    if curr == None:
      return 'item No found'
    else:
      new_node.next = curr.next
      curr.next = new_node
      self.n += 1




  ### DELETION
  def clear(self):
    self.head = None
    self.n = 0
  # delete form head
  def delete_head(self):

    if self.head == None:
      return 'Empty LL--already'

    self.head = self.head.next
    self.n -= 1
  # delete from tail (pop)
  def pop(self):

    # no node? or empty alrdy
    if self.head == None:
      return 'Empty LL'

    # if there is only 1 node/item?
    curr = self.head
    if curr.next == None:
      self.delete_head()
      return

    curr = self.head
    while curr.next.next != None:
      curr = curr.next

    curr.next = None
    self.n -= 1
  ## remove in btw
  def remove(self, target):
    if self.head == None:
      return 'Empty LL'

    # Case 1: Agar pehla hi node target hai
    if self.head.value == target:
      self.delete_head()
      return

    # Case 2: Beech me dhoondna
    curr = self.head
    while curr.next != None:
      if curr.next.value == target:
        break
      curr = curr.next

    # 2 cases: (i) item ni mila, (ii) item mil gaya ,
    if curr.next == None:
      return f'{target} not found'
    else:
      curr.next= curr.next.next
      self.n -= 1






  #### SEARCHING
  #search by target/item (find)
  def search(self, target):

    curr = self.head
    pos = 0

    #find if exist... if do return index
    while curr != None:
      if curr.value == target:
        return pos
      curr = curr.next
      pos += 1

    # nahi mila
    return -1   # 'Not found'
  # search by index ulta ex: L[2] --> 2nd index me kya h?
  # __magic__ method use krege
  def __getitem__(self, idx):

    if idx < 0 or idx >= self.n:
      return 'IndexError'

    curr = self.head
    pos = 0

    while curr != None:
      if pos == idx:
        return curr.value
      curr = curr.next
      pos += 1

  # delete by index -> del L[idx]
  # Magic method taaki del L[3] kaam kare
  def __delitem__(self, idx):
    if idx < 0 or idx >= self.n:
      return 'IndexError'

    if idx == 0:
      self.delete_head()
      return

    curr = self.head
    pos = 0
    while pos < idx - 1:
      curr = curr.next
      pos += 1

    curr.next = curr.next.next
    self.n -= 1



L = LinkedList()


L.append(10)
L.append(20)
L.append(30)
L.append(40)


print(L.traversePrint())

# Delete node with value 20
L.remove(20)
print(L.traversePrint())