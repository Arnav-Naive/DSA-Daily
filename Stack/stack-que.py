#_______________________________________________________________________________
# simple questions on Stack
from C_R_U_D import Stack


def reverse_string(text):

  s = Stack()

  for i in text:
    s.push(i)

  res = ""
  while ( not s.isempty() ):  
    res = res + s.pop()

  return res

# Good que
# Text Editor

def text_editor(text, pattern): # text = 'Hello' , pattern = "uurur"

  undo = Stack()
  redo = Stack()

  for i in text:
    undo.push(i)

  for i in pattern:

    if i == "u":
      data = undo.pop()
      redo.push(data)
    else:
      data = redo.pop()
      undo.push(data)

  #printing part
  res = ""
  while(not undo.isempty()):
    res = undo.pop() + res
  print(res)



text_editor("Kolkata", "uuurr")

#_______________________________________________________________________________

# leetcode |  Balanced parentheses | Valid-Parentheses (Homework)


#_______________________________________________________________________________
# Celebrity problem 
    ## https://www.geeksforgeeks.org/problems/the-celebrity-problem/1 
    
L = [
  [0,0,1,0],  # 0 -> knows 2
  [0,0,1,0],  # 1 -> knows 2
  [1,0,0,1],  # 2 -> knows 0 and 3
  [0,0,1,0]   # 3 -> knows 2
]

def celebrity(L):

  s = Stack()

  for i in range(len(L)):
    s.push(i)

  while s.size() >= 2:

    a = s.pop()
    b = s.pop()

    if  L[a][b] == 0:
      # b is not a celeb
      s.push(a)
      
    else:
      # a is not a celeb
      s.push(b)

  celeb = s.pop()

  for i in range(len(L)):

    if i == celeb: # if i is celebrity
      continue

    #check celeb is know by all OR celeb does not know anyone 
    if  L[celeb][i] == 1 or L[i][celeb] == 0:
      return -1

  return celeb

print(celebrity(L))