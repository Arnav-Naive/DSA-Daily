class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # ==========================================
    #                  # LOGIC 
    # ==========================================

    # Enqueue -> Add node to the tail/rear
    def enqueue(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
  
    # Dequeue -> Delete node from the front/head
    def dequeue(self):
        if self.is_empty():
            return "Empty"
        else:
            res = self.front.data       # Save data to return later
            self.front = self.front.next  # Move front pointer forward
            
            if self.front == None:      # If queue becomes empty, reset rear too
                self.rear = None
                
            return res                  # Return the deleted data

    # ==========================================
    #               UTILITY METHODS
    # ==========================================

    def is_empty(self):
        return self.front == None
  
    def front_item(self):
        if self.is_empty():
            return "Empty"
        return self.front.data

    def rear_item(self):
        if self.is_empty():
            return "Empty"
        return self.rear.data
  
    def size(self):
        temp = self.front
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        return count

    def traverse(self):
        temp = self.front
        while temp != None:
            print(temp.data, end=" ") 
            temp = temp.next
        print()