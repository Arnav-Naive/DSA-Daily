# 1. Initialize an empty stack
stack = []

# 2. PUSH: Add elements to the top of the stack (Time: O(1))
stack.append(10)
stack.append(20)
stack.append(30)

# 3. PEEK: Look at the top element without removing it (Time: O(1))
if stack:  # Always check if the stack is not empty first
    print("Top Element:", stack[-1])  # Output: 30

# 4. POP: Remove and return the top element (Time: O(1))
if stack:  # Always check if the stack is not empty first
    popped_val = stack.pop()
    print("Popped Element:", popped_val)  # Output: 30

# 5. IS_EMPTY: Check if the stack has no elements (Time: O(1))
if not stack:  # Or: if len(stack) == 0
    print("Stack is empty")