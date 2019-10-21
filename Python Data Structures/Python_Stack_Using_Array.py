'''
STACK OPERATIONS

push() :- pushed at the top of the stack
pop() :- removes the top element and returns it

Note :-
A stack is both Abstract Data Type(ADT) and Data Structure

ADT :-
Abstract Data type (ADT) is a type (or class) for objects whose behaviour is defined by a set of value and a set of operations.
So a user only needs to know what a data type can do, but not how it will be implemented.
Think of ADT as a black box which hides the inner structure and design of the data type.
'''

SIZE = 10
S = [0]*(SIZE+1) #to initialize the list
top = 0

def is_empty():
  if top==0:
    return True
  return False

def push(x):
  global top
  top = top+1
  if top>SIZE:
    print("Stackoverflow")
  else:
    S[top] = x

def pop():
  global top
  if is_empty():
    print("Stackunderflow")
  else:
    top = top-1
    return S[top+1]

if __name__ == '__main__':
  pop()
  push(10)
  push(20)
  push(30)
  push(40)
  push(50)
  push(60)
  push(70)
  push(80)
  push(90)
  push(100)
  push(110)



  print(S[1:SIZE+1])