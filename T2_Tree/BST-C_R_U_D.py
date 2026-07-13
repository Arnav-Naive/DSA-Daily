########################################
#       BST (Binary Search Tree)       #
#          C.R.U.D.S                   #
########################################

# BST kya hai?
# -> Ek Binary Tree jisme:
#    Left child  < Parent
#    Right child > Parent
#
# Har subtree bhi BST hota hai (recursive property)
#
# Visualization:
#         50
#        /  \
#      30    70
#     / \   / \
#   20  40 60  80
#
# Inorder traversal of BST -> SORTED order milta hai!
# 20 -> 30 -> 40 -> 50 -> 60 -> 70 -> 80


class Node:
  def __init__(self, value):   # value or data anything is fine
    self.value = value
    self.left = None
    self.right = None


class BST:

  # empty BST
  def __init__(self):
    self.root = None
    self.n = 0

  def __len__(self):
    return self.n

  def is_empty(self):
    return self.root is None


  # ============================================
  #              CREATE / INSERT
  # ============================================
  # O(h) -> h = height (best: log n, worst: n)
  #
  # Logic:
  #   Chhota hai -> left jao
  #   Bada hai   -> right jao
  #   Jagah khaali -> wahi daal do

  def insert(self, value):
    new_node = Node(value)

    # agar tree khaali hai -> root ban jaao
    if self.root is None:
      self.root = new_node
      self.n += 1
      return

    curr = self.root

    while curr:
      if value < curr.value:
        # left jao
        if curr.left is None:
          curr.left = new_node
          self.n += 1
          return
        curr = curr.left

      elif value > curr.value:
        # right jao
        if curr.right is None:
          curr.right = new_node
          self.n += 1
          return
        curr = curr.right

      else:
        # duplicate -> BST me normally duplicates nahi hote
        return 'Duplicate value'


  # INSERT (Recursive version) -> zyada clean hai
  def insert_recursive(self, value):
    self.root = self._insert_rec(self.root, value)

  def _insert_rec(self, node, value):
    if node is None:
      self.n += 1
      return Node(value)

    if value < node.value:
      node.left = self._insert_rec(node.left, value)
    elif value > node.value:
      node.right = self._insert_rec(node.right, value)
    # duplicate -> kuch mat karo

    return node


  # ============================================
  #             READ / SEARCH
  # ============================================
  # O(h) -> BST ka fayda: sorted hai toh binary search lagta hai

  # Search by value -> True/False
  def search(self, target):
    curr = self.root

    while curr:
      if target == curr.value:
        return True
      elif target < curr.value:
        curr = curr.left
      else:
        curr = curr.right

    return False   # nahi mila

  # PEEK -> min element (leftmost node)
  # O(h)
  def get_min(self):
    if self.root is None:
      return 'Tree is empty'

    curr = self.root
    while curr.left:
      curr = curr.left
    return curr.value

  # PEEK -> max element (rightmost node)
  # O(h)
  def get_max(self):
    if self.root is None:
      return 'Tree is empty'

    curr = self.root
    while curr.right:
      curr = curr.right
    return curr.value


  # ============================================
  #             TRAVERSALS (Tree ka traverse)
  # ============================================
  # Yeh 3 important hain -> Inorder, Preorder, Postorder
  # + Level Order (BFS)

  # INORDER -> Left, Root, Right
  # BST me inorder -> SORTED order! (yeh important hai)
  def inorder(self):
    result = []
    self._inorder(self.root, result)
    return result

  def _inorder(self, node, result):
    if node is None:
      return
    self._inorder(node.left, result)
    result.append(node.value)
    self._inorder(node.right, result)

  # PREORDER -> Root, Left, Right
  # (root pehle aata hai -> tree copy/serialize ke kaam aata hai)
  def preorder(self):
    result = []
    self._preorder(self.root, result)
    return result

  def _preorder(self, node, result):
    if node is None:
      return
    result.append(node.value)
    self._preorder(node.left, result)
    self._preorder(node.right, result)

  # POSTORDER -> Left, Right, Root
  # (root last me -> tree delete karne ke kaam aata hai)
  def postorder(self):
    result = []
    self._postorder(self.root, result)
    return result

  def _postorder(self, node, result):
    if node is None:
      return
    self._postorder(node.left, result)
    self._postorder(node.right, result)
    result.append(node.value)

  # LEVEL ORDER -> BFS using queue
  # Har level ek ek karke print hota hai
  def level_order(self):
    if self.root is None:
      return []

    from collections import deque

    result = []
    queue = deque()
    queue.append(self.root)

    while queue:
      node = queue.popleft()
      result.append(node.value)

      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)

    return result

  # TRAVERSE PRINT -> visualize the tree structure
  def traverse_print(self):
    self._print_tree(self.root, "", True)

  def _print_tree(self, node, indent, is_right):
    if node is None:
      return
    if is_right:
      print(indent + "+-- " + str(node.value))
      new_indent = indent + "    "
    else:
      print(indent + "+-- " + str(node.value))
      new_indent = indent + "|   "

    self._print_tree(node.right, new_indent, True)
    self._print_tree(node.left, new_indent, False)


  # ============================================
  #             UPDATE (value change karo)
  # ============================================
  # BST me direct update nahi hota (kyunki order bigad jaata hai)
  # Trick: purana delete karo, naya insert karo
  # O(h) delete + O(h) insert = O(h)

  def update(self, old_val, new_val):
    if not self.search(old_val):
      return f'{old_val} not found'

    self.delete(old_val)
    self.insert(new_val)


  # ============================================
  #             DELETE (sabse tricky!)
  # ============================================
  # 3 Cases hain:
  #
  # Case 1: LEAF node (no children)
  #         -> seedha delete kar do
  #
  # Case 2: EK child hai (left ya right)
  #         -> child ko parent se connect karo, node delete
  #
  # Case 3: DO children hain
  #         -> Inorder Successor dhundho (right subtree ka smallest)
  #         -> Uski value copy karo
  #         -> Phir successor ko delete karo (Case 1 ya 2 hoga)
  #
  # O(h)

  def delete(self, target):
    self.root = self._delete(self.root, target)

  def _delete(self, node, target):
    # Base case: nahi mila
    if node is None:
      return None

    # target dhundho
    if target < node.value:
      node.left = self._delete(node.left, target)
    elif target > node.value:
      node.right = self._delete(node.right, target)
    else:
      # MIL GAYA! Ab delete karo

      # Case 1 & 2: 0 ya 1 child
      if node.left is None:
        self.n -= 1
        return node.right         # right child ya None return
      elif node.right is None:
        self.n -= 1
        return node.left          # left child return

      # Case 3: 2 children
      # Inorder Successor = right subtree ka leftmost (smallest)
      successor = self._get_min_node(node.right)
      node.value = successor.value    # value copy karo
      # ab successor ko right subtree se delete karo
      node.right = self._delete(node.right, successor.value)

    return node

  # helper: right subtree ka sabse chhota node (for Case 3)
  def _get_min_node(self, node):
    curr = node
    while curr.left:
      curr = curr.left
    return curr

  # DELETE ALL -> pura tree saaf
  def clear(self):
    self.root = None
    self.n = 0


  # ============================================
  #           EXTRA USEFUL OPERATIONS
  # ============================================

  # HEIGHT of tree
  # O(n) -> saare nodes visit karne padte hain
  def height(self):
    return self._height(self.root)

  def _height(self, node):
    if node is None:
      return -1     # convention: empty tree height = -1
                     # agar 0 rakhna ho toh wo bhi chalega, bas consistent raho
    left_h = self._height(node.left)
    right_h = self._height(node.right)
    return 1 + max(left_h, right_h)

  # COUNT total nodes
  def count_nodes(self):
    return self._count(self.root)

  def _count(self, node):
    if node is None:
      return 0
    return 1 + self._count(node.left) + self._count(node.right)

  # Check if valid BST
  def is_valid_bst(self):
    return self._is_valid(self.root, float('-inf'), float('inf'))

  def _is_valid(self, node, min_val, max_val):
    if node is None:
      return True
    if node.value <= min_val or node.value >= max_val:
      return False
    return (self._is_valid(node.left, min_val, node.value) and
            self._is_valid(node.right, node.value, max_val))



