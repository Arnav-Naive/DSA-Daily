class Node:
  def __init__(self, value):
    self.data = value
    self.next = None


class Stack:
  def __init__(self):
    self.top = None


  def isempty(self):
    return self.top == None

  # PUSH
  def push(self, target):
    new_node = Node(target)

    new_node.next = self.top
    self.top = new_node 

  
  # PEEK
  def peek(self):
    if self.isempty():
      return "Stack Empty"
    else:
      return self.top.data

  # POP
  def pop(self):
    if self.isempty():
      return "Stack Empty"
    else:
      temp_data = self.top.data  # Value save karo
      self.top = self.top.next   # Node delete karo
      return temp_data           # Value return karo

  # Traverse
  def traverse(self):
    temp = self.top

    while temp != None:
      print(temp.data)
      temp = temp.next

  # len (No necessaryly mantatory)
  def __len__(self):      # just use --> len(s)
    curr = self.top
    count = 0
    while curr != None:
      count += 1
      curr = curr.next
    return count





s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Top element is:", s.peek())

print("Popped element is:", s.pop())

print("Top element is:", s.peek())

print("Length of stack:", len(s))

print("Stack elements:")
s.traverse()
    