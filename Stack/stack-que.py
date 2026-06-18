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