# ============================================
#          DEMO / TESTING SECTION
#   (LinkedList jaisa bottom me run karenge)
# ============================================

if __name__ == '__main__':

  print("="*50)
  print("  BST CRUD DEMO")
  print("="*50)

  tree = BST()

  # ---- INSERT ----
  print("\n--- INSERT ---")
  tree.insert(50)
  tree.insert(30)
  tree.insert(70)
  tree.insert(20)
  tree.insert(40)
  tree.insert(60)
  tree.insert(80)

  print("Tree structure:")
  tree.traverse_print()
  #         50
  #        /  \
  #      30    70
  #     / \   / \
  #   20  40 60  80

  print("Size:", len(tree))                  # 7

  # ---- TRAVERSALS ----
  print("\n--- TRAVERSALS ---")
  print("Inorder  (sorted!):", tree.inorder())    # [20, 30, 40, 50, 60, 70, 80]
  print("Preorder (root 1st):", tree.preorder())  # [50, 30, 20, 40, 70, 60, 80]
  print("Postorder(root last):", tree.postorder())# [20, 40, 30, 60, 80, 70, 50]
  print("Level order (BFS):", tree.level_order()) # [50, 30, 70, 20, 40, 60, 80]

  # ---- SEARCH ----
  print("\n--- SEARCH ---")
  print("Search 40:", tree.search(40))    # True
  print("Search 99:", tree.search(99))    # False
  print("Min:", tree.get_min())           # 20
  print("Max:", tree.get_max())           # 80

  # ---- DELETE ----
  print("\n--- DELETE ---")

  # Case 1: Leaf node delete (20 -> no children)
  tree.delete(20)
  print("After deleting 20 (leaf):")
  print("Inorder:", tree.inorder())       # [30, 40, 50, 60, 70, 80]

  # Case 2: 1 child node delete (30 -> only right child 40)
  tree.delete(30)
  print("After deleting 30 (1 child):")
  print("Inorder:", tree.inorder())       # [40, 50, 60, 70, 80]

  # Case 3: 2 children node delete (70 -> left:60, right:80)
  tree.delete(70)
  print("After deleting 70 (2 children):")
  print("Inorder:", tree.inorder())       # [40, 50, 60, 80]

  print("\nTree after all deletions:")
  tree.traverse_print()

  # ---- UPDATE ----
  print("\n--- UPDATE ---")
  tree.update(60, 65)
  print("After update 60->65:")
  print("Inorder:", tree.inorder())       # [40, 50, 65, 80]

  # ---- EXTRAS ----
  print("\n--- EXTRA OPERATIONS ---")
  print("Height:", tree.height())
  print("Node count:", tree.count_nodes())
  print("Valid BST?:", tree.is_valid_bst())

  # ---- CLEAR ----
  print("\n--- CLEAR ---")
  tree.clear()
  print("After clear, empty?:", tree.is_empty())   # True
  print("Size:", len(tree))                         # 0


  # ============================================
  #        QUICK CHEATSHEET
  # ============================================
  print("\n" + "="*50)
  print("  BST QUICK CHEATSHEET")
  print("="*50)
  print("""
  BST OPERATIONS:
  +----------------------------+-------------------+
  | Operation                  | Time Complexity   |
  +----------------------------+-------------------+
  | Insert                     | O(h)  ~O(log n)   |
  | Search                     | O(h)  ~O(log n)   |
  | Delete                     | O(h)  ~O(log n)   |
  | Get Min / Get Max          | O(h)  ~O(log n)   |
  | Inorder / Pre / Post       | O(n)              |
  | Level Order (BFS)          | O(n)              |
  | Height                     | O(n)              |
  | Update (delete + insert)   | O(h)  ~O(log n)   |
  +----------------------------+-------------------+

  h = height of tree
  Best case:  h = log n  (balanced BST)
  Worst case: h = n      (skewed BST -> like a LinkedList!)

  3 DELETE CASES:
    Case 1: Leaf (no child)     -> seedha remove
    Case 2: 1 child             -> child connect to parent
    Case 3: 2 children          -> replace with inorder successor
                                   (right subtree ka smallest)

  TRAVERSAL TRICKS:
    Inorder  (L, Root, R) -> SORTED order nikalta hai!
    Preorder (Root, L, R) -> tree copy/serialize
    Postorder(L, R, Root) -> tree delete (bottom-up)
    Level Order           -> BFS, queue use karo

  BST vs LinkedList:
    LL search  = O(n)    |  BST search  = O(log n) *better*
    LL insert  = O(1)    |  BST insert  = O(log n)
    LL sorted? = NO      |  BST sorted? = YES (inorder)

  REMEMBER:
    Left < Root < Right   (yeh BST ki jaan hai!)
  """)
